"""Motor de carrossel da Orbyt (1080x1350) e story (1080x1920).
Uso: python3 carrossel.py <spec.py>  -> PNGs em saida/<slug>/
O spec define SLUG e CARDS (lista de dicts). Tipos: capa, passo, final, texto.
"""
import sys, os, html, importlib.util
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
F = f'file://{BASE}/www/fonts'
P = f'file://{BASE}/prints'

CSS = f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700;font-stretch:75% 100%}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800;font-stretch:75% 112.5%}}
:root{{--gelo:#F1F3F5;--papel:#FFFFFF;--nevoa:#E6EAEE;--grafite:#16181B;--ardosia:#59606A;--sinal:#FF5A1F;--linha:#D9DEE3}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:var(--gelo);color:var(--grafite);font-family:I,sans-serif;position:relative}}
body.story,html.story{{height:1920px}}
body.escuro{{background:var(--grafite);color:var(--gelo)}}
.orbita{{position:absolute;inset:0;pointer-events:none}}
.topo{{position:absolute;left:96px;right:96px;top:78px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.marca{{display:flex;align-items:center;gap:14px;font-family:B;font-weight:700;font-stretch:88%;font-size:34px;letter-spacing:-.035em}}
.marca span{{font-weight:400;color:var(--ardosia)}}
.escuro .marca span{{color:#9AA1AB}}
.marca svg{{width:40px;height:40px}}
.cont{{font-family:M;font-size:22px;color:var(--ardosia);letter-spacing:.04em}}
.escuro .cont{{color:#9AA1AB}}
.pe{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;align-items:center;gap:28px;z-index:3}}
.barra{{flex:1;height:4px;background:var(--linha);border-radius:4px;overflow:hidden}}
.escuro .barra{{background:#2C3036}}
.barra i{{display:block;height:100%;background:var(--sinal);border-radius:4px}}
.arraste{{font-family:M;font-size:21px;color:var(--ardosia);letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}}
.escuro .arraste{{color:#9AA1AB}}
.miolo{{position:absolute;left:96px;right:96px;top:170px;bottom:150px;display:flex;flex-direction:column;z-index:2}}
.olho{{font-family:M;font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:var(--sinal);font-weight:500}}
h1{{font-family:B;font-weight:700;font-stretch:88%;letter-spacing:-.04em;line-height:.97;font-size:var(--t,96px);margin-top:22px}}
h1 em{{font-style:normal;color:var(--sinal)}}
.sub{{font-family:I;font-size:var(--s,36px);line-height:1.34;color:var(--ardosia);margin-top:26px;max-width:860px}}
.escuro .sub{{color:#B9C0C8}}
.sub b{{color:var(--grafite);font-weight:600}}
.escuro .sub b{{color:var(--gelo)}}
.visual.centro{{align-items:center}}
.visual{{flex:1;display:flex;align-items:flex-end;justify-content:center;gap:40px;margin-top:40px;min-height:0}}
/* celular */
.cel{{position:relative;height:100%;max-height:var(--ch,700px);aspect-ratio:390/844;border-radius:58px;padding:11px;
 background:linear-gradient(145deg,#8E9196,#3B3E43 30%,#6C6F75 55%,#2A2C30 80%,#7A7D82);box-shadow:0 40px 70px -40px rgba(22,24,27,.55),0 0 0 1.5px #1d1f22 inset}}
.cel .tela{{position:relative;width:100%;height:100%;border-radius:47px;overflow:hidden;background:#000}}
.cel .tela img{{width:100%;height:100%;object-fit:cover;object-position:top;display:block}}
.cel .ilha{{position:absolute;top:22px;left:50%;transform:translateX(-50%);width:30%;height:28px;border-radius:20px;background:#000;z-index:2}}
.cel .chip{{position:absolute;left:50%;top:-22px;transform:translateX(-50%);background:var(--grafite);color:var(--gelo);font-family:M;font-size:19px;letter-spacing:.04em;padding:12px 20px;border-radius:999px;white-space:nowrap;z-index:4;box-shadow:0 14px 30px -14px rgba(0,0,0,.5)}}
.cel .chip i{{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--sinal);margin-right:10px;vertical-align:1px}}
/* navegador */
.nav{{width:100%;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 40px 70px -40px rgba(22,24,27,.55),0 0 0 1.5px var(--linha)}}
.nav .barra-nav{{height:58px;background:var(--nevoa);display:flex;align-items:center;gap:12px;padding:0 22px}}
.nav .barra-nav b{{width:14px;height:14px;border-radius:50%;background:#C7CDD3}}
.nav .url{{margin-left:14px;flex:1;height:36px;border-radius:10px;background:#fff;display:flex;align-items:center;padding:0 16px;font-family:M;font-size:18px;color:var(--ardosia)}}
.nav img{{width:100%;display:block}}
/* conversa */
.conversa{{width:100%;background:#EFE7DE;border-radius:36px;padding:44px 36px;display:flex;flex-direction:column;gap:22px;box-shadow:0 40px 70px -40px rgba(22,24,27,.4)}}
.balao{{max-width:78%;padding:22px 26px 16px;border-radius:24px;font-size:31px;line-height:1.32;color:#111B21;position:relative}}
.balao small{{display:block;text-align:right;font-size:18px;color:#667781;margin-top:6px}}
.balao.eu{{align-self:flex-end;background:#D9FDD3;border-top-right-radius:6px}}
.balao.ela{{align-self:flex-start;background:#fff;border-top-left-radius:6px}}
.conversa .quem{{display:flex;align-items:center;gap:16px;font-weight:600;font-size:28px;color:#111B21;padding-bottom:14px;border-bottom:1px solid rgba(0,0,0,.08)}}
.conversa .quem svg{{width:54px;height:54px}}
/* barra de pagamento */
.pag{{width:100%;display:grid;grid-template-columns:1fr 1.7fr;gap:18px}}
.pag div{{border-radius:28px;padding:40px 36px;display:flex;flex-direction:column;gap:16px;min-height:380px;justify-content:flex-end}}
.pag .zero{{border:3px dashed #B7BEC6;color:var(--ardosia)}}
.pag .cem{{background:var(--sinal);color:#fff}}
.pag strong{{font-family:M;font-weight:600;font-size:66px;letter-spacing:-.04em;white-space:nowrap}}
.pag span{{font-size:32px;line-height:1.25}}
/* final */
.preco{{display:flex;align-items:flex-end;gap:22px;margin-top:34px}}
.preco strong{{font-family:M;font-weight:600;font-size:150px;letter-spacing:-.05em;line-height:.85}}
.preco span{{font-family:M;font-size:24px;color:#B9C0C8;line-height:1.35;padding-bottom:10px;text-transform:uppercase;letter-spacing:.06em}}
ul.checks{{list-style:none;margin-top:46px;display:grid;gap:20px}}
ul.checks li{{display:flex;gap:20px;align-items:center;font-size:36px}}
ul.checks li:before{{content:"";flex:none;width:36px;height:36px;border-radius:50%;background:var(--sinal) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 12.5l4 4L18 8'/%3E%3C/svg%3E") center/22px no-repeat}}
.cta{{margin-top:auto;border:2px solid #2E3238;border-radius:28px;padding:34px 36px;font-size:34px;line-height:1.32}}
.cta b{{color:var(--sinal);font-weight:600}}

/* busca */
.busca{{width:100%;background:#fff;border-radius:30px;padding:30px 30px 14px;box-shadow:0 40px 70px -40px rgba(22,24,27,.45),0 0 0 1.5px var(--linha)}}
.busca .campo{{display:flex;align-items:center;gap:16px;border:2px solid var(--linha);border-radius:999px;padding:18px 26px;font-size:30px;color:var(--grafite)}}
.busca .campo svg{{width:30px;height:30px;flex:none}}
.busca .res{{padding:24px 6px;border-bottom:1px solid var(--linha);display:flex;gap:20px;align-items:center}}
.busca .res:last-child{{border-bottom:0}}
.busca .res b{{display:block;font-size:29px;font-weight:600;color:#1a0dab}}
.busca .res span{{font-size:23px;color:var(--ardosia)}}
.busca .res i{{flex:none;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-family:M;font-size:24px;font-weight:700}}
.busca .res.ruim i{{background:#F3E2DD;color:#C2410C}}
.busca .res.bom{{background:#FFF1EB;border-radius:18px;padding-left:16px;border-bottom:0;margin-top:6px}}
.busca .res.bom i{{background:var(--sinal);color:#fff}}
/* lista */
ul.lista{{list-style:none;display:grid;gap:26px;width:100%}}
ul.lista li{{display:flex;gap:26px;align-items:flex-start;font-size:38px;line-height:1.25;background:#fff;border-radius:26px;padding:30px 32px;box-shadow:0 0 0 1.5px var(--linha)}}
ul.lista li i{{flex:none;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-family:M;font-weight:700;font-size:28px;margin-top:-2px}}
ul.lista.pode li i{{background:#E3F4E8;color:#1F7A3D}}
ul.lista.nao li i{{background:#FBE4DC;color:#C2410C}}
ul.lista.num li i{{background:var(--grafite);color:#fff}}
ul.lista li small{{display:block;font-size:27px;color:var(--ardosia);margin-top:8px;line-height:1.3}}
/* ficha */
.ficha{{width:100%;background:#fff;border-radius:30px;box-shadow:0 0 0 1.5px var(--linha);overflow:hidden}}
.ficha.destaque{{box-shadow:0 0 0 3px var(--sinal),0 40px 70px -40px rgba(255,90,31,.45)}}
.ficha div{{display:grid;grid-template-columns:250px 1fr;gap:24px;padding:28px 34px;border-bottom:1px solid var(--linha);align-items:baseline}}
.ficha div:last-child{{border-bottom:0}}
.ficha dt{{font-family:M;font-size:21px;text-transform:uppercase;letter-spacing:.06em;color:var(--ardosia)}}
.ficha dd{{font-size:33px;line-height:1.28}}
.ficha.destaque dd{{font-weight:500}}
.ficha.grande div{{grid-template-columns:330px 1fr;padding:34px 36px;align-items:center}}
.ficha.grande dt{{font-size:24px}}
.ficha.grande dd{{font-family:M;font-weight:600;font-size:46px;letter-spacing:-.03em}}
/* link de app generico */
.applink{{position:relative;height:100%;max-height:var(--ch,700px);aspect-ratio:390/844;border-radius:58px;padding:11px;background:linear-gradient(145deg,#8E9196,#3B3E43 30%,#6C6F75 55%,#2A2C30 80%,#7A7D82)}}
.applink .tela{{width:100%;height:100%;border-radius:47px;overflow:hidden;background:#F4F4F6;padding:70px 22px 22px;font-family:I;color:#333;display:flex;flex-direction:column;gap:14px}}
.applink .cab{{display:flex;gap:14px;align-items:center}}
.applink .cab b{{width:58px;height:58px;border-radius:50%;background:#C9CCD1}}
.applink .cab span{{display:block;height:16px;width:180px;background:#C9CCD1;border-radius:8px}}
.applink .cab span+span{{width:110px;margin-top:8px;background:#DADDE1}}
.applink .lin{{background:#fff;border-radius:14px;padding:16px;display:flex;justify-content:space-between;font-size:19px;color:#555}}
.applink .lin em{{font-style:normal;color:#888}}
.applink .btn{{margin-top:auto;background:#9AA0A6;color:#fff;border-radius:12px;text-align:center;padding:16px;font-size:20px}}
"""

LOGO = '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10.5" fill="none" stroke="currentColor" stroke-width="3.4"/><circle cx="24.4" cy="8.6" r="4.8" fill="{bg}"/><circle cx="24.4" cy="8.6" r="3.1" fill="#FF5A1F"/></svg>'

def orbita(escuro, alto=1350, ponto=True):
    c = 'rgba(241,243,245,.07)' if escuro else 'rgba(22,24,27,.07)'
    return f'''<svg class="orbita" viewBox="0 0 1080 {alto}"><circle cx="1010" cy="{alto*0.22:.0f}" r="560" fill="none" stroke="{c}" stroke-width="2"/>
    {'<circle cx="%.0f" cy="%.0f" r="9" fill="#FF5A1F" opacity=".9"/>' % (1010-560*0.7071, alto*0.22+560*0.7071) if ponto else ''}</svg>'''

def cel(img, chip=None, ch=None):
    c = f'<span class="chip"><i></i>{chip}</span>' if chip else ''
    st = f' style="--ch:{ch}px"' if ch else ''
    return f'<div class="cel"{st}>{c}<div class="tela"><span class="ilha"></span><img src="{P}/{img}"></div></div>'

def navegador(img, url, w=None):
    st = f' style="max-width:{w}px"' if w else ''
    return f'<div class="nav"{st}><div class="barra-nav"><b></b><b></b><b></b><div class="url">{html.escape(url)}</div></div><img src="{P}/{img}"></div>'

def conversa(nome, msgs):
    av = '<svg viewBox="0 0 54 54"><circle cx="27" cy="27" r="27" fill="#16181B"/><g transform="translate(27 27) scale(1.05) translate(-16 -16)"><circle cx="16" cy="16" r="10.5" fill="none" stroke="#F1F3F5" stroke-width="3.4"/><circle cx="24.4" cy="8.6" r="4.8" fill="#16181B"/><circle cx="24.4" cy="8.6" r="3.1" fill="#FF5A1F"/></g></svg>'
    b = ''.join(f'<div class="balao {q}">{html.escape(t)}<small>{h}</small></div>' for q, t, h in msgs)
    return f'<div class="conversa"><div class="quem">{av}{html.escape(nome)}</div>{b}</div>'

def pagamento():
    return ('<div class="pag"><div class="zero"><strong>R$ 0</strong><span>pra começar</span></div>'
            '<div class="cem"><strong>100%</strong><span>só depois que você aprova o site pronto</span></div></div>')


def busca(q, res):
    lupa = '<svg viewBox="0 0 24 24" fill="none" stroke="#59606A" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'
    r = ''.join(f'<div class="res {c}"><i>{"✓" if c=="bom" else "✕"}</i><div><b>{html.escape(a)}</b><span>{html.escape(b)}</span></div></div>' for c, a, b in res)
    return f'<div class="busca"><div class="campo">{lupa}{html.escape(q)}</div>{r}</div>'

def lista(itens, tipo='pode'):
    ic = {'pode': '✓', 'nao': '✕'}
    li = ''
    for k, it in enumerate(itens, 1):
        a, b = (it if isinstance(it, tuple) else (it, ''))
        i = str(k) if tipo == 'num' else ic[tipo]
        li += f'<li><i>{i}</i><div>{a}{f"<small>{b}</small>" if b else ""}</div></li>'
    return f'<ul class="lista {tipo}">{li}</ul>'

def ficha(linhas, destaque=False, grande=False):
    d = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in linhas)
    return f'<dl class="ficha{" destaque" if destaque else ""}{" grande" if grande else ""}">{d}</dl>'

def applink(ch=None, chip=None, linhas=('Corte', 'Barba', 'Corte + barba', 'Sobrancelha', 'Pezinho', 'Hidratação')):
    st = f' style="--ch:{ch}px"' if ch else ''
    c = f'<span class="chip" style="background:#59606A"><i style="background:#C9CCD1"></i>{chip}</span>' if chip else ''
    l = ''.join(f'<div class="lin">{x}<em>ver horários</em></div>' for x in linhas)
    return f'<div class="applink cel"{st}>{c}<div class="tela"><div class="cab"><b></b><div><span></span><span></span></div></div>{l}<div class="btn">Agendar</div></div></div>'

def pagina(card, i, n, story=False):
    tipo = card.get('tipo', 'passo')
    escuro = tipo == 'final' or card.get('escuro')
    bg = '#16181B' if escuro else '#F1F3F5'
    alto = 1920 if story else 1350
    cls = ('escuro ' if escuro else '') + ('story' if story else '')
    t = card.get('t'); s = card.get('s')
    estilo = ''
    if t: estilo += f'--t:{t}px;'
    if s: estilo += f'--s:{s}px;'
    topo = f'<div class="topo"><div class="marca">{LOGO.format(bg=bg)}Orbyt <span>Studio</span></div><div class="cont">{i:02d}/{n:02d}</div></div>'
    pe = '' if story else (f'<div class="pe"><div class="barra"><i style="width:{i/n*100:.1f}%"></i></div>'
          + ('<div class="arraste">arraste →</div>' if i < n else '<div class="arraste">link no perfil</div>') + '</div>')
    corpo = card.get('olho', '') and f'<div class="olho">{card["olho"]}</div>'
    corpo += f'<h1>{card["titulo"]}</h1>'
    if card.get('texto'): corpo += f'<p class="sub">{card["texto"]}</p>'
    if tipo == 'final':
        corpo += f'<div class="preco"><strong>{card["preco"]}</strong><span>{card["preco_nota"]}</span></div>'
        corpo += '<ul class="checks">' + ''.join(f'<li>{x}</li>' for x in card['checks']) + '</ul>'
        corpo += f'<div class="cta">{card["cta"]}</div>'
    if card.get('visual'):
        corpo += f'<div class="visual{" centro" if card.get("centro") else ""}">{card["visual"]}</div>'
    return f'''<!doctype html><html class="{'story' if story else ''}"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{cls}" style="{estilo}">{orbita(escuro, alto, card.get('ponto', tipo != 'final'))}{topo}<div class="miolo">{corpo}</div>{pe}</body></html>'''

def render(spec_path):
    spec = importlib.util.spec_from_file_location('spec', spec_path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    out = f'{BASE}/saida/{m.SLUG}'; os.makedirs(out, exist_ok=True)
    n = len(m.CARDS)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for i, c in enumerate(m.CARDS, 1):
            f = f'{out}/_c{i}.html'; open(f, 'w', encoding='utf-8').write(pagina(c, i, n))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(250)
            pg.screenshot(path=f'{out}/{i:02d}.png')
        b.close()
    print('ok', out, n)
    return out

if __name__ == '__main__':
    render(sys.argv[1])
