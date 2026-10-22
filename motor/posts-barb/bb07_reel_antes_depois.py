import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

# Carro-chefe da conta de barbearia: o antes e depois que o cliente arrasta com o dedo.
OUT = RAIZ + '/saida/bb07-reel-antes-depois'; FR = f'{OUT}/quadros'
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
def card_y(pg, i):
    return pg.evaluate(f"""() => {{ const el=document.querySelectorAll('.ba-card')[{i}]; const h=document.querySelector('header');
      return el.getBoundingClientRect().top+scrollY-(h?h.offsetHeight:0)-70; }}""")
def arrastar(pg, i, trechos):
    caixa = pg.evaluate(f"() => {{ const r=document.querySelectorAll('.ba-split')[{i}].getBoundingClientRect(); return [r.left,r.top,r.width,r.height]; }}")
    vals = []
    for a, z, n in trechos:
        for j in range(1, n + 1):
            u = j / n; u = u * u * (3 - 2 * u); vals.append(a + (z - a) * u)
    fs, pts = [], []
    for v in vals:
        pg.evaluate(f"() => {{ const r=document.querySelector('#ba{i + 1}'); r.value={v}; r.dispatchEvent(new Event('input',{{bubbles:true}})); }}")
        fs.append(foto(pg))
        pts.append(((caixa[0] + caixa[2] * v / 100) * 2, (caixa[1] + caixa[3] / 2) * 2))
    return fs, pts

s = C.servidor()
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg = C.abrir(ctx, 'modelos/barb-anon/index.html'); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, card_y(pg, 0), 54)
    a1, t1 = arrastar(pg, 0, ((50, 14, 34), (14, 88, 46), (88, 50, 28)))
    p2 = pan(pg, card_y(pg, 1), 36)
    a2, t2 = arrastar(pg, 1, ((50, 12, 30), (12, 86, 40), (86, 50, 26)))
    p3 = pan(pg, card_y(pg, 2), 36)
    a3, t3 = arrastar(pg, 2, ((50, 16, 28), (16, 84, 36), (84, 50, 26)))
    b.close()
s.shutdown()

R = Reel(OUT, 20.0)
renderizar_html([
    ('f1', html_fundo('Barbeiro, o seu corte <em>vende sozinho.</em>', 'Barbearia'), False),
    ('f2', html_fundo('O cliente arrasta <em>e vê a diferença.</em>', 'Antes e depois'), False),
    ('f3', html_fundo('Degradê, barba, cacheado. <em>Cada corte com o seu.</em>', 'Antes e depois'), False),
    ('f4', html_fundo('Antes e depois no site da sua barbearia, <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 399', 'preço fechado', ['Menos que 5 cortes.', 'Você só paga depois de aprovar.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 3.4, f'{OUT}/f1.png'), (3.4, 11.4, f'{OUT}/f2.png'), (11.4, 15.6, f'{OUT}/f3.png'), (15.6, 20.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.6, capa), (1.6, 3.4, p1), (3.4, 7.0, a1), (7.0, 8.2, p2), (8.2, 11.4, a2), (11.4, 12.6, p3), (12.6, 15.6, a3), (15.6, 20.0, capa)]
R.arrastes = [(3.4, 7.0, t1), (8.2, 11.4, t2), (12.6, 15.6, t3)]
R.camadas = [(15.9, 20.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-antes-depois.mp4')
