import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

OUT = RAIZ + '/saida/r02-adv-guia'; FR = f'{OUT}/quadros'
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
def centro(pg, loc):
    b = loc.bounding_box(); return ((b['x'] + b['width'] / 2) * 2, (b['y'] + b['height'] / 2) * 2)

s = C.servidor()
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg = C.abrir(ctx, 'modelos/advocacia/1/index.html'); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, alvo_y(pg, '#triagem'), 60)
    g1 = [foto(pg)]
    ch1 = pg.locator('#chips1 button, #chips1 .chip').first; t1 = centro(pg, ch1); ch1.click(); pg.wait_for_timeout(500)
    pg.evaluate(f"window.scrollTo(0,{alvo_y(pg, '#tri', 12)})"); pg.wait_for_timeout(300)
    g2 = [foto(pg)]
    ch2 = pg.locator('#chips2 button, #chips2 .chip').first; t2 = centro(pg, ch2); ch2.click(); pg.wait_for_timeout(700)
    pg.evaluate(f"window.scrollTo(0,{alvo_y(pg, '#tri', 12)})"); pg.wait_for_timeout(300)
    g3 = [foto(pg)]
    btn = pg.locator('#rBtn')
    yb = pg.evaluate("() => { const b=document.querySelector('#rBtn').getBoundingClientRect(); return b.top+scrollY - innerHeight + b.height + 120; }")
    p2 = pan(pg, yb, 50)
    g4 = [foto(pg)]; t3 = centro(pg, btn)
    p3 = pan(pg, alvo_y(pg, '#areas'), 45)
    ar = [foto(pg)]
    b.close()
s.shutdown()

R = Reel(OUT, 21.0)
renderizar_html([
    ('f1', html_fundo('Advogado, olha o site que o seu cliente <em>vai ver.</em>', 'Advocacia'), False),
    ('f2', html_fundo('O cliente escolhe o assunto <em>em três cliques.</em>', 'Guia por assunto'), False),
    ('f3', html_fundo('E chega no seu WhatsApp <em>sabendo com quem falar.</em>', 'Guia por assunto'), False),
    ('f4', html_fundo('Seu escritório com site novo <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 797', 'preço fechado', ['Você só paga depois de aprovar.', 'Dentro das regras da OAB.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 4.0, f'{OUT}/f1.png'), (4.0, 9.2, f'{OUT}/f2.png'), (9.2, 16.0, f'{OUT}/f3.png'), (16.0, 21.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.6, capa), (1.6, 4.0, p1), (4.0, 5.6, g1), (5.6, 7.6, g2), (7.6, 9.2, g3), (9.2, 11.4, p2),
           (11.4, 13.4, g4), (13.4, 15.0, p3), (15.0, 16.0, ar), (16.0, 21.0, capa)]
R.toques = [(5.2, *t1), (7.2, *t2), (12.6, *t3)]
R.camadas = [(16.3, 21.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-advocacia.mp4')
