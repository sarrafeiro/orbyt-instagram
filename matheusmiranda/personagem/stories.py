import os, sys
from playwright.sync_api import sync_playwright
F='file:///home/claude/insta-pessoal/motor/fontes'
C=dict(papel='#FCF4E1', navy='#1E2B4A', laranja='#E2492F', amarelo='#F2C94C')
CSS=f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{font-family:I;position:relative;background:{C['papel']};color:{C['navy']}}}
body.navy{{background:{C['navy']};color:{C['papel']}}} body.laranja{{background:{C['laranja']};color:{C['papel']}}}
.painel{{position:absolute;inset:30px;border:6px solid {C['navy']};border-radius:6px}}
.navy .painel{{border-color:{C['papel']}}} .laranja .painel{{border-color:{C['navy']}}}
.txt{{position:absolute;left:100px;right:100px;top:300px;bottom:300px;display:flex;flex-direction:column;justify-content:center}}
.tag{{align-self:flex-start;font-family:M;font-weight:600;font-size:30px;letter-spacing:.08em;text-transform:uppercase;background:{C['amarelo']};color:{C['navy']};padding:12px 22px;border:3px solid {C['navy']};transform:rotate(-2deg);margin-bottom:40px}}
h1{{font-family:B;font-weight:800;font-stretch:85%;letter-spacing:-.035em;line-height:.98;font-size:var(--t,120px)}}
h1 em{{font-style:normal;color:{C['laranja']}}} .navy h1 em{{color:{C['amarelo']}}} .laranja h1 em{{color:{C['navy']}}}
.sub{{font-size:52px;line-height:1.3;margin-top:36px;opacity:.88}}
.pe{{position:absolute;left:100px;right:100px;bottom:120px;font-family:M;font-size:30px;letter-spacing:.05em}}
"""
def html(s):
    t=f'--t:{s["t"]}px' if s.get('t') else ''
    tag=f'<span class="tag">{s["tag"]}</span>' if s.get('tag') else ''
    sub=f'<p class="sub">{s["sub"]}</p>' if s.get('sub') else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{s.get("fundo","papel")}" style="{t}"><div class="painel"></div><div class="txt">{tag}<h1>{s["titulo"]}</h1>{sub}</div><div class="pe">@matheusmiranda.ia</div></body></html>'
L=[
 dict(nome='2026-11-12-1240', fundo='navy', tag='Post novo', titulo='12 anos vendendo. <em>Agora eu construo com IA.</em>', sub='Primeiro post no ar. Tá no perfil.'),
 dict(nome='2026-11-12-1610', fundo='papel', tag='Regra minha', titulo='O braçal fica com a IA. <em>A decisão, comigo.</em>', t=128),
 dict(nome='2026-11-13-1210', fundo='laranja', tag='Bastidor', titulo='30 pessoas novas por dia. <em>Nenhuma abordada por mim.</em>', t=118),
 dict(nome='2026-11-13-1950', fundo='navy', tag='Post novo', titulo='Meu time de IA <em>no Instagram.</em>', sub='Quem acha o cliente, quem vai atrás e quem posta. Tá no perfil.', t=130),
 dict(nome='2026-11-14-1510', fundo='papel', tag='Pensa nisso', titulo='Achar o cliente certo vale mais que <em>falar com todo mundo.</em>', t=112),
 dict(nome='2026-11-15-1210', fundo='navy', tag='Post novo', titulo='Site no ar em <em>15 minutos.</em>', sub='Barbearia, advocacia e consultório na Alemanha. Tá no perfil.', t=140),
 dict(nome='2026-11-15-1710', fundo='laranja', tag='Regra minha', titulo='Site bonito sem oferta boa é <em>vitrine vazia.</em>', t=124),
]
out='/home/claude/insta-pessoal/personagem/saida/stories'; os.makedirs(out,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for s in L:
        f=f'{out}/_{s["nome"]}.html'; open(f,'w',encoding='utf-8').write(html(s))
        pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}/{s["nome"]}.png')
    b.close()
print('ok')
