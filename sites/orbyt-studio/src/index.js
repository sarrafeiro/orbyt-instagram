// Servidor do site da Orbyt (Cloudflare Worker).
// As páginas continuam saindo da pasta public/. Este código só responde em /api/...
//
// Segredos (Cloudflare > orbyt-studio > Settings > Variables and Secrets, tipo Secret):
//   MP_ACCESS_TOKEN  Access Token de PRODUÇÃO da aplicação "Orbyt Medicina" no Mercado Pago
//   PDF_KEY          chave que abre o PDF criptografado (src/40prompts.bin)
//   RESEND_API_KEY   (opcional) se existir, o PDF também vai por e-mail

import PDF_CRIPTO from "./40prompts.bin";

const PRODUTO = {
  nome: "40 Prompts para Estudar Medicina com IA",
  preco: "27.90",
  arquivo: "40-prompts-medicina-ia.pdf",
  prefixo: "40p",
};
const MP = "https://api.mercadopago.com";

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    const p = url.pathname;
    try {
      if (p === "/api/mp/pix" && req.method === "POST") return await criarPix(req, env, url, ctx);
      if (p === "/api/mp/cartao" && req.method === "POST") return await criarCartao(req, env, url, ctx);
      if (p === "/api/mp/status" && req.method === "GET") return await status(env, url, ctx);
      if (p === "/api/mp/webhook") return await webhook(req, env, url, ctx);
      if (p === "/api/download" && req.method === "GET") return await download(env, url);
      if (p === "/api/saude") return await saude(env);
      if (p === "/api/oa/evento" && req.method === "POST") return await eventoOa(req, env, ctx);
      if (p.startsWith("/api/")) return json({ erro: "rota não existe" }, 404);
    } catch (e) {
      console.log("erro", p, e && e.stack || e);
      return json({ erro: "falha no servidor" }, 500);
    }
    return env.ASSETS.fetch(req);
  },
};

// ---------- criação de pagamentos ----------

function lerComprador(b) {
  const nome = String(b.nome || "").trim().replace(/\s+/g, " ").slice(0, 120);
  const email = String(b.email || "").trim().toLowerCase().slice(0, 160);
  const cpf = String(b.cpf || "").replace(/\D/g, "");
  if (nome.split(" ").length < 2) throw new ErroCliente("Digite nome e sobrenome.");
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) throw new ErroCliente("Confira o e-mail.");
  if (!cpfOk(cpf)) throw new ErroCliente("CPF inválido.");
  const partes = nome.split(" ");
  return {
    email,
    first_name: partes[0],
    last_name: partes.slice(1).join(" "),
    identification: { type: "CPF", number: cpf },
  };
}

function baseOrder(payer, metodo) {
  return {
    type: "online",
    processing_mode: "automatic",
    total_amount: PRODUTO.preco,
    external_reference: PRODUTO.prefixo + "-" + metodo + "-" + crypto.randomUUID().slice(0, 18),
    description: PRODUTO.nome,
    payer,
    items: [{ title: PRODUTO.nome, unit_price: PRODUTO.preco, quantity: 1 }],
  };
}

async function criarPix(req, env, url, ctx) {
  let b, payer;
  try { b = await req.json(); payer = lerComprador(b); } catch (e) { return erroCliente(e); }
  const corpo = baseOrder(payer, "pix");
  corpo.transactions = { payments: [{ amount: PRODUTO.preco, payment_method: { id: "pix", type: "bank_transfer" }, expiration_time: "PT30M" }] };
  const r = await mp(env, "POST", "/v1/orders", corpo);
  if (!r.ok) { console.log("pix falhou", r.status, JSON.stringify(r.data)); return json({ erro: "Não deu para gerar o Pix agora. Tente de novo." }, 502); }
  await guardarComprador(env, r.data.id, payer, atribuicao(req, b));
  const pg = (((r.data.transactions || {}).payments || [])[0] || {}).payment_method || {};
  return json({ id: r.data.id, status: r.data.status, qr_code: pg.qr_code, qr_code_base64: pg.qr_code_base64, ticket_url: pg.ticket_url });
}

async function criarCartao(req, env, url, ctx) {
  let b, payer;
  try { b = await req.json(); payer = lerComprador(b); } catch (e) { return erroCliente(e); }
  if (!b.token || !b.payment_method_id) return json({ erro: "Confira os dados do cartão." }, 400);
  const corpo = baseOrder(payer, "cartao");
  const tipo = b.payment_type_id === "debit_card" ? "debit_card" : "credit_card";
  corpo.transactions = { payments: [{ amount: PRODUTO.preco, payment_method: { id: String(b.payment_method_id), type: tipo, token: String(b.token), installments: 1 } }] };
  const r = await mp(env, "POST", "/v1/orders", corpo);
  const o = r.data || {};
  if (o.id) await guardarComprador(env, o.id, payer, atribuicao(req, b));
  const pgto = ((o.transactions || {}).payments || [])[0] || {};
  const det = pgto.status_detail || o.status_detail || (o.errors && o.errors[0] && o.errors[0].code) || "";
  if (o.status === "processed") {
    ctx.waitUntil(posVenda(env, url, o));
    return json({ id: o.id, status: "processed", download: await linkDownload(env, url, o.id) });
  }
  if (o.status === "processing" || o.status === "action_required") {
    return json({ id: o.id, status: o.status });
  }
  console.log("cartao recusado", r.status, JSON.stringify(o).slice(0, 1500));
  return json({ id: o.id || null, status: "failed", motivo: motivoCartao(det) });
}

function motivoCartao(d) {
  d = String(d || "");
  if (/insufficient|amount/.test(d)) return "O cartão não tem limite para esta compra. Tente outro cartão ou pague com Pix.";
  if (/security_code|cvv/.test(d)) return "O código de segurança não confere. Confira e tente de novo.";
  if (/expiration|date/.test(d)) return "A validade do cartão não confere. Confira e tente de novo.";
  if (/high_risk|fraud|blacklist/.test(d)) return "O pagamento não foi aprovado por segurança. Pague com Pix, aprova na hora.";
  if (/call_for_authorize|authorize/.test(d)) return "O banco pediu autorização. Libere a compra no app do banco e tente de novo, ou pague com Pix.";
  return "O cartão foi recusado. Tente outro cartão ou pague com Pix, aprova na hora.";
}

// ---------- status, webhook e entrega ----------

async function status(env, url, ctx) {
  const id = url.searchParams.get("id") || "";
  if (!/^ORD[0-9A-Z]{10,40}$/.test(id)) return json({ erro: "pedido inválido" }, 400);
  const r = await mp(env, "GET", "/v1/orders/" + id);
  if (!r.ok) return json({ status: "desconhecido" }, 200);
  const o = r.data;
  if (!String(o.external_reference || "").startsWith(PRODUTO.prefixo + "-")) return json({ erro: "pedido inválido" }, 400);
  const saida = { id: o.id, status: o.status };
  if (o.status === "processed") {
    saida.download = await linkDownload(env, url, o.id);
    ctx.waitUntil(posVenda(env, url, o));
  }
  return json(saida);
}

async function webhook(req, env, url, ctx) {
  // O aviso do Mercado Pago só diz "o pedido X mudou". A gente confere direto na API, sem confiar no corpo.
  let id = url.searchParams.get("data.id") || url.searchParams.get("id") || "";
  if (!id && req.method === "POST") {
    try { const b = await req.json(); id = (b.data && b.data.id) || b.id || ""; } catch (e) {}
  }
  id = String(id);
  if (/^ORD[0-9A-Z]{10,40}$/.test(id)) {
    ctx.waitUntil((async () => {
      const r = await mp(env, "GET", "/v1/orders/" + id);
      if (r.ok && r.data.status === "processed" && String(r.data.external_reference || "").startsWith(PRODUTO.prefixo + "-")) {
        console.log("venda aprovada", id, r.data.external_reference);
        await posVenda(env, url, r.data);
      }
    })());
  }
  return new Response("ok", { status: 200 });
}

async function download(env, url) {
  const id = url.searchParams.get("id") || "";
  const t = url.searchParams.get("t") || "";
  if (!/^ORD[0-9A-Z]{10,40}$/.test(id) || t !== (await assinar(env, id))) return paginaErro("Link inválido. Use o botão da página de compra ou o link do e-mail.");
  const r = await mp(env, "GET", "/v1/orders/" + id);
  if (!r.ok || r.data.status !== "processed") return paginaErro("Ainda não encontramos o pagamento deste pedido. Se você acabou de pagar, espere alguns segundos e abra de novo.");
  const pdf = await abrirPdf(env);
  return new Response(pdf, {
    headers: {
      "content-type": "application/pdf",
      "content-disposition": 'attachment; filename="' + PRODUTO.arquivo + '"',
      "cache-control": "private, no-store",
    },
  });
}

async function abrirPdf(env) {
  const bruto = new Uint8Array(PDF_CRIPTO);
  const chave = await crypto.subtle.importKey("raw", b64(env.PDF_KEY), "AES-GCM", false, ["decrypt"]);
  return crypto.subtle.decrypt({ name: "AES-GCM", iv: bruto.slice(0, 12) }, chave, bruto.slice(12));
}

async function linkDownload(env, url, id) {
  return url.origin + "/api/download?id=" + id + "&t=" + (await assinar(env, id));
}

async function assinar(env, id) {
  const k = await crypto.subtle.importKey("raw", new TextEncoder().encode("dl:" + env.MP_ACCESS_TOKEN), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const s = new Uint8Array(await crypto.subtle.sign("HMAC", k, new TextEncoder().encode(id)));
  return [...s.slice(0, 16)].map((x) => x.toString(16).padStart(2, "0")).join("");
}

// E-mail pós-compra com o PDF anexado e o link de download (Resend).
// Só funciona com RESEND_API_KEY criada. A chave de idempotência garante 1 e-mail por pedido,
// mesmo que o webhook e a página de compra confirmem o pagamento ao mesmo tempo.
async function enviarEmail(env, url, o) {
  if (!env.RESEND_API_KEY) return;
  const comp = env.PEDIDOS ? await env.PEDIDOS.get("pedido:" + o.id, "json") : null;
  const email = (comp && comp.email) || (o.payer && o.payer.email);
  if (!email) { console.log("pedido sem e-mail", o.id); return; }
  if (comp && comp.emailEnviado) return;
  const link = await linkDownload(env, url, o.id);
  const nome = ((comp && comp.first_name) || (o.payer && o.payer.first_name) || "").trim();
  const pdf = await abrirPdf(env);
  const html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.55;color:#16181B;max-width:520px;margin:0 auto;padding:24px">'
    + '<p style="margin:0 0 16px">' + (nome ? "Oi, " + escapar(nome) + "!" : "Oi!") + " Pagamento aprovado.</p>"
    + '<p style="margin:0 0 16px">O seu <b>' + PRODUTO.nome + "</b> está anexado neste e-mail. Se preferir, baixe pelo botão:</p>"
    + '<p style="margin:0 0 24px"><a href="' + link + '" style="display:inline-block;background:#FF5A1F;color:#ffffff;padding:13px 22px;border-radius:999px;text-decoration:none;font-weight:bold">Baixar o PDF</a></p>'
    + '<p style="margin:0 0 8px"><b>Próximo passo:</b> abra o PDF, copie o Prompt 1 e cole na sua IA. Ele coloca a conversa no nível de um estudante de Medicina.</p>'
    + '<p style="margin:24px 0 0;color:#5B6470;font-size:13px">Orbyt Studio para Medicina · orbytstudio.com.br<br>Pedido ' + o.id + "</p></div>";
  const texto = "Pagamento aprovado. O seu " + PRODUTO.nome + " está anexado. Link para baixar: " + link;
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { authorization: "Bearer " + env.RESEND_API_KEY, "content-type": "application/json", "idempotency-key": "pedido-" + o.id },
    body: JSON.stringify({
      from: env.EMAIL_DE || "Orbyt Studio para Medicina <medicina@orbytstudio.com.br>",
      reply_to: "medicina@orbytstudio.com.br",
      to: [email],
      subject: "Seu PDF chegou: " + PRODUTO.nome,
      html, text: texto,
      attachments: [{ filename: PRODUTO.arquivo, content: paraB64(new Uint8Array(pdf)) }],
    }),
  });
  if (r.ok) {
    if (comp && env.PEDIDOS) await env.PEDIDOS.put("pedido:" + o.id, JSON.stringify(Object.assign(comp, { emailEnviado: new Date().toISOString() })), { expirationTtl: 60 * 60 * 24 * 90 });
    console.log("email enviado", o.id);
  }
  else console.log("email falhou", o.id, r.status, (await r.text()).slice(0, 500));
}

// Guarda e-mail e nome do comprador por 90 dias. O Mercado Pago não devolve esses dados na consulta do pedido.
async function guardarComprador(env, id, payer, atrib) {
  if (!env.PEDIDOS || !id) return;
  await env.PEDIDOS.put("pedido:" + id, JSON.stringify(Object.assign({ email: payer.email, first_name: payer.first_name, last_name: payer.last_name, criado: new Date().toISOString() }, atrib || {})), { expirationTtl: 60 * 60 * 24 * 90 });
}

// ---------- ChatGPT Ads: API de conversão (servidor) ----------
// Pixel "Orbyt Medicina - 40 Prompts". Chave em OPENAI_CAPI_KEY (Secret). Sem a chave, não envia nada.
const OA_PIXEL = "9XiKvStxRXDEi93APHe2ak";
const OA_ORIGEM = "https://orbytstudio.com.br";

function atribuicao(req, b) {
  const t = (v, n) => (typeof v === "string" && v.trim() ? v.trim().slice(0, n) : undefined);
  return {
    oppref: t(b && b.oppref, 512),
    obref: t(b && b.obref, 128),
    ip: t(req.headers.get("cf-connecting-ip"), 64),
    ua: t(req.headers.get("user-agent"), 512),
  };
}

function oaProduto(comValor) {
  const d = { type: "contents", contents: [{ id: "40-prompts-medicina", name: PRODUTO.nome, content_type: "product", quantity: 1 }] };
  if (comValor) { d.amount = Math.round(Number(PRODUTO.preco) * 100); d.currency = "BRL"; }
  return d;
}

async function capi(env, eventos) {
  if (!env.OPENAI_CAPI_KEY) return false;
  const r = await fetch("https://bzr.openai.com/v1/events?pid=" + OA_PIXEL, {
    method: "POST",
    headers: { authorization: "Bearer " + env.OPENAI_CAPI_KEY, "content-type": "application/json" },
    body: JSON.stringify({ validate_only: false, events: eventos }),
  });
  if (!r.ok) console.log("capi falhou", r.status, (await r.text()).slice(0, 500));
  return r.ok;
}

function usuarioBase(a) {
  const u = { countries: ["BR"] };
  if (a.obref) u.obref = a.obref;
  if (a.ip) u.ip_address = a.ip;
  if (a.ua) u.user_agent = a.ua;
  return u;
}

// LP vista e checkout iniciado: o navegador manda o mesmo ID que usou no pixel.
async function eventoOa(req, env, ctx) {
  let b;
  try { b = await req.json(); } catch (e) { return json({ erro: "inválido" }, 400); }
  const tipos = { page_viewed: false, checkout_started: true };
  if (!(b.type in tipos) || !/^[A-Za-z0-9_.-]{6,80}$/.test(String(b.id || ""))) return json({ erro: "inválido" }, 400);
  let fonte = OA_ORIGEM + "/40prompts-estudante-medicina/";
  try { const u = new URL(String(b.source_url)); if (u.origin === OA_ORIGEM) fonte = u.origin + u.pathname; } catch (e) {}
  const a = atribuicao(req, b);
  const ev = { id: String(b.id), type: b.type, timestamp_ms: Date.now(), source_url: fonte, action_source: "web", user: usuarioBase(a), data: oaProduto(tipos[b.type]) };
  if (b.type === "page_viewed") ev.data = { type: "contents", contents: [{ id: "lp-40-prompts", name: "LP 40 Prompts Medicina", content_type: "page" }] };
  if (a.oppref) ev.oppref = a.oppref;
  ctx.waitUntil(capi(env, [ev]));
  return json({ ok: true });
}

// Compra: mesmo ID do pedido que o pixel usa como event_id.
async function conversaoCompra(env, o) {
  if (!env.OPENAI_CAPI_KEY || !env.PEDIDOS) return;
  const comp = await env.PEDIDOS.get("pedido:" + o.id, "json");
  if (!comp || comp.capiEnviado) return;
  const u = usuarioBase(comp);
  if (comp.email) u.emails_sha256 = [await sha256(comp.email.trim().toLowerCase())];
  if (comp.first_name) u.first_names_sha256 = [await sha256(normNome(comp.first_name))];
  if (comp.last_name) u.last_names_sha256 = [await sha256(normNome(comp.last_name))];
  const ev = { id: o.id, type: "order_created", timestamp_ms: Date.now(), source_url: OA_ORIGEM + "/40prompts-estudante-medicina/checkout/", action_source: "web", user: u, data: oaProduto(true) };
  if (comp.oppref) ev.oppref = comp.oppref;
  if (await capi(env, [ev])) {
    const atual = (await env.PEDIDOS.get("pedido:" + o.id, "json")) || comp;
    atual.capiEnviado = new Date().toISOString();
    await env.PEDIDOS.put("pedido:" + o.id, JSON.stringify(atual), { expirationTtl: 60 * 60 * 24 * 90 });
    console.log("capi compra enviada", o.id);
  }
}

async function posVenda(env, url, o) {
  try { await enviarEmail(env, url, o); } catch (e) { console.log("email erro", e && e.stack || e); }
  try { await conversaoCompra(env, o); } catch (e) { console.log("capi erro", e && e.stack || e); }
}

async function sha256(t) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(t)); return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join(""); }
function normNome(t) { return String(t || "").toLowerCase().replace(/[\s!-\/:-@\[-`{-~]/g, ""); }

function paraB64(u) { let s = ""; for (let i = 0; i < u.length; i += 0x8000) s += String.fromCharCode.apply(null, u.subarray(i, i + 0x8000)); return btoa(s); }
function escapar(t) { return String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

// Checagem rápida: confirma que as duas chaves funcionam, sem mostrar nenhuma delas.
async function saude(env) {
  let mpOk = false, pdfOk = false;
  try { const r = await fetch(MP + "/users/me", { headers: { authorization: "Bearer " + env.MP_ACCESS_TOKEN } }); mpOk = r.ok; } catch (e) {}
  try { const b = new Uint8Array(await abrirPdf(env)); pdfOk = b[0] === 0x25 && b[1] === 0x50; } catch (e) {}
  return json({ mercado_pago: mpOk, pdf: pdfOk, email: !!env.RESEND_API_KEY, pedidos: !!env.PEDIDOS, chatgpt_capi: !!env.OPENAI_CAPI_KEY });
}

// ---------- utilitários ----------

async function mp(env, metodo, caminho, corpo) {
  const h = { authorization: "Bearer " + env.MP_ACCESS_TOKEN, accept: "application/json" };
  if (corpo) { h["content-type"] = "application/json"; h["x-idempotency-key"] = crypto.randomUUID(); }
  const r = await fetch(MP + caminho, { method: metodo, headers: h, body: corpo ? JSON.stringify(corpo) : undefined });
  let data = {};
  try { data = await r.json(); } catch (e) {}
  return { ok: r.ok, status: r.status, data };
}

class ErroCliente extends Error {}
function erroCliente(e) { return json({ erro: e instanceof ErroCliente ? e.message : "Dados inválidos." }, 400); }

function json(d, s = 200) {
  return new Response(JSON.stringify(d), { status: s, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });
}

function paginaErro(msg) {
  return new Response('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orbyt Studio</title><div style="font-family:Arial,sans-serif;max-width:480px;margin:15vh auto;padding:24px;text-align:center;color:#16181B"><h2>Quase lá</h2><p>' + msg + '</p><p><a href="/40prompts-estudante-medicina/checkout/">Voltar para a página de compra</a></p></div>', { status: 403, headers: { "content-type": "text/html; charset=utf-8" } });
}

function b64(s) { const bin = atob(String(s || "").trim()); const u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); return u; }

function cpfOk(d) {
  if (d.length !== 11 || /^(\d)\1+$/.test(d)) return false;
  for (let t = 9; t < 11; t++) {
    let soma = 0;
    for (let i = 0; i < t; i++) soma += +d[i] * (t + 1 - i);
    if (((soma * 10) % 11) % 10 !== +d[t]) return false;
  }
  return true;
}
