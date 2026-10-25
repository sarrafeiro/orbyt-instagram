import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

OUT = RAIZ + '/saida/r07-adv-conteudo'; FR = f'{OUT}/quadros'
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
    pg = C.abrir(ctx, 'modelos/advocacia/1/index.html'); pg.evaluate("document.documentElement.style.scrollBehavior='auto'"); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, alvo_y(pg, '#conteudo'), 60)
    c1 = [foto(pg)]
    p2 = pan(pg, alvo_y(pg, '#conteudo') + 420, 35)
    c2 = [foto(pg)]
    yd = pg.evaluate("() => document.querySelectorAll('#duvidas details')[0].getBoundingClientRect().top + scrollY - 260")
    p3 = pan(pg, yd, 45)
    d1 = [foto(pg)]
    sm = pg.locator('#duvidas summary').nth(2); t1 = centro(pg, sm); sm.click(); pg.wait_for_timeout(600)
    d2 = [foto(pg)]
    b.close()
s.shutdown()

R = Reel(OUT, 21.0)
renderizar_html([
    ('f1', html_fundo('Advogado, você está em audiência. <em>Quem responde o cliente?</em>', 'Advocacia', t=80), False),
    ('f2', html_fundo('Artigos que explicam <em>o direito dele.</em>', 'Conteúdo informativo'), False),
    ('f3', html_fundo('As dúvidas de sempre <em>respondidas no site.</em>', 'Dúvidas frequentes'), False),
    ('f4', html_fundo('Seu escritório com site novo <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 797', 'preço fechado', ['Você só paga depois de aprovar.', 'Seguindo o Provimento 205/2021.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 3.6, f'{OUT}/f1.png'), (3.6, 9.0, f'{OUT}/f2.png'), (9.0, 16.0, f'{OUT}/f3.png'), (16.0, 21.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.6, capa), (1.6, 3.8, p1), (3.8, 6.2, c1), (6.2, 7.4, p2), (7.4, 9.2, c2), (9.2, 10.8, p3),
           (10.8, 12.4, d1), (12.4, 16.0, d2), (16.0, 21.0, capa)]
R.toques = [(12.0, *t1)]
R.camadas = [(16.3, 21.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-adv-conteudo.mp4')
