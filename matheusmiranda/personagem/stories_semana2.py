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
 dict(nome='2026-11-23-1240', fundo='navy', tag='Post novo', titulo='Paguei R$ 174 pra Meta. <em>Recebi zero conversa.</em>', sub='A IA achou pra onde foi o dinheiro. Tá no perfil.', t=118),
 dict(nome='2026-11-25-1240', fundo='laranja', tag='Post novo', titulo='Uma pergunta no lugar errado <em>travava meu cadastro.</em>', sub='Mudei de lugar e virou outro jogo. Tá no perfil.', t=112),
 dict(nome='2026-11-27-1240', fundo='navy', tag='Post novo', titulo='Meu anúncio aparece <em>dentro do ChatGPT.</em>', sub='Quanto custa e o que aprendi. Tá no perfil.', t=124),
 dict(nome='2026-11-28-1240', fundo='papel', tag='Post novo', titulo='Um canal de receita <em>sem câmera.</em>', sub='Sem cozinha e sem cozinheiro. Tá no perfil.', t=130),
]
out='/home/claude/insta-pessoal/personagem/saida/stories-semana2'; os.makedirs(out,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for s in L:
        f=f'{out}/_{s["nome"]}.html'; open(f,'w',encoding='utf-8').write(html(s))
        pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}/{s["nome"]}.png')
    b.close()
print('ok')
