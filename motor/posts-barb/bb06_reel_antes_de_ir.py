import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

OUT = RAIZ + '/saida/bb06-reel-antes-de-ir'; FR = f'{OUT}/quadros'
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
    p1 = pan(pg, alvo_y(pg, '#equipe'), 55)
    eq = pan(pg, alvo_y(pg, '#equipe') + 330, 60)
    p2 = pan(pg, alvo_y(pg, '#espaco'), 45)
    es = pan(pg, alvo_y(pg, '#espaco') + 380, 55)
    p3 = pan(pg, alvo_y(pg, '#avaliacoes'), 45)
    av = pan(pg, alvo_y(pg, '#avaliacoes') + 260, 50)
    p4 = pan(pg, alvo_y(pg, '#local'), 45)
    lc = [foto(pg)]
    b.close()
s.shutdown()

R = Reel(OUT, 20.0)
renderizar_html([
    ('f1', html_fundo('Barbeiro, o cliente novo quer ver tudo <em>antes de ir.</em>', 'Barbearia'), False),
    ('f2', html_fundo('Quem vai cortar. <em>E agendar direto com ele.</em>', 'Barbearia'), False),
    ('f3', html_fundo('O espaço, as avaliações <em>e como chegar.</em>', 'Barbearia'), False),
    ('f4', html_fundo('Tudo isso no site da sua barbearia, <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 797', 'preço fechado', ['Você só paga depois de aprovar.', 'Agendar pelo WhatsApp ou pelo seu app.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 3.8, f'{OUT}/f1.png'), (3.8, 7.6, f'{OUT}/f2.png'), (7.6, 15.6, f'{OUT}/f3.png'), (15.6, 20.0, f'{OUT}/f4.png')]
R.telas = [(0, 1.8, capa), (1.8, 3.8, p1), (3.8, 6.0, eq), (6.0, 7.6, p2), (7.6, 9.6, es), (9.6, 11.2, p3),
           (11.2, 13.0, av), (13.0, 14.6, p4), (14.6, 15.6, lc), (15.6, 20.0, capa)]
R.camadas = [(15.9, 20.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-antes-de-ir.mp4')
