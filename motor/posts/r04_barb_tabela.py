import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, shutil; sys.path.insert(0, RAIZ)
import capturar as C
from reel import Reel, html_fundo, html_fim, renderizar_html
from playwright.sync_api import sync_playwright

OUT = RAIZ + '/saida/r04-barb-tabela'; FR = f'{OUT}/quadros'
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
def pan_lista(pg, y1, n):
    y0 = pg.evaluate("document.querySelector('#tabelaLista').scrollTop"); fs = []
    for i in range(1, n + 1):
        u = i / n; u = u * u * (3 - 2 * u)
        pg.evaluate(f"document.querySelector('#tabelaLista').scrollTop={y0 + (y1 - y0) * u}"); pg.wait_for_timeout(15); fs.append(foto(pg))
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
    pg = C.abrir(ctx, 'modelos/barb-anon/index.html')
    pg.evaluate("document.documentElement.style.scrollBehavior='auto'"); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
    capa = [foto(pg)]
    p1 = pan(pg, alvo_y(pg, '#servicos'), 60)
    sv = [foto(pg)]
    yb = pg.evaluate("() => { const b=document.querySelector('#abrirTabela').getBoundingClientRect(); return b.top+scrollY - innerHeight + b.height + 140; }")
    p2 = pan(pg, yb, 45)
    sv2 = [foto(pg)]
    btn = pg.locator('#abrirTabela'); t1 = centro(pg, btn); btn.click(); pg.wait_for_timeout(900)
    tb = [foto(pg)]
    p3 = pan_lista(pg, 1400, 70)
    p4 = pan_lista(pg, 0, 30)
    ch = pg.locator('#chips button, #chips .chip').nth(2); t2 = centro(pg, ch); ch.click(); pg.wait_for_timeout(700)
    ba = [foto(pg)]
    b.close()
s.shutdown()

R = Reel(OUT, 22.0)
renderizar_html([
    ('f1', html_fundo('Barbeiro, seu cliente quer saber o preço <em>antes de ir.</em>', 'Barbearia', t=82), False),
    ('f2', html_fundo('Os mais pedidos, <em>com preço, logo de cara.</em>', 'Serviços'), False),
    ('f3', html_fundo('Um toque e abre a tabela <em>com os 38 serviços.</em>', 'Tabela completa'), False),
    ('f4', html_fundo('Ele filtra por barba, corte ou combo <em>e toca em Agendar.</em>', 'Tabela completa', t=80), False),
    ('f5', html_fundo('Sua barbearia com site novo <em>em 2 dias úteis.</em>', 'Orbyt Studio'), False),
    ('camada-fim', html_fim('R$ 797', 'preço fechado', ['Você só paga depois de aprovar.', 'Agendar pelo WhatsApp ou pelo seu app.', '<b>Link no perfil.</b>']), True),
], OUT)
R.fundos = [(0, 3.6, f'{OUT}/f1.png'), (3.6, 8.0, f'{OUT}/f2.png'), (8.0, 13.6, f'{OUT}/f3.png'), (13.6, 17.0, f'{OUT}/f4.png'), (17.0, 22.0, f'{OUT}/f5.png')]
R.telas = [(0, 1.6, capa), (1.6, 3.6, p1), (3.6, 5.4, sv), (5.4, 7.0, p2), (7.0, 8.6, sv2), (8.6, 9.6, tb), (9.6, 12.6, p3), (12.6, 13.6, p4),
           (13.6, 14.6, p4[-1:]), (14.6, 17.0, ba), (17.0, 22.0, capa)]
R.toques = [(8.2, *t1), (14.3, *t2)]
R.camadas = [(17.3, 22.0, f'{OUT}/camada-fim.png')]
R.gravar(f'{OUT}/reel-barbearia-tabela.mp4')
