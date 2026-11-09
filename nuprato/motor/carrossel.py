"""Motor de carrossel do NuPrato (1080x1350), no padrão de posts do Matheus adaptado pra marca.
Uso: python3 carrossel.py posts/<spec>.py   -> PNGs em saida/<SLUG>/01.png ...
O spec define SLUG e CARDS (lista de dicts).

Campos de um card:
  tipo   'capa' | 'meio' | 'final'   (final = card de oferta verde com selo dourado)
  tema   'creme' | 'papel' | 'verde' | 'escuro'
  selo   etiqueta pequena acima do título (pílula)
  olho   linha pequena verde acima do título
  titulo HTML; <em> vira marca-texto amarelo
  texto  apoio (até 40 palavras)
  nota   anotação à mão (Caveat) embaixo do título
  carimbo ('MITO','mito') ou ('VERDADE','verdade')
  visual HTML de um dos helpers abaixo
  foto   caminho de uma cena (foto 9:16 ou 4:5) em tela cheia; use tema='foto'. fy = foco vertical em %, baixo=True = texto embaixo
  t, s   tamanho do título e do texto em px
"""
import sys, os, html, json, importlib.util, base64
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(BASE, 'marca.json'), encoding='utf-8'))
C = M['cores']
F = f'file://{BASE}/fontes'
SELO = f'file://{BASE}/img/selo-ouro.png'
W, H = 1080, 1350

# ---------- logo Livro servido ----------
def logo(fg, bg, w=64, reforcado=False):
    sw = (28, 30, 24, 27) if not reforcado else (34, 36, 30, 32)
    return (f'<svg viewBox="0 100 512 380" width="{w}" height="{w*380/512:.0f}" fill="none" aria-hidden="true">'
            f'<ellipse cx="256" cy="400" rx="222" ry="62" stroke="{fg}" stroke-width="{sw[0]-6}" fill="{bg}"/>'
            '<g transform="translate(256 392) scale(0.7) translate(-256 -408)">'
            f'<path d="M64 144 C64 132 74 124 86 124 H236 C248 124 256 132 256 144 V408 C256 408 246 396 224 392 C190 386 130 388 96 396 C80 400 72 396 68 388 C66 384 64 380 64 374 Z" stroke="{fg}" stroke-width="{sw[0]}" stroke-linejoin="round" fill="{bg}"/>'
            f'<path d="M448 144 C448 132 438 124 426 124 H276 C264 124 256 132 256 144 V408 C256 408 266 396 288 392 C322 386 382 388 416 396 C432 400 440 396 444 388 C446 384 448 380 448 374 Z" stroke="{fg}" stroke-width="{sw[0]}" stroke-linejoin="round" fill="{bg}"/>'
            f'<path d="M256 144 V408" stroke="{fg}" stroke-width="{sw[2]}" stroke-linecap="round"/>'
            f'<path d="M0 0 C 18 -28, 46 -42, 68 -33 C 94 -22, 94 22, 68 33 C 46 42, 18 28, 0 0 C -18 -28, -46 -42, -68 -33 C -94 -22, -94 22, -68 33 C -46 42, -18 28, 0 0 Z" transform="translate(256 268) scale(0.92)" stroke="{fg}" stroke-width="{sw[3]}" stroke-linejoin="round" fill="none"/>'
            f'<path d="M150 124 V200 L170 182 L190 200 V124 Z" fill="{C["dourado"]}"/></g></svg>')

TEMAS = {
    'creme':  dict(bg=C['creme'], fg=C['grafite'], sec=C['texto_sec'], olho=C['verde_escuro'], logo_fg=C['verde'], mao=C['verde_escuro']),
    'papel':  dict(bg=C['papel'], fg=C['grafite'], sec=C['texto_sec'], olho=C['verde_escuro'], logo_fg=C['verde'], mao=C['verde_escuro']),
    'verde':  dict(bg=C['verde'], fg=C['creme'], sec='#E4EFE7', olho=C['amarelo'], logo_fg=C['creme'], mao=C['creme']),
    'escuro': dict(bg=C['grafite'], fg=C['creme'], sec='#C9CCC8', olho=C['amarelo'], logo_fg=C['creme'], mao=C['amarelo']),
    'foto':   dict(bg='#1d1f20', fg='#FFFFFF', sec='#EDEDE8', olho=C['amarelo'], logo_fg='#FFFFFF', mao=C['amarelo']),
}

CSS = f"""
@font-face{{font-family:P;src:url({F}/{M['letras']['texto']});font-weight:400}}
@font-face{{font-family:P;src:url({F}/{M['letras']['texto_medio']});font-weight:500}}
@font-face{{font-family:P;src:url({F}/{M['letras']['texto_bold']});font-weight:700}}
@font-face{{font-family:P;src:url({F}/{M['letras']['titulo']});font-weight:800}}
@font-face{{font-family:K;src:url({F}/{M['letras']['mao']});font-weight:400 700}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:P,sans-serif;position:relative;background:var(--bg);color:var(--fg)}}
body.papel{{background-color:{C['papel']};background-image:linear-gradient({C['pauta']} 1.5px,transparent 1.5px);background-size:100% 66px;background-position:0 18px}}
body.papel:before{{content:"";position:absolute;left:86px;top:0;bottom:0;width:3px;background:{C['margem']};opacity:.55}}
.grao{{position:absolute;inset:0;pointer-events:none;opacity:.55}}
.topo{{position:absolute;left:84px;right:84px;top:64px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.marca{{display:flex;align-items:center;gap:12px;font-weight:700;font-size:32px;letter-spacing:-.02em}}
.cont{{font-weight:500;font-size:22px;color:var(--sec);letter-spacing:.06em}}
.miolo{{position:absolute;left:84px;right:84px;top:168px;bottom:156px;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:2}}
.miolo.meio{{justify-content:center}}
.pilula{{display:inline-block;font-weight:700;font-size:22px;letter-spacing:.1em;text-transform:uppercase;border:3px solid currentColor;border-radius:999px;padding:10px 24px;margin-bottom:30px;color:var(--olho)}}
.olho{{font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:var(--olho)}}
h1{{font-weight:800;letter-spacing:-.035em;line-height:1.12;font-size:var(--t,92px);margin-top:18px}}
h1 em{{font-style:normal;background:linear-gradient(transparent 14%,{C['amarelo']} 14%,{C['amarelo']} 94%,transparent 94%);color:{C['grafite']};padding:0 .12em;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.sub{{font-size:var(--s,40px);line-height:1.36;color:var(--sec);margin-top:28px;max-width:860px}}
.sub b{{color:var(--fg);font-weight:700}}
.mao{{font-family:K;font-weight:700;font-size:56px;color:var(--mao);margin-top:22px;transform:rotate(-3deg);line-height:1.05}}
.visual{{flex:1;display:flex;align-items:center;justify-content:center;width:100%;margin-top:34px;min-height:0}}
.visual.cima{{align-items:center}}
.pe{{position:absolute;left:84px;right:84px;bottom:70px;display:flex;align-items:center;justify-content:space-between;z-index:3}}
.pontos{{display:flex;gap:10px}}
.pontos i{{width:12px;height:12px;border-radius:50%;background:var(--sec);opacity:.35}}
.pontos i.on{{opacity:1;background:var(--olho);width:34px;border-radius:8px}}
.arrasta{{display:flex;align-items:center;gap:14px;background:{C['grafite']};color:{C['creme']};border-radius:999px;padding:10px 12px 10px 28px;font-weight:700;font-size:24px}}
.arrasta span{{width:46px;height:46px;border-radius:50%;background:{C['creme']};display:grid;place-items:center}}
.escuro .arrasta,.verde .arrasta{{background:{C['creme']};color:{C['grafite']}}}
.escuro .arrasta span,.verde .arrasta span{{background:{C['grafite']}}}
/* ficha de receita */
.ficha{{position:relative;width:860px;background:{C['papel']};border-radius:8px;padding:76px 56px 44px 96px;text-align:left;color:{C['grafite']};
 background-image:linear-gradient({C['pauta']} 1.5px,transparent 1.5px);background-size:100% 64px;background-position:0 52px;
 box-shadow:0 30px 50px -26px rgba(30,40,32,.45),0 0 0 1.5px #E6E0D4;transform:rotate(var(--rot,-1.2deg))}}
.ficha:before{{content:"";position:absolute;left:70px;top:0;bottom:0;width:2.5px;background:{C['margem']};opacity:.7}}
.ficha .fita{{position:absolute;left:50%;top:-22px;width:170px;height:46px;transform:translateX(-50%) rotate(-3deg);background:rgba(244,211,94,.78);
 clip-path:polygon(3% 0,97% 8%,100% 30%,97% 52%,100% 74%,96% 100%,4% 93%,0 70%,3% 48%,0 24%)}}
.ficha .num{{position:absolute;right:40px;top:26px;font-weight:700;font-size:20px;letter-spacing:.14em;color:#6E7376}}
.ficha .tit{{font-weight:800;font-size:44px;letter-spacing:-.02em;line-height:1.1;margin-bottom:14px}}
.ficha .tit em{{font-style:normal;background:{C['amarelo']};padding:0 6px;border-radius:4px}}
.ficha ul{{list-style:none}}
.ficha li{{font-family:K;font-weight:700;font-size:50px;line-height:64px;display:flex;gap:18px;align-items:center}}
.ficha li.x{{color:#9A9C9A;text-decoration:line-through;text-decoration-thickness:4px;text-decoration-color:{C['mito']}}}
.ficha li svg{{flex:none;width:44px;height:44px}}
.ficha .rodape{{font-weight:700;font-size:24px;color:{C['verde_escuro']};margin-top:16px;letter-spacing:.02em}}
.ficha .rodape.ruim{{color:{C['mito']}}}
/* par de fichas */
.par{{display:grid;grid-template-columns:1fr 1fr;gap:34px;width:100%;align-items:start}}
.par .ficha{{width:100%;padding:70px 26px 30px 54px;background-size:100% 56px;background-position:0 48px}}
.par .ficha:before{{left:38px}}
.par .ficha .tit{{font-size:32px}}
.par .ficha li{{font-size:38px;line-height:56px;gap:10px}}
.par .ficha li svg{{width:32px;height:32px}}
.par .ficha .num{{right:22px;top:22px;font-size:16px}}
.par .rot{{font-weight:800;font-size:26px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:26px}}
/* conversa */
.conversa{{width:900px;background:#EFE7DE;border-radius:36px;padding:36px 34px 40px;display:flex;flex-direction:column;gap:20px;text-align:left;box-shadow:0 30px 60px -36px rgba(30,40,32,.5)}}
.conversa .quem{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:30px;color:#111B21;padding-bottom:16px;border-bottom:1px solid rgba(0,0,0,.08)}}
.conversa .av{{width:58px;height:58px;border-radius:50%;background:#C9CCD1;display:grid;place-items:center}}
.balao{{max-width:80%;padding:20px 26px 14px;border-radius:24px;font-size:33px;line-height:1.3;color:#111B21}}
.balao small{{display:block;text-align:right;font-size:19px;color:#667781;margin-top:4px}}
.balao.eu{{align-self:flex-end;background:#D9FDD3;border-top-right-radius:6px}}
.balao.ela{{align-self:flex-start;background:#fff;border-top-left-radius:6px}}
/* busca */
.busca{{width:900px;background:#fff;border-radius:30px;padding:30px 30px 16px;text-align:left;box-shadow:0 30px 60px -36px rgba(30,40,32,.5),0 0 0 1.5px #E6E0D4}}
.busca .campo{{display:flex;align-items:center;gap:16px;border:2px solid #DADCE0;border-radius:999px;padding:18px 26px;font-size:32px;color:#202124}}
.busca .res{{padding:24px 8px;border-bottom:1px solid #ECECEC;display:flex;gap:20px;align-items:center}}
.busca .res:last-child{{border-bottom:0}}
.busca .res b{{display:block;font-size:30px;font-weight:700;color:#1a0dab;line-height:1.25}}
.busca .res span{{font-size:24px;color:#5F6368}}
.busca .res i{{flex:none;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-weight:800;font-size:26px;background:#F6DDD3;color:{C['mito']}}}
.busca .res.bom{{background:#EAF3EC;border-radius:18px;padding-left:18px;border-bottom:0;margin-top:8px}}
.busca .res.bom b{{color:{C['verde_escuro']}}}
.busca .res.bom i{{background:{C['verde']};color:#fff}}
/* carimbo */
.carimbo{{display:inline-block;font-weight:800;font-size:76px;letter-spacing:.14em;padding:10px 40px;border:8px solid currentColor;border-radius:18px;transform:rotate(-6deg);margin-bottom:46px}}
.carimbo.mito{{color:{C['mito']}}} .carimbo.verdade{{color:{C['verde_escuro']}}}
.escuro .carimbo.mito{{color:{C['laranja']}}} .escuro .carimbo.verdade{{color:{C['amarelo']}}}
/* número */
.numero{{display:flex;flex-direction:column;align-items:center;gap:6px}}
.numero strong{{font-weight:800;font-size:var(--nz,300px);letter-spacing:-.06em;line-height:.9}}
.numero span{{font-size:52px;font-weight:700;color:var(--fg)!important;max-width:820px;line-height:1.3;color:var(--sec)}}
/* lista numerada */
ul.lista{{list-style:none;display:grid;gap:22px;width:100%;text-align:left}}
ul.lista li{{display:flex;gap:26px;align-items:center;font-size:36px;font-weight:700;line-height:1.22;background:{C['papel']};color:{C['grafite']};border-radius:24px;padding:26px 32px;box-shadow:0 0 0 1.5px #E6E0D4}}
ul.lista li i{{flex:none;width:60px;height:60px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-weight:800;font-size:30px;background:{C['verde']};color:{C['creme']}}}
ul.lista li small{{display:block;font-size:27px;font-weight:400;color:{C['texto_sec']};margin-top:6px}}
/* card de foto (cena real gerada, tela cheia) */
body.foto{{background-color:#1d1f20;background-size:cover;background-repeat:no-repeat}}
.sombra{{position:absolute;inset:0;z-index:1;pointer-events:none}}
.foto h1{{text-shadow:0 4px 28px rgba(0,0,0,.55)}}
.foto h1 em{{text-shadow:none}}
.foto .sub{{text-shadow:0 2px 14px rgba(0,0,0,.7);color:#fff}}
.foto .olho{{text-shadow:0 2px 10px rgba(0,0,0,.6)}}
.foto .miolo.baixo{{justify-content:flex-end}}
.foto .marca,.foto .cont{{text-shadow:0 2px 10px rgba(0,0,0,.5)}}
.foto .arrasta{{background:{C['creme']};color:{C['grafite']}}}
.foto .arrasta span{{background:{C['grafite']}}}
/* card final */
.final .miolo{{justify-content:flex-start}}
.final .selo{{width:380px;height:380px;margin:6px auto 0;transform:rotate(-8deg);filter:drop-shadow(0 22px 26px rgba(20,40,28,.35))}}
.final .oferta{{margin-top:auto;background:{C['papel']};color:{C['grafite']};border-radius:22px;padding:26px 40px;transform:rotate(-1.5deg);box-shadow:0 22px 36px -18px rgba(20,40,28,.6)}}
.final .oferta b{{display:block;font-weight:800;font-size:44px;line-height:1.1}}
.final .oferta span{{display:block;font-weight:700;font-size:28px;color:{C['verde_escuro']};margin-top:6px}}
"""

SETA = f'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{C["verde"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SETA_ESC = f'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{C["amarelo"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = (f'<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="4" y="6" width="28" height="28" rx="4" stroke="{C["grafite"]}" stroke-width="2.6" fill="none" transform="rotate(-3 18 20)"/>'
         f'<path d="M9 20 L17 29 L37 4" stroke="{C["verde_escuro"]}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CAIXA = f'<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="4" y="6" width="28" height="28" rx="4" stroke="{C["grafite"]}" stroke-width="2.6" fill="none" transform="rotate(2 18 20)"/></svg>'
XIS = (f'<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="4" y="6" width="28" height="28" rx="4" stroke="{C["grafite"]}" stroke-width="2.6" fill="none" transform="rotate(-2 18 20)"/>'
       f'<path d="M10 12 L28 30 M28 12 L10 30" stroke="{C["mito"]}" stroke-width="4.5" stroke-linecap="round"/></svg>')

# ---------- helpers de visual ----------
def ficha(titulo, itens, numero=None, rodape=None, ruim=False, rot=-1.2, fita=True):
    """itens: lista de str (check), ('x', str) riscado, ('o', str) caixa vazia."""
    li = ''
    for it in itens:
        k, t = it if isinstance(it, tuple) else ('v', it)
        ic = {'v': CHECK, 'x': XIS, 'o': CAIXA}[k]
        li += f'<li class="{"x" if k == "x" else ""}">{ic}<span>{t}</span></li>'
    n = f'<span class="num">FICHA Nº {numero}</span>' if numero else ''
    r = f'<div class="rodape{" ruim" if ruim else ""}">{rodape}</div>' if rodape else ''
    f = '<span class="fita"></span>' if fita else ''
    return f'<div class="ficha" style="--rot:{rot}deg">{f}{n}<div class="tit">{titulo}</div><ul>{li}</ul>{r}</div>'

def par(a, b, rot_a='Receita de caderno', rot_b='Receita NuPrato'):
    return (f'<div class="par"><div><div class="rot" style="color:{C["mito"]}">{rot_a}</div>{a}</div>'
            f'<div><div class="rot" style="color:{C["verde_escuro"]}">{rot_b}</div>{b}</div></div>')

def conversa(nome, msgs):
    av = '<span class="av"><svg viewBox="0 0 54 54" width="58" height="58"><circle cx="27" cy="21" r="9" fill="#F1F3F5"/><path d="M10 46c3-10 10-14 17-14s14 4 17 14" fill="#F1F3F5"/></svg></span>'
    b = ''.join(f'<div class="balao {q}">{html.escape(t)}<small>{h}</small></div>' for q, t, h in msgs)
    return f'<div class="conversa"><div class="quem">{av}{html.escape(nome)}</div>{b}</div>'

def busca(q, res):
    lupa = '<svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#5F6368" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'
    r = ''.join(f'<div class="res {c}"><i>{"✓" if c == "bom" else "✕"}</i><div><b>{html.escape(a)}</b><span>{html.escape(b)}</span></div></div>' for c, a, b in res)
    return f'<div class="busca"><div class="campo">{lupa}{html.escape(q)}</div>{r}</div>'

def numero(valor, rotulo, tam=None):
    st = f' style="--nz:{tam}px"' if tam else ''
    return f'<div class="numero"{st}><strong>{valor}</strong><span>{rotulo}</span></div>'

def lista(itens):
    li = ''
    for k, it in enumerate(itens, 1):
        a, b = it if isinstance(it, tuple) else (it, '')
        li += f'<li><i>{k}</i><div>{a}{f"<small>{b}</small>" if b else ""}</div></li>'
    return f'<ul class="lista">{li}</ul>'

GRAO = ('<svg class="grao" viewBox="0 0 1080 1350" aria-hidden="true"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="9"/>'
        '<feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .12"/></feComponentTransfer></filter><rect width="1080" height="1350" filter="url(#g)"/></svg>')

def pagina(card, i, n):
    tipo = card.get('tipo', 'meio')
    tema = card.get('tema') or ('verde' if tipo == 'final' else 'creme')
    T = TEMAS[tema]
    var = ';'.join(f'--{k}:{v}' for k, v in T.items() if k in ('bg', 'fg', 'sec', 'olho', 'mao'))
    if card.get('t'): var += f';--t:{card["t"]}px'
    if card.get('s'): var += f';--s:{card["s"]}px'
    topo = (f'<div class="topo"><div class="marca">{logo(T["logo_fg"], T["bg"] if tema != "papel" else C["papel"], 58)}<span>{M["nome"]}</span></div>'
            + (f'<div class="cont">{i:02d}/{n:02d}</div>' if n > 1 else f'<div class="cont">@{M["handle"]}</div>') + '</div>')
    pontos = '<div class="pontos">' + ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, n + 1)) + '</div>'
    seta = SETA if tema not in ('escuro', 'verde') else SETA_ESC
    if i < n:
        pe = f'<div class="pe">{pontos}<div class="arrasta">{M["textos"]["arraste"]}<span>{seta}</span></div></div>'
    else:
        pe = f'<div class="pe">{pontos}<div class="cont">@{M["handle"]}</div></div>' if tipo != 'final' else f'<div class="pe" style="justify-content:center">{pontos}</div>'
    if n == 1:
        pe = ''
    c = ''
    if card.get('carimbo'): c += f'<div class="carimbo {card["carimbo"][1]}">{card["carimbo"][0]}</div>'
    if card.get('selo'): c += f'<div class="pilula">{card["selo"]}</div>'
    if card.get('olho'): c += f'<div class="olho">{card["olho"]}</div>'
    if tipo == 'final':
        c += f'<img class="selo" src="{SELO}" alt="">'
    if card.get('titulo'): c += f'<h1>{card["titulo"]}</h1>'
    if card.get('texto'): c += f'<p class="sub">{card["texto"]}</p>'
    if card.get('nota'): c += f'<div class="mao">{card["nota"]}</div>'
    if card.get('visual'):
        c += f'<div class="visual{" cima" if card.get("cima") else ""}">{card["visual"]}</div>'
    if tipo == 'final':
        c += (f'<div class="oferta"><b>{card.get("oferta", M["textos"]["oferta"])}</b>'
              f'<span>{card.get("cta", M["textos"]["fim"])}</span></div>')
    centro = ' meio' if (card.get('centro') or (not card.get('visual') and tipo != 'final')) else ''
    cls = tema + (' final' if tipo == 'final' else '')
    grao = GRAO if tema in ('verde', 'escuro') else ''
    sombra = ''
    if card.get('foto'):
        # foto: caminho da cena; fy: foco vertical em % (0 = topo); baixo=True põe o texto embaixo
        var += f";background-image:url(file://{card['foto']});background-position:center {card.get('fy', 40)}%"
        baixo = card.get('baixo')
        g = ('linear-gradient(to top, rgba(0,0,0,.80) 0%, rgba(0,0,0,.45) 34%, rgba(0,0,0,0) 58%), linear-gradient(to bottom, rgba(0,0,0,.45), rgba(0,0,0,0) 22%)' if baixo else
             'linear-gradient(to bottom, rgba(0,0,0,.78) 0%, rgba(0,0,0,.42) 34%, rgba(0,0,0,0) 58%), linear-gradient(to top, rgba(0,0,0,.45), rgba(0,0,0,0) 22%)')
        sombra = f'<div class="sombra" style="background:{g}"></div>'
        centro = ' baixo' if baixo else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="{cls}" style="{var}">{grao}{sombra}{topo}<div class="miolo{centro}">{c}</div>{pe}</body></html>')

def render(spec_path, so=None):
    """O spec tem SLUG + CARDS (um post) ou POSTS = [(slug, cards), ...] (vários)."""
    sp = importlib.util.spec_from_file_location('spec', spec_path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    posts = getattr(m, 'POSTS', None) or [(m.SLUG, m.CARDS)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H})
        for slug, cards in posts:
            if so and slug not in so: continue
            _render(pg, slug, cards)
        b.close()

def _render(pg, slug, cards):
    class _M: pass
    m = _M(); m.SLUG = slug; m.CARDS = cards
    out = f'{BASE}/saida/{m.SLUG}'; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith('.png'): os.remove(os.path.join(out, f))
    n = len(m.CARDS)
    if True:
        for i, c in enumerate(m.CARDS, 1):
            f = f'{out}/_c{i}.html'; open(f, 'w', encoding='utf-8').write(pagina(c, i, n))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
            # confere se algo vazou pra fora do miolo
            vaza = pg.evaluate('''() => { const m = document.querySelector('.miolo'); const r = m.getBoundingClientRect();
                return m.scrollHeight > m.clientHeight + 2 ? (m.scrollHeight - m.clientHeight) : 0 }''')
            if vaza: print(f'AVISO {m.SLUG} card {i}: conteúdo passa {vaza}px do miolo')
            pg.screenshot(path=f'{out}/{i:02d}.png')
    print('ok', out, n)
    return out

if __name__ == '__main__':
    so = os.environ.get('SO', '').split(',') if os.environ.get('SO') else None
    for a in sys.argv[1:]:
        render(a, so)
