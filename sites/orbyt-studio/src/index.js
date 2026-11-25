// Servidor do site da Orbyt (Cloudflare Worker).
// As páginas continuam saindo da pasta public/. Este código só responde em /api/...
//
// Segredos (Cloudflare > orbyt-studio > Settings > Variables and Secrets, tipo Secret):
//   MP_ACCESS_TOKEN  Access Token de PRODUÇÃO da aplicação "Orbyt Medicina" no Mercado Pago
//   PDF_KEY          chave que abre os PDFs criptografados (src/40prompts.bin e public/.../dl/*.bin)
//   RESEND_API_KEY   (opcional) se existir, o PDF também vai por e-mail

import PDF_CRIPTO from "./40prompts.bin";

const PRODUTO = {
  nome: "40 Prompts para Estudar Medicina com IA",
  preco: "29.90",
  centavos: 2990,
  arquivo: "40-prompts-medicina-ia.pdf",
  prefixo: "40p",
};

// ---------- extras do checkout (order bump), por fase do curso ----------
// A pessoa escolhe a fase e marca o que quer. Os 3 juntos saem pelo preço do combo e levam o bônus.
// Os PDFs ficam criptografados (mesma PDF_KEY) em public/40prompts-estudante-medicina/dl/.
const FASES = {
  1: { slug: "ciclo-basico", rotulo: "ciclo básico", ano: "2º ano" },
  2: { slug: "ciclo-clinico", rotulo: "ciclo clínico", ano: "4º ano" },
  3: { slug: "internato", rotulo: "internato", ano: "6º ano" },
};
const EXTRAS = {
  osce: { letra: "o", centavos: 890, titulo: (f) => "OSCE: 32 estações do " + f.rotulo, arquivo: (f) => "osce-" + f.slug + ".pdf" },
  enamed: { letra: "e", centavos: 890, titulo: (f) => "Simulados ENAMED do " + f.ano, arquivo: (f) => "simulados-enamed-" + f.ano.charAt(0) + "-ano.pdf" },
  kit: { letra: "k", centavos: 690, titulo: (f) => "Kit de prompts do " + f.rotulo, arquivo: (f) => "kit-de-prompts-" + f.slug + ".pdf" },
};
const ORDEM_EXTRAS = ["osce", "enamed", "kit"];
const COMBO_CENTAVOS = 1290;
const BONUS = { chave: "academico", titulo: "Kit Acadêmico: seminário, artigo e TCC (bônus)", arquivo: "kit-academico.pdf", bin: "academico" };
const DIR_EXTRAS = "/40prompts-estudante-medicina/dl/";

function reais(c) { return (c / 100).toFixed(2); }

// O que veio do navegador: fase (1 a 3) e itens marcados. O preço é sempre calculado aqui.
function lerSelecao(b) {
  const fase = [1, 2, 3].includes(Number(b && b.fase)) ? Number(b.fase) : 0;
  const marcados = Array.isArray(b && b.itens) ? b.itens.map(String) : [];
  return { fase, itens: fase ? ORDEM_EXTRAS.filter((k) => marcados.includes(k)) : [] };
}

function totalCentavos(sel) {
  if (sel.preco) return sel.preco;   // oferta do e-mail de recuperação: preço fechado
  if (sel.itens.length === 3) return PRODUTO.centavos + COMBO_CENTAVOS;
  return PRODUTO.centavos + sel.itens.reduce((s, k) => s + EXTRAS[k].centavos, 0);
}

// A seleção viaja dentro da referência do pedido no Mercado Pago (ex.: 40p-pix-f3oek-...),
// então a entrega não depende de nenhum outro registro.
function refDe(metodo, sel) {
  const marca = (sel.fase ? "f" + sel.fase + sel.itens.map((k) => EXTRAS[k].letra).join("") + "-" : "") + (sel.preco ? "of" + sel.preco + "-" : "");
  return PRODUTO.prefixo + "-" + metodo + "-" + marca + crypto.randomUUID().slice(0, 18);
}

function selecaoDaRef(ref) {
  ref = String(ref || "");
  const m = /^40p-(?:pix|cartao)-f([123])([oek]{0,3})-/.exec(ref);
  const of = /^40p-(?:pix|cartao)-(?:f[123][oek]{0,3}-)?of(\d{3,5})-/.exec(ref);
  const sel = m ? { fase: Number(m[1]), itens: ORDEM_EXTRAS.filter((k) => m[2].includes(EXTRAS[k].letra)) } : { fase: 0, itens: [] };
  if (of) sel.preco = Number(of[1]);
  return sel;
}

function itensMp(sel) {
  const l = [{ title: PRODUTO.nome, unit_price: PRODUTO.preco, quantity: 1 }];
  const f = FASES[sel.fase];
  if (sel.preco) return [{ title: sel.itens.length === 3 && f ? "Oferta: 40 Prompts + pacote do " + f.rotulo + " + bônus" : PRODUTO.nome + " (oferta)", unit_price: reais(sel.preco), quantity: 1 }];
  if (!f || !sel.itens.length) return l;
  if (sel.itens.length === 3) l.push({ title: "Combo " + f.rotulo + ": OSCE + Simulados ENAMED + Kit de prompts", unit_price: reais(COMBO_CENTAVOS), quantity: 1 });
  else for (const k of sel.itens) l.push({ title: EXTRAS[k].titulo(f), unit_price: reais(EXTRAS[k].centavos), quantity: 1 });
  return l;
}

// Arquivos a que o pedido dá direito. O primeiro é sempre o guia principal.
function arquivosDe(sel) {
  const l = [{ chave: "principal", titulo: PRODUTO.nome, arquivo: PRODUTO.arquivo }];
  const f = FASES[sel.fase];
  if (!f) return l;
  for (const k of sel.itens) l.push({ chave: k, titulo: EXTRAS[k].titulo(f), arquivo: EXTRAS[k].arquivo(f), bin: "f" + sel.fase + "-" + k });
  if (sel.itens.length === 3) l.push({ chave: BONUS.chave, titulo: BONUS.titulo, arquivo: BONUS.arquivo, bin: BONUS.bin });
  return l;
}
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
      if (p === "/api/saude/capi") {
        const r = await fetch("https://bzr.openai.com/v1/events?pid=" + OA_PIXEL, { method: "POST", headers: { authorization: "Bearer " + env.OPENAI_CAPI_KEY, "content-type": "application/json" }, body: JSON.stringify({ validate_only: true, events: [{ id: "teste-validacao-1", type: "page_viewed", timestamp_ms: Date.now(), source_url: OA_ORIGEM + "/40prompts-estudante-medicina/", action_source: "web", user: { countries: ["BR"], external_ids_sha256: [await sha256("teste-validacao")] }, data: { type: "contents" } }] }) });
        return json({ validacao: { status: r.status, resposta: (await r.text()).slice(0, 800) }, ultima_compra_ou_falha: env.PEDIDOS ? await env.PEDIDOS.get("diag:capi", "json") : null });
      }
      if (p === "/api/saude/extras") return await saudeExtra(env, url);
      if (p === "/api/saude") return await saude(env);
      if (p === "/api/oa/evento" && req.method === "POST") return await eventoOa(req, env, ctx);
      if (p === "/api/funil/sessao" && req.method === "POST") return await funilSessao(req, env);
      if (p === "/api/funil/lp" && req.method === "POST") return await funilLp(req, env);
      if (p === "/api/funil" && req.method === "GET") return await funilRelatorio(env, url);
      if (p === "/api/oferta" && req.method === "GET") return await ofertaVer(env, url);
      if (p === "/api/sair") return await recSair(req, env, url);
      if (p === "/api/recupera" && req.method === "GET") return await recAdmin(env, url, ctx);
      if (p.startsWith("/api/")) return json({ erro: "rota não existe" }, 404);
    } catch (e) {
      console.log("erro", p, e && e.stack || e);
      return json({ erro: "falha no servidor" }, 500);
    }
    return env.ASSETS.fetch(req);
  },
  // Roda a cada minuto (wrangler.jsonc > triggers): manda os e-mails de recuperação que estão na hora.
  async scheduled(ev, env, ctx) {
    ctx.waitUntil(recuperar(env).catch((e) => console.log("recuperar erro", (e && e.stack) || e)));
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

function baseOrder(payer, metodo, sel) {
  return {
    type: "online",
    processing_mode: "automatic",
    total_amount: reais(totalCentavos(sel)),
    external_reference: refDe(metodo, sel),
    description: PRODUTO.nome + (sel.itens.length ? " + extras do " + FASES[sel.fase].rotulo : ""),
    payer,
    items: itensMp(sel),
  };
}

async function criarPix(req, env, url, ctx) {
  let b, payer;
  let sel;
  try { b = await req.json(); payer = lerComprador(b); sel = await selecaoFinal(env, b); } catch (e) { return erroCliente(e); }
  const corpo = baseOrder(payer, "pix", sel);
  corpo.transactions = { payments: [{ amount: corpo.total_amount, payment_method: { id: "pix", type: "bank_transfer" }, expiration_time: "PT30M" }] };
  const r = await mp(env, "POST", "/v1/orders", corpo);
  if (!r.ok) { console.log("pix falhou", r.status, JSON.stringify(r.data)); return json({ erro: "Não deu para gerar o Pix agora. Tente de novo." }, 502); }
  await guardarComprador(env, r.data.id, payer, atribuicao(req, b), sel, "pix");
  ctx.waitUntil(funilConverteu(env, b.sid));
  const pg = (((r.data.transactions || {}).payments || [])[0] || {}).payment_method || {};
  await recRegistrar(env, { email: payer.email, nome: payer.first_name, sel, pedido: r.data.id, metodo: "pix", qr: pg.qr_code, ticket: pg.ticket_url });
  return json({ id: r.data.id, status: r.data.status, total: totalCentavos(sel), qr_code: pg.qr_code, qr_code_base64: pg.qr_code_base64, ticket_url: pg.ticket_url });
}

async function criarCartao(req, env, url, ctx) {
  let b, payer;
  let sel;
  try { b = await req.json(); payer = lerComprador(b); sel = await selecaoFinal(env, b); } catch (e) { return erroCliente(e); }
  if (!b.token || !b.payment_method_id) return json({ erro: "Confira os dados do cartão." }, 400);
  const corpo = baseOrder(payer, "cartao", sel);
  const tipo = b.payment_type_id === "debit_card" ? "debit_card" : "credit_card";
  corpo.transactions = { payments: [{ amount: corpo.total_amount, payment_method: { id: String(b.payment_method_id), type: tipo, token: String(b.token), installments: 1 } }] };
  const r = await mp(env, "POST", "/v1/orders", corpo);
  const o = r.data || {};
  if (o.id) {
    await guardarComprador(env, o.id, payer, atribuicao(req, b), sel, "cartao");
    ctx.waitUntil(funilConverteu(env, b.sid));
    await recRegistrar(env, { email: payer.email, nome: payer.first_name, sel, pedido: o.id, metodo: "cartao" });
  }
  const pgto = ((o.transactions || {}).payments || [])[0] || {};
  const det = pgto.status_detail || o.status_detail || (o.errors && o.errors[0] && o.errors[0].code) || "";
  if (o.status === "processed") {
    ctx.waitUntil(posVenda(env, url, o));
    return json(Object.assign({ id: o.id, status: "processed" }, await entrega(env, url, o)));
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
    Object.assign(saida, await entrega(env, url, o));
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
  const pedido = url.searchParams.get("f") || "principal";
  const alvo = arquivosDe(selecaoDaRef(r.data.external_reference)).find((a) => a.chave === pedido);
  if (!alvo) return paginaErro("Este arquivo não faz parte do seu pedido.");
  const pdf = await abrirArquivo(env, url, alvo);
  return new Response(pdf, {
    headers: {
      "content-type": "application/pdf",
      "content-disposition": 'attachment; filename="' + alvo.arquivo + '"',
      "cache-control": "private, no-store",
    },
  });
}

async function decifrar(env, bruto) {
  const chave = await crypto.subtle.importKey("raw", b64(env.PDF_KEY), "AES-GCM", false, ["decrypt"]);
  return crypto.subtle.decrypt({ name: "AES-GCM", iv: bruto.slice(0, 12) }, chave, bruto.slice(12));
}

async function abrirPdf(env) {
  return decifrar(env, new Uint8Array(PDF_CRIPTO));
}

// Guia principal: vai dentro do servidor. Extras: ficam criptografados na pasta pública dl/.
async function abrirArquivo(env, url, a) {
  if (!a.bin) return abrirPdf(env);
  const r = await env.ASSETS.fetch(new Request(url.origin + DIR_EXTRAS + a.bin + ".bin"));
  if (!r.ok) throw new Error("extra fora do ar: " + a.bin + " " + r.status);
  return decifrar(env, new Uint8Array(await r.arrayBuffer()));
}

async function linkDownload(env, url, id, chave) {
  return url.origin + "/api/download?id=" + id + "&t=" + (await assinar(env, id)) + (chave && chave !== "principal" ? "&f=" + chave : "");
}

// O que a página de compra recebe quando o pagamento aprova: link do guia e de cada extra.
async function entrega(env, url, o) {
  const sel = selecaoDaRef(o.external_reference);
  const downloads = [];
  for (const a of arquivosDe(sel)) downloads.push({ chave: a.chave, titulo: a.titulo, url: await linkDownload(env, url, o.id, a.chave) });
  return { download: downloads[0].url, downloads, total: totalCentavos(sel), fase: sel.fase, itens: sel.itens };
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
  const nome = ((comp && comp.first_name) || (o.payer && o.payer.first_name) || "").trim();
  const arqs = [];
  for (const a of arquivosDe(selecaoDaRef(o.external_reference))) arqs.push(Object.assign({ url: await linkDownload(env, url, o.id, a.chave) }, a));
  const link = arqs[0].url, extras = arqs.slice(1);
  const pdf = await abrirPdf(env);
  const botao = (href, txt, cor) => '<a href="' + href + '" style="display:inline-block;background:' + cor + ';color:#ffffff;padding:13px 22px;border-radius:999px;text-decoration:none;font-weight:bold">' + txt + "</a>";
  let html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.55;color:#16181B;max-width:520px;margin:0 auto;padding:24px">'
    + '<p style="margin:0 0 16px">' + (nome ? "Oi, " + escapar(nome) + "!" : "Oi!") + " Pagamento aprovado.</p>"
    + '<p style="margin:0 0 16px">O seu <b>' + PRODUTO.nome + "</b> está anexado neste e-mail. Se preferir, baixe pelo botão:</p>"
    + '<p style="margin:0 0 24px">' + botao(link, "Baixar o PDF", "#FF5A1F") + "</p>";
  if (extras.length) {
    html += '<p style="margin:0 0 12px"><b>Seus extras</b> também estão liberados:</p>';
    for (const a of extras) html += '<p style="margin:0 0 12px">' + botao(a.url, "Baixar: " + escapar(a.titulo), "#16181B") + "</p>";
    html += '<p style="margin:0 0 24px"></p>';
  }
  html += '<p style="margin:0 0 8px"><b>Próximo passo:</b> abra o PDF, copie o Prompt 1 e cole na sua IA. Ele coloca a conversa no nível de um estudante de Medicina.</p>'
    + '<p style="margin:24px 0 0;color:#5B6470;font-size:13px">Orbyt Studio para Medicina · orbytstudio.com.br<br>Pedido ' + o.id + "</p></div>";
  let texto = "Pagamento aprovado. O seu " + PRODUTO.nome + " está anexado. Link para baixar: " + link;
  for (const a of extras) texto += "\n" + a.titulo + ": " + a.url;
  const principal = { filename: PRODUTO.arquivo, content: paraB64(new Uint8Array(pdf)) };
  const enviar = (anexos, chave) => fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { authorization: "Bearer " + env.RESEND_API_KEY, "content-type": "application/json", "idempotency-key": chave },
    body: JSON.stringify({
      from: env.EMAIL_DE || "Orbyt Studio para Medicina <medicina@orbytstudio.com.br>",
      reply_to: "medicina@orbytstudio.com.br",
      to: [email],
      subject: extras.length ? "Seus PDFs chegaram: 40 Prompts + extras" : "Seu PDF chegou: " + PRODUTO.nome,
      html, text: texto,
      attachments: anexos,
    }),
  });
  // Os extras vão como anexo buscado pelo próprio Resend no link de download. Se essa busca falhar,
  // manda só o guia anexado: os botões de download dos extras continuam no corpo do e-mail.
  let r = await enviar([principal].concat(extras.map((a) => ({ filename: a.arquivo, path: a.url }))), "pedido-" + o.id);
  if (!r.ok && extras.length) {
    console.log("email com extras falhou, indo só com o guia", o.id, r.status, (await r.text()).slice(0, 300));
    r = await enviar([principal], "pedido-" + o.id + "-guia");
  }
  if (r.ok) {
    if (comp && env.PEDIDOS) await salvarPedido(env, o.id, Object.assign(comp, { emailEnviado: new Date().toISOString() }));
    console.log("email enviado", o.id);
  }
  else console.log("email falhou", o.id, r.status, (await r.text()).slice(0, 500));
}

// Guarda e-mail e nome do comprador por 90 dias. O Mercado Pago não devolve esses dados na consulta do pedido.
async function guardarComprador(env, id, payer, atrib, sel, metodo) {
  if (!env.PEDIDOS || !id) return;
  const extra = sel ? { fase: sel.fase, itens: sel.itens, total: totalCentavos(sel), metodo: metodo || "" } : {};
  // Se a gravação falhar (cota do KV, instabilidade), a venda segue: o registro só serve para e-mail e relatório.
  try { await salvarPedido(env, id, Object.assign({ email: payer.email, first_name: payer.first_name, last_name: payer.last_name, criado: new Date().toISOString() }, extra, atrib || {})); }
  catch (e) { console.log("pedido não gravado", id, String((e && e.message) || e)); }
}

function diaBR(t) { return new Date((t || Date.now()) - 3 * 3600e3).toISOString().slice(0, 10); }

async function salvarPedido(env, id, o) {
  const meta = { d: diaBR(o.criado ? Date.parse(o.criado) : 0), f: o.fase || 0, x: (o.itens || []).map((k) => (EXTRAS[k] ? EXTRAS[k].letra : "")).join(""), t: o.total || PRODUTO.centavos, m: o.metodo || "", p: o.emailEnviado || o.capiEnviado ? 1 : 0 };
  await env.PEDIDOS.put("pedido:" + id, JSON.stringify(o), { expirationTtl: 60 * 60 * 24 * 90, metadata: meta });
}

// ---------- ChatGPT Ads: API de conversão (servidor) ----------
// Pixel "Orbyt Medicina - 40 Prompts", da conta de anúncios "Orbyt para Medicina" (criada em 18/11/2026).
// Chave em OPENAI_CAPI_KEY (Secret): tem de ser uma chave de conversão dessa mesma conta. Sem a chave, não envia nada.
const OA_PIXEL = "7CWbN3bYT15ftAS8pMju2m";
const OA_ORIGEM = "https://orbytstudio.com.br";

function atribuicao(req, b) {
  const t = (v, n) => (typeof v === "string" && v.trim() ? v.trim().slice(0, n) : undefined);
  return {
    oppref: t(b && b.oppref, 512),
    obref: t(b && b.obref, 128),
    vid: b && /^[a-f0-9]{24}$/.test(String(b.vid || "")) ? String(b.vid) : undefined,   // ID anônimo do visitante (LP e checkout)
    ip: t(req.headers.get("cf-connecting-ip"), 64),
    ua: t(req.headers.get("user-agent"), 512),
  };
}

function oaProduto(comValor, sel) {
  const d = { type: "contents", contents: [{ id: "40-prompts-medicina", name: PRODUTO.nome, content_type: "product", quantity: 1 }] };
  const f = sel && FASES[sel.fase];
  if (f) for (const k of sel.itens) d.contents.push({ id: "extra-" + k + "-" + f.slug, name: EXTRAS[k].titulo(f), content_type: "product", quantity: 1 });
  if (comValor) { d.amount = sel ? totalCentavos(sel) : PRODUTO.centavos; d.currency = "BRL"; }
  return d;
}

async function capi(env, eventos) {
  if (!env.OPENAI_CAPI_KEY) return false;
  const r = await fetch("https://bzr.openai.com/v1/events?pid=" + OA_PIXEL, {
    method: "POST",
    headers: { authorization: "Bearer " + env.OPENAI_CAPI_KEY, "content-type": "application/json" },
    body: JSON.stringify({ validate_only: false, events: eventos }),
  });
  const txt = (await r.text()).slice(0, 500);
  if (!r.ok) console.log("capi falhou", r.status, txt);
  await anotarCapi(env, r.status, txt, eventos, r.ok);
  return r.ok;
}

// Diagnóstico do envio (aparece em /api/saude/capi). Grava só a compra e as falhas, e a mesma falha
// no máximo 1 vez a cada 30 min. Gravar a cada visita da LP gastava a cota diária de gravações do KV.
async function anotarCapi(env, status, txt, eventos, ok) {
  if (!env.PEDIDOS) return;
  const compra = eventos.some((e) => e.type === "order_created");
  if (ok && !compra) return;
  try {
    if (!ok) {
      const ant = await env.PEDIDOS.get("diag:capi", "json");
      if (ant && ant.status === status && Date.now() - Date.parse(ant.quando) < 30 * 60e3) return;
    }
    await env.PEDIDOS.put("diag:capi", JSON.stringify({ quando: new Date().toISOString(), status, resposta: txt, tipos: eventos.map((e) => e.type) }), { expirationTtl: 60 * 60 * 24 * 30 });
  } catch (e) {}
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
  if (a.vid) ev.user.external_ids_sha256 = [await sha256(a.vid)];
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
  if (comp.vid) u.external_ids_sha256 = [await sha256(comp.vid)];
  if (comp.first_name) u.first_names_sha256 = [await sha256(normNome(comp.first_name))];
  if (comp.last_name) u.last_names_sha256 = [await sha256(normNome(comp.last_name))];
  const ev = { id: o.id, type: "order_created", timestamp_ms: Date.now(), source_url: OA_ORIGEM + "/40prompts-estudante-medicina/checkout/", action_source: "web", user: u, data: oaProduto(true, selecaoDaRef(o.external_reference)) };
  if (comp.oppref) ev.oppref = comp.oppref;
  if (await capi(env, [ev])) {
    const atual = (await env.PEDIDOS.get("pedido:" + o.id, "json")) || comp;
    atual.capiEnviado = new Date().toISOString();
    await salvarPedido(env, o.id, atual);
    console.log("capi compra enviada", o.id);
  }
}

async function posVenda(env, url, o) {
  try { await recPago(env, o); } catch (e) { console.log("rec pago erro", String((e && e.message) || e)); }
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
  let funil = env.FUNIL ? "d1" : "kv";
  if (env.FUNIL) { try { const db = await funilBanco(env); await db.prepare("SELECT 1 FROM sessao LIMIT 1").first(); } catch (e) { funil = "d1 com erro"; console.log("funil: banco com erro", String((e && e.message) || e)); } }
  return json({ mercado_pago: mpOk, pdf: pdfOk, email: !!env.RESEND_API_KEY, pedidos: !!env.PEDIDOS, chatgpt_capi: !!env.OPENAI_CAPI_KEY, funil });
}

// ---------- funil do checkout (tracking de produto, sem dado pessoal) ----------
// A página manda um resumo anônimo quando a pessoa sai sem gerar pedido: até onde ela chegou.
// Quem gera pedido já fica registrado em "pedido:". O relatório junta os dois: /api/funil?k=<senha>
// As sessões ficam no D1 (banco SQL da Cloudflare, binding FUNIL): 100 mil gravações por dia no plano grátis,
// contra 1.000 do KV. Sem o binding, cai no KV como era antes. Pedido continua no KV.
const FUNIL_HASH = "6ff70af390e6a4fcb4051ad704fac51a21fa599af4c36ae3e4f863035fb2a98b";
const funilFreio = new Map();
let funilPronto = false;

async function funilBanco(env) {
  if (!env.FUNIL) return null;
  if (!funilPronto) {
    await env.FUNIL.batch([
      env.FUNIL.prepare("CREATE TABLE IF NOT EXISTS sessao (sid TEXT PRIMARY KEY, dia TEXT NOT NULL, dados INTEGER NOT NULL DEFAULT 0, fase INTEGER NOT NULL DEFAULT 0, itens TEXT NOT NULL DEFAULT '', viu INTEGER NOT NULL DEFAULT 0, clicou INTEGER NOT NULL DEFAULT 0, seg INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID"),
      env.FUNIL.prepare("CREATE INDEX IF NOT EXISTS sessao_dia ON sessao (dia)"),
      env.FUNIL.prepare("CREATE TABLE IF NOT EXISTS lp (sid TEXT PRIMARY KEY, dia TEXT NOT NULL, tela INTEGER NOT NULL DEFAULT 1, clique TEXT NOT NULL DEFAULT '', seg INTEGER NOT NULL DEFAULT 0, anuncio TEXT NOT NULL DEFAULT '', mob INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID"),
      env.FUNIL.prepare("CREATE INDEX IF NOT EXISTS lp_dia ON lp (dia)"),
      env.FUNIL.prepare("CREATE TABLE IF NOT EXISTS lp2 (sid TEXT PRIMARY KEY, dia TEXT NOT NULL, tela INTEGER NOT NULL DEFAULT 1, clique TEXT NOT NULL DEFAULT '', seg INTEGER NOT NULL DEFAULT 0, anuncio TEXT NOT NULL DEFAULT '', mob INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID"),
      env.FUNIL.prepare("CREATE INDEX IF NOT EXISTS lp2_dia ON lp2 (dia)"),
      env.FUNIL.prepare("CREATE TABLE IF NOT EXISTS recupera (email TEXT PRIMARY KEY, nome TEXT NOT NULL DEFAULT '', fase INTEGER NOT NULL DEFAULT 0, itens TEXT NOT NULL DEFAULT '', pedido TEXT NOT NULL, metodo TEXT NOT NULL DEFAULT '', total INTEGER NOT NULL DEFAULT 0, qr TEXT NOT NULL DEFAULT '', ticket TEXT NOT NULL DEFAULT '', criado INTEGER NOT NULL, ultimo INTEGER NOT NULL, e1 INTEGER NOT NULL DEFAULT 0, e2 INTEGER NOT NULL DEFAULT 0, e3 INTEGER NOT NULL DEFAULT 0, pago INTEGER NOT NULL DEFAULT 0, sair INTEGER NOT NULL DEFAULT 0, chave TEXT NOT NULL, origem TEXT NOT NULL DEFAULT '') WITHOUT ROWID"),
      env.FUNIL.prepare("CREATE INDEX IF NOT EXISTS recupera_ultimo ON recupera (ultimo)"),
      env.FUNIL.prepare("CREATE INDEX IF NOT EXISTS recupera_criado ON recupera (criado)"),
    ]);
    funilPronto = true;
  }
  return env.FUNIL;
}

// Gerou pedido: a sessão sai da lista de abandono, para a mesma pessoa não contar duas vezes no relatório.
async function funilConverteu(env, sid) {
  sid = String(sid || "");
  if (!env.FUNIL || !/^[a-z0-9]{8,24}$/.test(sid)) return;
  try { const db = await funilBanco(env); await db.prepare("DELETE FROM sessao WHERE sid = ?1").bind(sid).run(); } catch (e) { console.log("funil: sessão não baixada", String((e && e.message) || e)); }
}

async function funilSessao(req, env) {
  if (!env.FUNIL && !env.PEDIDOS) return json({ ok: false });
  const origem = req.headers.get("origin");
  if (origem && !/^(https:\/\/(www\.)?orbytstudio\.com\.br|http:\/\/localhost(:\d+)?)$/.test(origem)) return json({ ok: false }, 403);
  const ip = req.headers.get("cf-connecting-ip") || "x", agora = Date.now(), f = funilFreio.get(ip) || [0, agora];
  if (agora - f[1] > 600e3) { f[0] = 0; f[1] = agora; }
  if (++f[0] > 6) return json({ ok: false }, 429);
  if (funilFreio.size > 5000) funilFreio.clear();
  funilFreio.set(ip, f);
  let b;
  try { const txt = await req.text(); if (txt.length > 600) return json({ ok: false }, 400); b = JSON.parse(txt); } catch (e) { return json({ ok: false }, 400); }
  const sid = String((b && b.sid) || "");
  if (!/^[a-z0-9]{8,24}$/.test(sid)) return json({ ok: false }, 400);
  const sel = lerSelecao(b);
  const meta = { d: b.dados ? 1 : 0, f: sel.fase, x: sel.itens.map((k) => EXTRAS[k].letra).join(""), v: b.viuPag ? 1 : 0, c: b.clicou ? 1 : 0, s: Math.max(0, Math.min(7200, Math.round(Number(b.seg) || 0))) };
  try {
    const db = await funilBanco(env);
    if (db) await db.prepare("INSERT INTO sessao (sid, dia, dados, fase, itens, viu, clicou, seg) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8) ON CONFLICT(sid) DO UPDATE SET dados = max(dados, excluded.dados), fase = CASE WHEN excluded.fase > 0 THEN excluded.fase ELSE fase END, itens = excluded.itens, viu = max(viu, excluded.viu), clicou = max(clicou, excluded.clicou), seg = max(seg, excluded.seg)").bind(sid, diaBR(), meta.d, meta.f, meta.x, meta.v, meta.c, meta.s).run();
    else await env.PEDIDOS.put("sessao:" + diaBR() + ":" + sid, "1", { metadata: meta, expirationTtl: 60 * 60 * 24 * 60 });
  } catch (e) { console.log("funil não gravado", String((e && e.message) || e)); }
  return json({ ok: true });
}

// ---------- tracking da LP (sem dado pessoal) ----------
// A LP avisa até qual tela a pessoa chegou, qual botão de compra tocou, quanto tempo ficou e de qual anúncio veio.
// Uma linha por visita (sid da aba), atualizada a cada aviso. Fica só no D1, 60 dias.
// LP v2 (no ar em 23/11/2026): página curta. As visitas da LP antiga (21 a 23/11) ficaram na tabela lp, com outras telas.
const LP_TELAS = ["capa", "diferenca", "frase", "jornada", "numeros", "oferta", "fim"];
const LP_TELA_NOME = ["Capa (demonstração)", "Com e sem prompt", "Frase", "Jornada dos 40", "Números", "Oferta e dúvidas", "Fim da página"];
const LP_BOTAO_NOME = { topo: "Barra do topo", capa: "Botão da capa", oferta: "Botão da oferta" };
const LP_TABELA = "lp2";
const lpFreio = new Map();

async function funilLp(req, env) {
  if (!env.FUNIL) return json({ ok: false });
  const origem = req.headers.get("origin");
  if (origem && !/^(https:\/\/(www\.)?orbytstudio\.com\.br|http:\/\/localhost(:\d+)?)$/.test(origem)) return json({ ok: false }, 403);
  const ip = req.headers.get("cf-connecting-ip") || "x", agora = Date.now(), f = lpFreio.get(ip) || [0, agora];
  if (agora - f[1] > 600e3) { f[0] = 0; f[1] = agora; }
  if (++f[0] > 20) return json({ ok: false }, 429);
  if (lpFreio.size > 5000) lpFreio.clear();
  lpFreio.set(ip, f);
  let b;
  try { const txt = await req.text(); if (txt.length > 400) return json({ ok: false }, 400); b = JSON.parse(txt); } catch (e) { return json({ ok: false }, 400); }
  const sid = String((b && b.sid) || "");
  if (!/^[a-z0-9]{8,24}$/.test(sid)) return json({ ok: false }, 400);
  const tela = Math.max(1, Math.min(LP_TELAS.length, Math.round(Number(b.tela) || 1)));
  const clique = Object.prototype.hasOwnProperty.call(LP_BOTAO_NOME, b.clique) ? b.clique : "";
  const anuncio = String(b.anuncio || "").replace(/[^A-Za-z0-9_-]/g, "").slice(0, 40);
  const seg = Math.max(0, Math.min(7200, Math.round(Number(b.seg) || 0)));
  try {
    const db = await funilBanco(env);
    await db.prepare("INSERT INTO " + LP_TABELA + " (sid, dia, tela, clique, seg, anuncio, mob) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7) ON CONFLICT(sid) DO UPDATE SET tela = max(tela, excluded.tela), clique = CASE WHEN clique = '' THEN excluded.clique ELSE clique END, seg = max(seg, excluded.seg), anuncio = CASE WHEN anuncio = '' THEN excluded.anuncio ELSE anuncio END").bind(sid, diaBR(), tela, clique, seg, anuncio, b.mob ? 1 : 0).run();
  } catch (e) { console.log("lp não gravada", String((e && e.message) || e)); }
  return json({ ok: true });
}

async function lpResumo(env, desde) {
  const db = await funilBanco(env);
  const q = (sql) => db.prepare(sql).bind(desde).all().then((r) => r.results || []);
  const [telas, botoes, anuncios, aparelhos, tempos, dias] = await Promise.all([
    q("SELECT tela, COUNT(*) AS n, SUM(clique <> '') AS k FROM " + LP_TABELA + " WHERE dia >= ?1 GROUP BY tela"),
    q("SELECT clique, COUNT(*) AS n FROM " + LP_TABELA + " WHERE dia >= ?1 AND clique <> '' GROUP BY clique ORDER BY n DESC"),
    q("SELECT anuncio, COUNT(*) AS v, SUM(tela >= 6) AS o, SUM(clique <> '') AS k FROM " + LP_TABELA + " WHERE dia >= ?1 GROUP BY anuncio ORDER BY v DESC"),
    q("SELECT mob, COUNT(*) AS v, SUM(clique <> '') AS k FROM " + LP_TABELA + " WHERE dia >= ?1 GROUP BY mob"),
    q("SELECT CASE WHEN seg < 5 THEN 0 WHEN seg < 15 THEN 1 WHEN seg < 30 THEN 2 WHEN seg < 60 THEN 3 ELSE 4 END AS f, COUNT(*) AS n FROM " + LP_TABELA + " WHERE dia >= ?1 AND clique = '' GROUP BY f"),
    q("SELECT dia, COUNT(*) AS v, SUM(clique <> '') AS k FROM " + LP_TABELA + " WHERE dia >= ?1 GROUP BY dia"),
  ]);
  const visitas = telas.reduce((a, l) => a + Number(l.n), 0), clicaram = telas.reduce((a, l) => a + Number(l.k || 0), 0);
  const chegou = LP_TELAS.map((_, i) => telas.filter((l) => l.tela >= i + 1).reduce((a, l) => a + Number(l.n), 0));
  const saiu = LP_TELAS.map((_, i) => { const l = telas.find((x) => x.tela === i + 1); return l ? Number(l.n) - Number(l.k || 0) : 0; });
  const faixa = ["menos de 5 s", "5 a 15 s", "15 a 30 s", "30 s a 1 min", "mais de 1 min"].map((nome, i) => { const l = tempos.find((x) => x.f === i); return { faixa: nome, n: l ? Number(l.n) : 0 }; });
  return {
    visitas, clicaram,
    telas: LP_TELAS.map((t, i) => ({ tela: t, nome: LP_TELA_NOME[i], chegaram: chegou[i], sairamAqui: saiu[i] })),
    botoes: botoes.map((l) => ({ botao: l.clique, nome: LP_BOTAO_NOME[l.clique] || l.clique, n: Number(l.n) })),
    anuncios: anuncios.map((l) => ({ anuncio: l.anuncio || "(sem anúncio)", visitas: Number(l.v), chegaramNaOferta: Number(l.o || 0), clicaram: Number(l.k || 0) })),
    aparelhos: aparelhos.map((l) => ({ aparelho: l.mob ? "celular" : "computador", visitas: Number(l.v), clicaram: Number(l.k || 0) })),
    tempoDeQuemSaiu: faixa,
    porDia: Object.fromEntries(dias.map((l) => [l.dia, { visitas: Number(l.v), clicaram: Number(l.k || 0) }])),
  };
}

// Detalhe dos pedidos do período, sem dado pessoal: método, hora, valor, status no Mercado Pago e motivo de recusa.
async function funilPedidos(env, lista) {
  const ks = [];
  let cursor;
  do {
    const r = await env.PEDIDOS.list({ prefix: "pedido:", cursor });
    for (const k of r.keys) if (k.metadata && lista.includes(k.metadata.d)) ks.push(k);
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  const out = await Promise.all(ks.slice(0, 40).map(async (k) => {
    const id = k.name.slice(7), reg = (await env.PEDIDOS.get(k.name, "json")) || {};
    let mpd = {};
    try { const r = await mp(env, "GET", "/v1/orders/" + encodeURIComponent(id)); mpd = r.data || {}; } catch (e) {}
    const pg = ((mpd.transactions || {}).payments || [])[0] || {};
    return {
      id: id.slice(0, 6) + "…", dia: k.metadata.d, criado: reg.criado || "", metodo: reg.metodo || k.metadata.m || "", fase: reg.fase || 0, extras: (reg.itens || []).join(","), total: reg.total || k.metadata.t || 0,
      emailEnviado: !!reg.emailEnviado, dominioEmail: String(reg.email || "").split("@")[1] || "",
      doAnuncio: !!reg.oppref, aparelho: /iPhone|iPad/.test(reg.ua || "") ? "iOS" : /Android/.test(reg.ua || "") ? "Android" : reg.ua ? "computador" : "", navegador: /Instagram|FBAN|FBAV/.test(reg.ua || "") ? "app" : /CriOS|Chrome/.test(reg.ua || "") ? "Chrome" : /Safari/.test(reg.ua || "") ? "Safari" : "", mp_status: mpd.status || "", mp_detalhe: mpd.status_detail || "",
      pagamento_status: pg.status || "", pagamento_detalhe: pg.status_detail || "", meio: (pg.payment_method || {}).id || "", tipo: (pg.payment_method || {}).type || "",
      atualizado: mpd.last_updated_date || "",
    };
  }));
  return out.sort((a, b) => String(a.criado).localeCompare(String(b.criado)));
}

// Sessões que tocaram em pagar e não geraram pedido (ex.: cartão recusado antes de virar pedido).
async function funilCliques(env, lista) {
  if (!env.FUNIL) return null;
  try { const db = await funilBanco(env); const r = await db.prepare("SELECT dia, fase, itens, viu, clicou, seg FROM sessao WHERE dia >= ?1 AND clicou = 1").bind(lista[lista.length - 1]).all(); return r.results || []; } catch (e) { return null; }
}

async function funilRelatorio(env, url) {
  if (!env.PEDIDOS || (await sha256(url.searchParams.get("k") || "")) !== FUNIL_HASH) return new Response("Não encontrado.", { status: 404 });
  const dias = Math.max(1, Math.min(14, Number(url.searchParams.get("dias")) || 7));
  const zero = () => ({ abriu: 0, dados: 0, fase: 0, viu: 0, pedido: 0, pago: 0, extra: 0, combo: 0, receita: 0, f1: 0, f2: 0, f3: 0 });
  const lista = [], porDia = {};
  for (let i = 0; i < dias; i++) { const d = diaBR(Date.now() - i * 864e5); lista.push(d); porDia[d] = zero(); }
  let fonte = "kv";                    // quem saiu sem gerar pedido
  if (env.FUNIL) {
    fonte = "d1";
    try {
      const db = await funilBanco(env);
      const r = await db.prepare("SELECT dia, COUNT(*) AS abriu, SUM(dados) AS dados, SUM(fase > 0) AS fase, SUM(viu) AS viu, SUM(fase = 1) AS f1, SUM(fase = 2) AS f2, SUM(fase = 3) AS f3 FROM sessao WHERE dia >= ?1 GROUP BY dia").bind(lista[lista.length - 1]).all();
      for (const l of r.results || []) { const n = porDia[l.dia]; if (n) for (const c of ["abriu", "dados", "fase", "viu", "f1", "f2", "f3"]) n[c] += Number(l[c]) || 0; }
      await db.prepare("DELETE FROM sessao WHERE dia < ?1").bind(diaBR(Date.now() - 60 * 864e5)).run();   // guarda 60 dias
    } catch (e) { fonte = "d1 com erro"; console.log("funil: leitura falhou", String((e && e.message) || e)); }
  } else {
    for (const d of lista) {
      let cursor;
      do {
        const r = await env.PEDIDOS.list({ prefix: "sessao:" + d + ":", cursor });
        for (const k of r.keys) { const m = k.metadata || {}, n = porDia[d]; n.abriu++; if (m.d) n.dados++; if (m.f) { n.fase++; n["f" + m.f]++; } if (m.v) n.viu++; }
        cursor = r.list_complete ? null : r.cursor;
      } while (cursor);
    }
  }
  let cursor;                          // quem gerou Pix ou passou o cartão
  do {
    const r = await env.PEDIDOS.list({ prefix: "pedido:", cursor });
    for (const k of r.keys) {
      const m = k.metadata, n = m && porDia[m.d];
      if (!n) continue;
      n.abriu++; n.dados++; n.viu++; n.pedido++;
      if (m.f) { n.fase++; n["f" + m.f]++; }
      if (m.p) { n.pago++; n.receita += m.t || 0; if (m.x) n.extra++; if (m.x && m.x.length === 3) n.combo++; }
    }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  const tot = zero();
  for (const d of lista) for (const c in tot) tot[c] += porDia[d][c];
  let lp = null;
  if (env.FUNIL) { try { lp = await lpResumo(env, lista[lista.length - 1]); await (await funilBanco(env)).prepare("DELETE FROM " + LP_TABELA + " WHERE dia < ?1").bind(diaBR(Date.now() - 60 * 864e5)).run(); } catch (e) { console.log("lp: leitura falhou", String((e && e.message) || e)); } }
  if (url.searchParams.get("pedidos") === "1") return json({ dias, pedidos: await funilPedidos(env, lista), cliquesSemPedido: await funilCliques(env, lista) });
  let rec = null;
  try { rec = await recResumo(env); } catch (e) { console.log("rec: resumo falhou", String((e && e.message) || e)); }
  if (url.searchParams.get("formato") === "json") return json({ dias, fonte, total: tot, porDia, lp, recuperacao: rec });
  const pct = (a, b) => (b ? Math.round((a / b) * 100) + "%" : "0%");
  const grana = (c) => "R$ " + (c / 100).toFixed(2).replace(".", ",");
  const passos = [["Abriram o checkout", "abriu"], ["Preencheram os dados", "dados"], ["Escolheram a fase", "fase"], ["Chegaram no botão de pagar", "viu"], ["Geraram Pix ou passaram o cartão", "pedido"], ["Pagaram", "pago"]];
  const semVer = tot.fase - Math.min(tot.viu, tot.fase);
  let h = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Funil do checkout</title><style>body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:#F4F5F7;color:#16181B;margin:0;padding:20px;line-height:1.45}main{max-width:720px;margin:0 auto}h1{font-size:1.35rem;margin:0 0 4px}h2{font-size:1rem;margin:26px 0 8px}p{margin:0 0 10px;color:#5B6470;font-size:.92rem}.c{background:#fff;border-radius:14px;padding:14px 16px;margin-bottom:12px}.l{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px solid #EEF0F3}.l:last-child{border-bottom:0}.l b{font-variant-numeric:tabular-nums;white-space:nowrap}.l small{color:#8A929C;font-weight:400;margin-left:6px}.a{background:#FFF1EA;border:1.5px solid #FF5A1F;border-radius:14px;padding:14px 16px;margin-bottom:12px}.a b{font-size:1.2rem}table{width:100%;border-collapse:collapse;font-size:.84rem;background:#fff;border-radius:14px;overflow:hidden}th,td{padding:8px 6px;text-align:right;border-bottom:1px solid #EEF0F3;font-variant-numeric:tabular-nums;white-space:nowrap}th:first-child,td:first-child{text-align:left;padding-left:12px}th{font-size:.7rem;color:#5B6470;font-weight:600}.r{overflow-x:auto}</style></head><body><main>';
  h += "<h1>Funil da LP e do checkout</h1><p>40 Prompts de Medicina · últimos " + dias + " dias (horário de Brasília)</p>";
  if (lp && lp.visitas) {
    const piorTela = lp.telas.reduce((a, t) => (t.sairamAqui > a.sairamAqui ? t : a), lp.telas[0]);
    h += '<h2>LP (versão nova, desde 23/11)</h2><div class="a"><b>' + lp.clicaram + " de " + lp.visitas + " (" + pct(lp.clicaram, lp.visitas) + ")</b> tocaram num botão de compra. Onde mais gente sai sem tocar: <b>" + piorTela.nome + "</b> (" + piorTela.sairamAqui + (piorTela.sairamAqui === 1 ? " pessoa" : " pessoas") + ").</div>";
    h += '<div class="c">';
    lp.telas.forEach((t, i) => { h += '<div class="l"><span>' + (i + 1) + ". " + t.nome + "</span><b>" + t.chegaram + "<small>" + pct(t.chegaram, lp.visitas) + " chegaram · " + t.sairamAqui + " saíram aqui</small></b></div>"; });
    h += "</div>";
    h += '<h2>Botão que levou ao checkout</h2><div class="c">';
    if (!lp.botoes.length) h += '<div class="l"><span>Ninguém tocou ainda</span><b>0</b></div>';
    lp.botoes.forEach((x) => { h += '<div class="l"><span>' + x.nome + "</span><b>" + x.n + "<small>" + pct(x.n, lp.clicaram) + "</small></b></div>"; });
    h += "</div>";
    h += '<h2>Por anúncio</h2><div class="r"><table><tr><th>Anúncio</th><th>Visitas</th><th>Oferta</th><th>Comprar</th></tr>';
    lp.anuncios.forEach((x) => { h += "<tr><td>" + escHtml(x.anuncio) + "</td><td>" + x.visitas + "</td><td>" + x.chegaramNaOferta + " (" + pct(x.chegaramNaOferta, x.visitas) + ")</td><td>" + x.clicaram + " (" + pct(x.clicaram, x.visitas) + ")</td></tr>"; });
    h += "</table></div><p>Oferta: chegaram na tela da oferta. Comprar: tocaram num botão de compra.</p>";
    h += '<h2>Aparelho e tempo</h2><div class="c">';
    lp.aparelhos.forEach((x) => { h += '<div class="l"><span>' + x.aparelho + "</span><b>" + x.visitas + "<small>" + pct(x.clicaram, x.visitas) + " tocaram em comprar</small></b></div>"; });
    lp.tempoDeQuemSaiu.forEach((x) => { h += '<div class="l"><span>Saiu sem tocar, ficou ' + x.faixa + "</span><b>" + x.n + "</b></div>"; });
    h += "</div><h2>Checkout</h2>";
  } else if (lp) h += '<h2>LP (versão nova, desde 23/11)</h2><p>Ainda sem visita registrada na LP nova.</p><h2>Checkout</h2>';
  h += '<div class="a"><b>' + semVer + " de " + tot.fase + " (" + pct(semVer, tot.fase) + ")</b><br>escolheram a fase e saíram sem chegar no botão de pagar. É esse número que diz se a rolagem depois dos extras está derrubando gente.</div>";
  h += '<div class="c">';
  for (const [nome, c] of passos) h += '<div class="l"><span>' + nome + "</span><b>" + tot[c] + "<small>" + pct(tot[c], tot.abriu) + "</small></b></div>";
  h += '</div><div class="c">';
  h += '<div class="l"><span>Pagos com algum extra</span><b>' + tot.extra + "<small>" + pct(tot.extra, tot.pago) + "</small></b></div>";
  h += '<div class="l"><span>Pagos com o combo</span><b>' + tot.combo + "<small>" + pct(tot.combo, tot.pago) + "</small></b></div>";
  h += '<div class="l"><span>Receita</span><b>' + grana(tot.receita) + "</b></div>";
  h += '<div class="l"><span>Ticket médio</span><b>' + grana(tot.pago ? Math.round(tot.receita / tot.pago) : 0) + "</b></div>";
  h += '<div class="l"><span>Fase escolhida</span><b>básico ' + tot.f1 + " · clínico " + tot.f2 + " · internato " + tot.f3 + "</b></div></div>";
  if (rec && rec.n) {
    h += '<h2>E-mails de recuperação (desde o início)</h2><div class="c">';
    h += '<div class="l"><span>E-mails na lista (geraram pedido)</span><b>' + rec.n + "</b></div>";
    h += '<div class="l"><span>1. Pix aberto ou cartão recusado (5 min)</span><b>' + rec.e1 + "</b></div>";
    h += '<div class="l"><span>2. Tudo por R$ 29,90 (24 h)</span><b>' + rec.e2 + "</b></div>";
    h += '<div class="l"><span>3. Só o guia por R$ 14,90 (7 dias)</span><b>' + rec.e3 + "</b></div>";
    h += '<div class="l"><span>Compraram depois de um e-mail</span><b>' + rec.recuperados + "</b></div>";
    h += '<div class="l"><span>Saíram da lista</span><b>' + rec.sairam + (rec.falhas ? "<small>" + rec.falhas + " envios falharam</small>" : "") + "</b></div></div>";
  }
  h += '<h2>Por dia</h2><div class="r"><table><tr><th>Dia</th><th>Abriu</th><th>Fase</th><th>Botão</th><th>Pedido</th><th>Pago</th><th>Extra</th><th>Receita</th></tr>';
  for (const d of lista) { const n = porDia[d]; h += "<tr><td>" + d.slice(8) + "/" + d.slice(5, 7) + "</td><td>" + n.abriu + "</td><td>" + n.fase + "</td><td>" + n.viu + "</td><td>" + n.pedido + "</td><td>" + n.pago + "</td><td>" + n.extra + "</td><td>" + grana(n.receita) + "</td></tr>"; }
  h += "</table></div>";
  h += '<p style="margin-top:14px">Como ler: "Abriram" conta quem gerou pedido mais quem saiu e o navegador conseguiu avisar. Alguns celulares fecham a página sem avisar, então o número real de visitas é um pouco maior. Pedidos e pagamentos são exatos. Troque o período com &amp;dias=14 no fim do endereço.</p></main></body></html>';
  return new Response(h, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store", "x-robots-tag": "noindex" } });
}

// Confere um extra por vez (abre e vê se é PDF). Ex.: /api/saude/extras?n=f1-osce
async function saudeExtra(env, url) {
  const n = url.searchParams.get("n") || "";
  if (!/^(f[123]-(osce|enamed|kit)|academico)$/.test(n)) return json({ erro: "nome inválido" }, 400);
  try { const b = new Uint8Array(await abrirArquivo(env, url, { bin: n })); return json({ extra: n, ok: b[0] === 0x25 && b[1] === 0x50, bytes: b.length }); }
  catch (e) { return json({ extra: n, ok: false }); }
}

// ---------- e-mails de recuperação (quem gerou pedido e não pagou) ----------
// Sequência por e-mail, guardada no D1 (tabela recupera). O cron da Cloudflare roda a cada minuto:
//   E1: 5 min depois do pedido sem pagamento. Pix: manda o código de novo. Cartão recusado: chama pro Pix.
//   E2: 24 h depois da 1ª tentativa: os 40 prompts + o pacote inteiro da fase + bônus por R$ 29,90 (72 h).
//   E3: 7 dias depois: só os 40 prompts por R$ 14,90 (72 h).
// Para na hora que o e-mail compra (posVenda marca "pago") ou quando a pessoa sai da lista.
// O preço da oferta vai num link assinado: o servidor confere a assinatura e cobra o preço fechado.
const REC_LIMITE_DIA = 40;   // o Resend grátis dá 100 por dia, divididos com a Cozinha Guiada
const OFERTAS = { tudo: { preco: 2990, de: PRODUTO.centavos + COMBO_CENTAVOS }, "14": { preco: 1490, de: PRODUTO.centavos } };
const CHECKOUT_URL = OA_ORIGEM + "/40prompts-estudante-medicina/checkout/";

async function hmacHex(env, rotulo, txt, n = 16) {
  const k = await crypto.subtle.importKey("raw", new TextEncoder().encode(rotulo + ":" + env.MP_ACCESS_TOKEN), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const s = new Uint8Array(await crypto.subtle.sign("HMAC", k, new TextEncoder().encode(txt)));
  return [...s.slice(0, n)].map((x) => x.toString(16).padStart(2, "0")).join("");
}
function b64url(t) { return btoa(t).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
function deB64url(t) { t = String(t).replace(/-/g, "+").replace(/_/g, "/"); return atob(t + "===".slice((t.length + 3) % 4)); }

async function criarOferta(env, tipo, fase, horas = 72) {
  const corpo = b64url(JSON.stringify({ t: tipo, f: fase || 0, e: Date.now() + horas * 3600e3 }));
  return corpo + "." + (await hmacHex(env, "of", corpo, 12));
}

async function lerOferta(env, token) {
  const [corpo, sig] = String(token || "").split(".");
  if (!corpo || !sig || corpo.length > 120 || sig !== (await hmacHex(env, "of", corpo, 12))) return null;
  let d; try { d = JSON.parse(deB64url(corpo)); } catch (e) { return null; }
  const o = OFERTAS[d.t];
  if (!o || !(d.e > Date.now())) return null;
  return { tipo: d.t, fase: [1, 2, 3].includes(d.f) ? d.f : 0, preco: o.preco, de: o.de, expira: d.e };
}

// Seleção que vai ser cobrada: a do navegador, ou a da oferta quando o link do e-mail vem junto.
async function selecaoFinal(env, b) {
  if (!b || !b.oferta) return lerSelecao(b);
  const o = await lerOferta(env, b.oferta);
  if (!o) throw new ErroCliente("Essa oferta expirou. Atualize a página para ver o preço normal.");
  if (o.tipo === "tudo") {
    const fase = o.fase || lerSelecao(b).fase;
    if (!fase) throw new ErroCliente("Escolha a sua fase para continuar.");
    return { fase, itens: ORDEM_EXTRAS.slice(), preco: o.preco };
  }
  return { fase: 0, itens: [], preco: o.preco };
}

async function ofertaVer(env, url) {
  const o = await lerOferta(env, url.searchParams.get("o"));
  if (!o) return json({ ok: false });
  return json({ ok: true, tipo: o.tipo, fase: o.fase, total: o.preco, de: o.de, expira: o.expira });
}

async function recRegistrar(env, d) {
  if (!env.FUNIL || !d.email || !d.pedido || /@orbytstudio\.com\.br$/.test(d.email)) return;
  try {
    const db = await funilBanco(env), agora = Date.now();
    const chave = [...crypto.getRandomValues(new Uint8Array(12))].map((x) => x.toString(16).padStart(2, "0")).join("");
    await db.prepare(
      "INSERT INTO recupera (email, nome, fase, itens, pedido, metodo, total, qr, ticket, criado, ultimo, chave, origem) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?10, ?11, ?12) " +
      "ON CONFLICT(email) DO UPDATE SET nome = excluded.nome, fase = CASE WHEN excluded.fase > 0 THEN excluded.fase ELSE recupera.fase END, itens = excluded.itens, pedido = excluded.pedido, metodo = excluded.metodo, total = excluded.total, qr = excluded.qr, ticket = excluded.ticket, ultimo = excluded.ultimo, origem = excluded.origem, " +
      "e1 = CASE WHEN recupera.e1 > 0 AND excluded.ultimo - recupera.e1 < 21600000 THEN recupera.e1 ELSE 0 END"
    ).bind(d.email, String(d.nome || "").slice(0, 60), d.sel.fase || 0, (d.sel.itens || []).join(","), d.pedido, d.metodo, totalCentavos(d.sel), String(d.qr || "").slice(0, 600), String(d.ticket || "").slice(0, 300), agora, chave, d.sel.preco ? "of" + d.sel.preco : "").run();
  } catch (e) { console.log("rec: registro falhou", String((e && e.message) || e)); }
}

async function recPago(env, o) {
  if (!env.FUNIL) return;
  const comp = env.PEDIDOS ? await env.PEDIDOS.get("pedido:" + o.id, "json") : null;
  const email = String((comp && comp.email) || (o.payer && o.payer.email) || "").toLowerCase();
  const db = await funilBanco(env);
  await db.prepare("UPDATE recupera SET pago = ?1 WHERE pago = 0 AND (email = ?2 OR pedido = ?3)").bind(Date.now(), email, o.id).run();
}

async function recSair(req, env, url) {
  const c = url.searchParams.get("c") || "";
  if (/^[a-f0-9]{24}$/.test(c) && env.FUNIL) { try { await (await funilBanco(env)).prepare("UPDATE recupera SET sair = ?1 WHERE chave = ?2 AND sair = 0").bind(Date.now(), c).run(); } catch (e) {} }
  if (req.method === "POST") return new Response("ok");
  return new Response('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Pronto</title></head><body style="font-family:Arial,Helvetica,sans-serif;background:#F4F5F7;color:#16181B;display:grid;place-items:center;min-height:90vh;margin:0;padding:20px"><div style="background:#fff;border-radius:16px;padding:28px;max-width:420px;text-align:center"><h1 style="font-size:1.3rem;margin:0 0 8px">Pronto, você saiu da lista.</h1><p style="color:#5B6470;margin:0">Não vamos mandar mais e-mails sobre esse pedido.</p></div></body></html>', { headers: { "content-type": "text/html; charset=utf-8" } });
}

// ---- horário de Brasília ----
function brt(ms) { return new Date(ms - 3 * 3600e3); }
function horaBR(ms) { const d = brt(ms); return d.getUTCHours() + "h" + String(d.getUTCMinutes()).padStart(2, "0"); }
function quandoBR(ms) {
  const d = brt(ms), hoje = brt(Date.now());
  const dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];
  const mesmoDia = d.toISOString().slice(0, 10) === hoje.toISOString().slice(0, 10);
  return (mesmoDia ? "hoje" : dias[d.getUTCDay()] + ", " + String(d.getUTCDate()).padStart(2, "0") + "/" + String(d.getUTCMonth() + 1).padStart(2, "0")) + ", às " + horaBR(ms);
}
function inicioDiaBR(ms) { return Date.parse(diaBR(ms) + "T03:00:00Z"); }

// ---- texto dos e-mails ----
function recLink(base, extra) { return CHECKOUT_URL + "?" + base + (extra ? "&" + extra : ""); }

async function recEmail(env, c, tipo, agora) {
  const nome = String(c.nome || "").trim();
  const oi = nome ? "Oi, " + escapar(nome) + "!" : "Oi!";
  const f = FASES[c.fase];
  const grana = (x) => "R$ " + (x / 100).toFixed(2).replace(".", ",");
  const botao = (href, txt, cor) => '<a href="' + href + '" style="display:inline-block;background:' + (cor || "#0E6B63") + ';color:#ffffff;padding:15px 26px;border-radius:999px;text-decoration:none;font-weight:bold;font-size:16px">' + txt + "</a>";
  const p = (t, est) => '<p style="margin:0 0 16px;' + (est || "") + '">' + t + "</p>";
  const sair = OA_ORIGEM + "/api/sair?c=" + c.chave;
  let assunto, corpo = "", texto = "";
  if (tipo === "1pix") {
    const vale = Number(c.ultimo) + 30 * 60e3;
    assunto = "Seu Pix de " + grana(c.total) + " ainda está aberto";
    corpo += p(oi + " Seu pedido dos <b>" + PRODUTO.nome + "</b> está reservado. Falta só o Pix.");
    if (c.qr) corpo += p("<b>Pix copia e cola</b> (toque e segure para copiar):", "margin-bottom:8px") + '<div style="background:#F1F5F4;border:1.5px dashed #9FC9C1;border-radius:12px;padding:14px;font-family:Menlo,Consolas,monospace;font-size:12px;line-height:1.5;word-break:break-all;color:#16181B;margin:0 0 16px">' + escapar(c.qr) + "</div>";
    corpo += p("Cole no app do seu banco, em Pix copia e cola. O código vale até as <b>" + horaBR(vale) + "</b>.");
    if (c.ticket && /^https:\/\//.test(c.ticket)) corpo += p(botao(escapar(c.ticket), "Abrir o QR Code do Pix"), "margin:0 0 22px");
    corpo += p("Pagou, o PDF chega neste e-mail na hora.");
    corpo += p('O Pix venceu? <a href="' + recLink("fase=" + c.fase + "&itens=" + itensLetras(c.itens), "origem=email-e1") + '" style="color:#0E6B63;font-weight:bold">Gere outro aqui</a>, leva 1 minuto.', "color:#5B6470;font-size:14px");
    texto = "Seu Pix de " + grana(c.total) + " ainda está aberto. Pix copia e cola: " + (c.qr || "") + " Vale até " + horaBR(vale) + ". Gerar outro: " + recLink("fase=" + c.fase, "origem=email-e1");
  } else if (tipo === "1cartao") {
    const link = recLink("fase=" + c.fase + "&itens=" + itensLetras(c.itens), "origem=email-e1");
    assunto = "Seu cartão não passou. No Pix resolve em 1 minuto";
    corpo += p(oi + " O pagamento no cartão não foi aprovado. Isso é comum em compra online e quase sempre é trava do banco, não do cartão.");
    corpo += p("No <b>Pix</b> aprova na hora e o PDF chega no seu e-mail em segundos. Sua fase e seus extras já ficam marcados:");
    corpo += p(botao(link, "Pagar " + grana(c.total) + " com Pix"), "margin:0 0 22px");
    texto = "Seu cartão não passou. No Pix aprova na hora: " + link;
  } else if (tipo === "2") {
    const of = OFERTAS.tudo, token = await criarOferta(env, "tudo", c.fase), link = recLink("oferta=" + token, "origem=email-e2");
    const fim = agora + 72 * 3600e3;
    assunto = f ? "Tudo do " + f.rotulo + " por " + grana(of.preco) : "Os 40 Prompts + o pacote da sua fase por " + grana(of.preco);
    const itens = [PRODUTO.nome].concat(f ? ORDEM_EXTRAS.map((k) => EXTRAS[k].titulo(f)) : ["OSCE, simulados ENAMED e kit de prompts da sua fase"]).concat([BONUS.titulo]);
    corpo += p(oi + " Ontem você chegou até o pagamento e parou. Então montei uma condição só para você:");
    corpo += '<div style="background:#F1F5F4;border-radius:14px;padding:18px 18px 8px;margin:0 0 18px"><p style="margin:0 0 10px;font-size:15px"><b>Leva tudo por ' + grana(of.preco) + '</b> <s style="color:#8A929C">' + grana(of.de) + "</s></p>";
    for (const t of itens) corpo += '<p style="margin:0 0 10px;font-size:15px"><span style="color:#0E6B63;font-weight:bold">&#10003;</span> ' + escapar(t) + "</p>";
    corpo += "</div>";
    corpo += p("É o preço só dos 40 prompts, com o pacote inteiro" + (f ? " do " + f.rotulo : " da sua fase") + " junto.");
    corpo += p(botao(link, "Quero tudo por " + grana(of.preco)), "margin:0 0 22px");
    corpo += p("Vale até " + quandoBR(fim) + ". Depois volta ao preço normal.", "color:#5B6470;font-size:14px");
    texto = "Tudo por " + grana(of.preco) + " (de " + grana(of.de) + "): " + itens.join(", ") + ". Vale até " + quandoBR(fim) + ": " + link;
  } else {
    const of = OFERTAS["14"], token = await criarOferta(env, "14", c.fase), link = recLink("oferta=" + token, "origem=email-e3");
    const fim = agora + 72 * 3600e3;
    assunto = "Último aviso: os 40 Prompts por " + grana(of.preco);
    corpo += p(oi + " Este é o último e-mail sobre o seu pedido.");
    corpo += p("Liberei os <b>" + PRODUTO.nome + "</b> pela metade do preço: <b>" + grana(of.preco) + "</b> <s style=\"color:#8A929C\">" + grana(of.de) + "</s>.");
    corpo += p("São 40 prompts prontos para colar na sua IA e transformar ela em tutora: resumo, revisão, questões, caso clínico e plano de estudo.");
    corpo += p(botao(link, "Quero por " + grana(of.preco)), "margin:0 0 22px");
    corpo += p("Vale até " + quandoBR(fim) + ".", "color:#5B6470;font-size:14px");
    texto = "Os 40 Prompts por " + grana(of.preco) + ", vale até " + quandoBR(fim) + ": " + link;
  }
  const html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.55;color:#16181B;max-width:520px;margin:0 auto;padding:24px">' + corpo +
    '<p style="margin:28px 0 0;color:#8A929C;font-size:12px;line-height:1.5">Orbyt Studio para Medicina · orbytstudio.com.br<br>Não quer mais estes e-mails? <a href="' + sair + '" style="color:#8A929C">Sair da lista</a>.</p></div>';
  return { assunto, html, texto: texto + "\n\nSair da lista: " + sair, sair };
}

function itensLetras(itens) { return String(itens || "").split(",").map((k) => (EXTRAS[k] ? EXTRAS[k].letra : "")).join(""); }

async function recEnviar(env, c, tipo, agora) {
  const m = await recEmail(env, c, tipo, agora);
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { authorization: "Bearer " + env.RESEND_API_KEY, "content-type": "application/json", "idempotency-key": "rec-" + tipo.charAt(0) + "-" + (tipo.charAt(0) === "1" ? c.pedido : await sha256(c.email)) },
    body: JSON.stringify({
      from: env.EMAIL_DE || "Orbyt Studio para Medicina <medicina@orbytstudio.com.br>",
      reply_to: "medicina@orbytstudio.com.br",
      to: [c.email], subject: m.assunto, html: m.html, text: m.texto,
      headers: { "List-Unsubscribe": "<" + m.sair + ">", "List-Unsubscribe-Post": "List-Unsubscribe=One-Click" },
    }),
  });
  if (!r.ok) console.log("rec: email falhou", tipo, r.status, (await r.text()).slice(0, 300));
  else console.log("rec: email enviado", tipo, c.pedido);
  return r.ok;
}

// Reserva a linha antes de mandar: se dois crons se cruzarem, só um envia.
async function recPegar(db, c, campo, agora) {
  const r = await db.prepare("UPDATE recupera SET " + campo + " = ?1 WHERE email = ?2 AND " + campo + " = 0").bind(agora, c.email).run();
  return ((r.meta && r.meta.changes) || 0) === 1;
}

async function recuperar(env) {
  if (!env.FUNIL || !env.RESEND_API_KEY) return { ok: false };
  const db = await funilBanco(env), agora = Date.now(), base = new URL(OA_ORIGEM), feitos = [];
  const d0 = inicioDiaBR(agora);
  const cont = await db.prepare("SELECT (SELECT COUNT(*) FROM recupera WHERE e1 >= ?1) + (SELECT COUNT(*) FROM recupera WHERE e2 >= ?1) + (SELECT COUNT(*) FROM recupera WHERE e3 >= ?1) AS n").bind(d0).first();
  let folga = REC_LIMITE_DIA - (Number(cont && cont.n) || 0);
  // passou da janela do 1º e-mail (o Pix já venceu): não manda mais esse
  await db.prepare("UPDATE recupera SET e1 = -1 WHERE e1 = 0 AND ultimo < ?1").bind(agora - 25 * 60e3).run();
  const etapas = [
    ["e1", "SELECT * FROM recupera WHERE e1 = 0 AND pago = 0 AND sair = 0 AND ultimo <= ?1 LIMIT 5", [agora - 5 * 60e3]],
    ["e2", "SELECT * FROM recupera WHERE e2 = 0 AND pago = 0 AND sair = 0 AND criado <= ?1 AND criado > ?2 AND ultimo <= ?3 LIMIT 5", [agora - 24 * 3600e3, agora - 6 * 864e5, agora - 12 * 3600e3]],
    ["e3", "SELECT * FROM recupera WHERE e3 = 0 AND pago = 0 AND sair = 0 AND criado <= ?1 AND criado > ?2 AND ultimo <= ?3 LIMIT 5", [agora - 7 * 864e5, agora - 10 * 864e5, agora - 24 * 3600e3]],
  ];
  for (const [campo, sql, args] of etapas) {
    const r = await db.prepare(sql).bind(...args).all();
    for (const c of r.results || []) {
      if (folga <= 0) return { ok: true, feitos, limite: true };
      if (!(await recPegar(db, c, campo, agora))) continue;
      let tipo = campo.slice(1);
      if (campo === "e1") {
        // confere no Mercado Pago antes: pagou e o aviso não chegou? entrega agora em vez de cobrar de novo
        const o = await mp(env, "GET", "/v1/orders/" + c.pedido);
        const st = o.ok ? o.data.status : "";
        if (st === "processed") { await posVenda(env, base, o.data); await db.prepare("UPDATE recupera SET e1 = -1 WHERE email = ?1").bind(c.email).run(); feitos.push({ tipo: "ja-pago" }); continue; }
        if (c.metodo === "pix" && c.qr && st !== "expired" && st !== "canceled" && st !== "failed") tipo = "1pix";
        else if (c.metodo === "cartao" && (st === "failed" || st === "canceled" || st === "expired")) tipo = "1cartao";
        else { await db.prepare("UPDATE recupera SET e1 = -1 WHERE email = ?1").bind(c.email).run(); continue; }
      }
      let ok = false;
      try { ok = await recEnviar(env, c, tipo, agora); } catch (e) { console.log("rec: envio erro", String((e && e.message) || e)); }
      if (!ok) await db.prepare("UPDATE recupera SET " + campo + " = -2 WHERE email = ?1").bind(c.email).run();
      folga--;
      feitos.push({ tipo, ok });
    }
  }
  return { ok: true, feitos };
}

async function recResumo(env) {
  if (!env.FUNIL) return null;
  const db = await funilBanco(env);
  const r = await db.prepare("SELECT COUNT(*) AS n, SUM(pago = 0 AND sair = 0) AS fila, SUM(e1 > 0) AS e1, SUM(e2 > 0) AS e2, SUM(e3 > 0) AS e3, SUM(pago > 0 AND ((e1 > 0 AND pago > e1) OR (e2 > 0 AND pago > e2) OR (e3 > 0 AND pago > e3))) AS recuperados, SUM(sair > 0) AS sairam, SUM(e1 = -2 OR e2 = -2 OR e3 = -2) AS falhas FROM recupera").first();
  const o = {};
  for (const k of ["n", "fila", "e1", "e2", "e3", "recuperados", "sairam", "falhas"]) o[k] = Number(r && r[k]) || 0;
  return o;
}

// Painel interno, com a mesma senha do relatório: /api/recupera?k=...&acao=status|ver|backfill|rodar
async function recAdmin(env, url, ctx) {
  if ((await sha256(url.searchParams.get("k") || "")) !== FUNIL_HASH) return new Response("Não encontrado.", { status: 404 });
  const acao = url.searchParams.get("acao") || "status";
  if (acao === "ver") {
    const tipo = url.searchParams.get("tipo") || "2", fase = Number(url.searchParams.get("fase")) || 2;
    const c = { email: "exemplo@email.com", nome: url.searchParams.get("nome") || "Ana", fase, itens: "osce,enamed,kit", pedido: "ORDEXEMPLO0000000000", metodo: tipo === "1cartao" ? "cartao" : "pix", total: 4280, qr: "00020126580014br.gov.bcb.pix0136exemplo-de-codigo-pix-copia-e-cola-0000000000005204000053039865406" + "42.805802BR5925ORBYT STUDIO6009SAO PAULO62070503***6304ABCD", ticket: "https://www.mercadopago.com.br/", ultimo: Date.now(), chave: "0".repeat(24) };
    const m = await recEmail(env, c, tipo, Date.now());
    return new Response('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + escapar(m.assunto) + '</title><body style="margin:0;background:#E9ECEF"><div style="max-width:560px;margin:0 auto;background:#fff;font-family:Arial;padding:12px 24px;font-size:13px;color:#5B6470;border-bottom:1px solid #EEF0F3">Assunto: <b style="color:#16181B">' + escapar(m.assunto) + "</b></div>" + '<div style="max-width:560px;margin:0 auto;background:#fff">' + m.html + "</div></body>", { headers: { "content-type": "text/html; charset=utf-8" } });
  }
  if (acao === "rodar") return json(await recuperar(env));
  if (acao === "backfill") return json(await recBackfill(env, Math.max(1, Math.min(10, Number(url.searchParams.get("dias")) || 7))));
  return json(await recResumo(env));
}

// Uma vez só: põe na fila quem gerou pedido nos últimos dias e não pagou (sem o e-mail 1, porque o Pix já venceu).
async function recBackfill(env, dias) {
  if (!env.FUNIL || !env.PEDIDOS) return { ok: false };
  const db = await funilBanco(env), desde = diaBR(Date.now() - dias * 864e5), porEmail = {};
  let cursor;
  do {
    const r = await env.PEDIDOS.list({ prefix: "pedido:", cursor });
    for (const k of r.keys) {
      const m = k.metadata || {};
      if (!m.d || m.d < desde) continue;
      const id = k.name.slice(7), comp = await env.PEDIDOS.get(k.name, "json");
      if (!comp || !comp.email) continue;
      const email = String(comp.email).toLowerCase();
      if (/@orbytstudio\.com\.br$/.test(email)) continue;
      let pago = !!m.p;
      if (!pago) { const o = await mp(env, "GET", "/v1/orders/" + id); pago = o.ok && o.data.status === "processed"; }
      const t = Date.parse(comp.criado) || Date.now();
      const e = porEmail[email] || (porEmail[email] = { email, nome: comp.first_name || "", fase: 0, itens: "", pedido: id, metodo: comp.metodo || "", total: comp.total || PRODUTO.centavos, criado: t, ultimo: 0, pago: false });
      e.pago = e.pago || pago;
      if (comp.fase) e.fase = comp.fase;
      e.criado = Math.min(e.criado, t);
      if (t >= e.ultimo) { e.ultimo = t; e.pedido = id; e.metodo = comp.metodo || ""; e.total = comp.total || PRODUTO.centavos; e.itens = (comp.itens || []).join(","); e.nome = comp.first_name || e.nome; }
    }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  let novos = 0, pagos = 0;
  for (const e of Object.values(porEmail)) {
    if (e.pago) pagos++;
    const chave = [...crypto.getRandomValues(new Uint8Array(12))].map((x) => x.toString(16).padStart(2, "0")).join("");
    const r = await db.prepare("INSERT OR IGNORE INTO recupera (email, nome, fase, itens, pedido, metodo, total, criado, ultimo, e1, pago, chave, origem) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, -1, ?10, ?11, 'backfill')")
      .bind(e.email, String(e.nome).slice(0, 60), e.fase, e.itens, e.pedido, e.metodo, e.total, e.criado, e.ultimo, e.pago ? Date.now() : 0, chave).run();
    if ((r.meta && r.meta.changes) === 1) novos++;
  }
  return { ok: true, emails: Object.keys(porEmail).length, jaPagaram: pagos, entraramNaFila: novos };
}

// ---------- utilitários ----------

function escHtml(t) { return String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]); }

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
