import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

OUT = RAIZ + '/saida/bbr-r03-barb-tour'; FR = f'{OUT}/quadros'
shutil.rmtree(FR, ignore_errors=True); os.makedirs(FR)
k = [0]
def foto(pg):
    k[0] += 1; f = f'{FR}/{k[0]:04d}.jpg'; pg.screenshot(path=f, type='jpeg', quality=90); return f
def pan(pg, y1, n):
    y0 = pg.evaluate('scrollY'); fs = []
    for i in range(1, n + 1):
        u = i / n; u = u * u * (3 - 2 * u)
        pg.evaluate(f'window.scrollTo(0,{y0 + (y1 - y0) * u})'); pg.wait_for_timeout(15); fs.append(foto(pg))
    return fs
def alvo_y(pg, sel, folga=0):
    return pg.evaluate(f"""() => {{ const el=document.querySelector('{sel}'); const h=document.querySelector('header');
      return el.getBoundingClientRect().top+scrollY-(h?h.offsetHeight:0)-{folga}; }}""")

s = C.servidor()
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg = C.abrir(ctx, 'modelos/barb-anon/index.html'); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, alvo_y(pg, '#clube'), 60)
    cl = pan(pg, alvo_y(pg, '#clube') + 260, 50)
    p2 = pan(pg, alvo_y(pg, '#servicos'), 45)
    sv = [foto(pg)]
    p3 = pan(pg, alvo_y(pg, '#antes-depois') + 120, 45)
    # arrasta o primeiro antes e depois: 50 -> 18 -> 85 -> 50
    caixa = pg.evaluate("() => { const r=document.querySelector('.ba-split').getBoundingClientRect(); return [r.left,r.top,r.width,r.height]; }")
    vals = []
    for a, z, n in ((50, 18, 30), (18, 85, 45), (85, 50, 30)):
        for i in range(1, n + 1):
            u = i / n; u = u * u * (3 - 2 * u); vals.append(a + (z - a) * u)
    ad, pts = [], []
    for v in vals:
        pg.evaluate(f"() => {{ const r=document.querySelector('#ba1'); r.value={v}; r.dispatchEvent(new Event('input',{{bubbles:true}})); }}")
        ad.append(foto(pg))
        pts.append(((caixa[0] + caixa[2] * v / 100) * 2, (caixa[1] + caixa[3] / 2) * 2))
    b.close()
s.shutdown()

R = Reel(OUT, 20.0)
renderizar_html([
    ('f1', html_fundo('Barbeiro, olha o site que a sua barbearia <em>pode ter.</em>', 'Barbearia'), False),
    ('f2', html_fundo('Clube de assinatura e tabela <em>com preço de tudo.</em>', 'Barbearia'), False),
    ('f3', html_fundo('Antes e depois que o cliente <em>arrasta com o dedo.</em>', 'Barbearia'), False),
    ('f4', html_fundo('Sua barbearia com site novo <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 399', 'preço fechado', ['Você só paga depois de aprovar.', 'Agendar pelo WhatsApp ou pelo seu app.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 4.0, f'{OUT}/f1.png'), (4.0, 9.8, f'{OUT}/f2.png'), (9.8, 15.0, f'{OUT}/f3.png'), (15.0, 20.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.8, capa), (1.8, 4.0, p1), (4.0, 6.4, cl), (6.4, 7.9, p2), (7.9, 9.8, sv), (9.8, 11.3, p3),
           (11.3, 15.0, ad), (15.0, 20.0, capa)]
R.arrastes = [(11.3, 15.0, pts)]
R.camadas = [(15.3, 20.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-barbearia.mp4')
