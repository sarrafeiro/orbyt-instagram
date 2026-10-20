"""Stories da Orbyt 1080x1920. Tipos: novo (capa de post), frase (fundo escuro), modelo (celular)."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.path.dirname(os.path.abspath(__file__)); F = f'file://{BASE}/www/fonts'
CSS = f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{background:#F1F3F5;color:#16181B;font-family:I;position:relative}} body.escuro{{background:#16181B;color:#F1F3F5}}
.marca{{position:absolute;left:90px;top:250px;display:flex;align-items:center;gap:14px;font-family:B;font-weight:700;font-stretch:88%;font-size:38px;letter-spacing:-.035em}}
.marca span{{font-weight:400;color:#59606A}} .escuro .marca span{{color:#9AA1AB}} .marca svg{{width:44px;height:44px}}
.olho{{font-family:M;font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:#FF5A1F}}
h1{{font-family:B;font-weight:700;font-stretch:88%;letter-spacing:-.04em;line-height:.98;font-size:var(--t,92px)}}
h1 em{{font-style:normal;color:#FF5A1F}}
.bloco{{position:absolute;left:90px;right:90px;top:360px;display:flex;flex-direction:column;gap:22px}}
.capa{{position:absolute;left:150px;right:150px;bottom:330px;border-radius:34px;overflow:hidden;box-shadow:0 50px 90px -40px rgba(22,24,27,.55),0 0 0 1.5px #D9DEE3}}
.capa img{{width:100%;display:block}}
.pe{{position:absolute;left:90px;right:90px;bottom:250px;font-family:M;font-size:26px;letter-spacing:.06em;text-transform:uppercase;color:#59606A;text-align:center}}
.escuro .pe{{color:#9AA1AB}}
.sub{{font-size:44px;line-height:1.3;color:#59606A}} .escuro .sub{{color:#B9C0C8}} .sub b{{color:#FF5A1F;font-weight:600}}
.preco{{font-family:M;font-weight:600;font-size:170px;letter-spacing:-.05em;line-height:.9;margin-top:30px}}
.cel{{position:absolute;left:50%;transform:translateX(-50%);bottom:330px;height:960px;aspect-ratio:390/844;border-radius:76px;padding:15px;background:linear-gradient(145deg,#8E9196,#3B3E43 30%,#6C6F75 55%,#2A2C30 80%,#7A7D82);box-shadow:0 50px 90px -50px rgba(22,24,27,.6)}}
.cel img{{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:62px;display:block}}
"""
def logo(bg, fg):
    return f'<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10.5" fill="none" stroke="{fg}" stroke-width="3.4"/><circle cx="24.4" cy="8.6" r="4.8" fill="{bg}"/><circle cx="24.4" cy="8.6" r="3.1" fill="#FF5A1F"/></svg>'

def pagina(s):
    esc = s.get('escuro'); bg, fg = ('#16181B', '#F1F3F5') if esc else ('#F1F3F5', '#16181B')
    corpo = f'<div class="marca">{logo(bg, fg)}Orbyt <span>Studio</span></div><div class="bloco">'
    if s.get('olho'): corpo += f'<div class="olho">{s["olho"]}</div>'
    corpo += f'<h1>{s["titulo"]}</h1>'
    if s.get('sub'): corpo += f'<p class="sub">{s["sub"]}</p>'
    if s.get('preco'): corpo += f'<div class="preco">{s["preco"]}</div>'
    corpo += '</div>'
    if s.get('capa'): corpo += f'<div class="capa"><img src="file://{s["capa"]}"></div>'
    if s.get('cel'): corpo += f'<div class="cel"><img src="file://{BASE}/prints/{s["cel"]}"></div>'
    if s.get('pe'): corpo += f'<div class="pe">{s["pe"]}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{"escuro" if esc else ""}" style="--t:{s.get("t",92)}px">{corpo}</body></html>'

def render(lista, pasta):
    os.makedirs(pasta, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        for s in lista:
            f = f'{pasta}/{s["nome"]}.html'; open(f, 'w', encoding='utf-8').write(pagina(s))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
            pg.screenshot(path=f'{pasta}/{s["nome"]}.png'); print('ok', s['nome'])
        b.close()
