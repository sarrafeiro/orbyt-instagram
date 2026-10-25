import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

# Carro-chefe: o cliente arrasta o antes e depois e toca em Agendar (semana de 26/10/2026).
OUT = RAIZ + '/saida/bb11-reel-agendar'; FR = f'{OUT}/quadros'
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

def agendar_xy(pg):
    return pg.evaluate("""() => { const h=document.querySelector('header'); const els=[...h.querySelectorAll('a,button')].filter(e=>e.textContent.trim().toLowerCase().startsWith('agendar'));
      const r=els[0].getBoundingClientRect(); return [(r.left+r.width/2)*2,(r.top+r.height/2)*2]; }""")

s = C.servidor()
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg = C.abrir(ctx, 'modelos/barb-anon/index.html'); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, card_y(pg, 0), 48)
    a1, t1 = arrastar(pg, 0, ((50, 10, 30), (10, 90, 44), (90, 50, 24)))
    p2 = pan(pg, card_y(pg, 1), 30)
    a2, t2 = arrastar(pg, 1, ((50, 12, 28), (12, 88, 38), (88, 50, 22)))
    parado = [foto(pg)]
    ax, ay = agendar_xy(pg)
    b.close()
s.shutdown()

R = Reel(OUT, 20.0)
renderizar_html([
    ('f1', html_fundo('Foto parada não mostra <em>o seu degradê.</em>', 'Barbearia'), False),
    ('f2', html_fundo('O cliente arrasta <em>e vê o antes e depois.</em>', 'Antes e depois'), False),
    ('f3', html_fundo('Gostou do corte? <em>Toca em Agendar.</em>', 'Antes e depois'), False),
    ('f4', html_fundo('O seu trabalho convence <em>melhor que qualquer texto.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 399', 'preço fechado', ['Menos que 5 cortes.', 'Você só paga depois de aprovar.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 3.0, f'{OUT}/f1.png'), (3.0, 11.0, f'{OUT}/f2.png'), (11.0, 15.0, f'{OUT}/f3.png'), (15.0, 20.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.4, capa), (1.4, 3.0, p1), (3.0, 7.0, a1), (7.0, 8.2, p2), (8.2, 11.0, a2), (11.0, 15.0, parado), (15.0, 20.0, capa)]
R.arrastes = [(3.0, 7.0, t1), (8.2, 11.0, t2)]
R.toques = [(13.2, ax, ay)]
R.camadas = [(15.4, 20.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-agendar.mp4')
