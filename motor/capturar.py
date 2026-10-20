"""Tira prints dos modelos de site (pasta www) com as letras locais.
Uso: python3 capturar.py [adv1 adv2 barb]  -> grava em motor/prints/
"""
import http.server, socketserver, threading, functools, os, sys, time
from playwright.sync_api import sync_playwright

WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prints')
PORT = 8765
os.makedirs(OUT, exist_ok=True)

FONTS_CSS = open(f'{WWW}/fonts/fonts.css', encoding='utf-8').read().replace('url(/fonts/', f'url(http://localhost:{PORT}/fonts/')

def servidor():
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k): pass
    h = functools.partial(Q, directory=WWW)
    socketserver.TCPServer.allow_reuse_address = True
    s = socketserver.TCPServer(('127.0.0.1', PORT), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s

LIMPA = """
() => {
  document.getElementById('orbyt-barra-css')?.remove();
  document.querySelectorAll('.orbyt-barra,.orbyt-troca,#cookie,.cookie,.guide-bar').forEach(e=>e.remove());
  document.body.classList.remove('guide');
  document.documentElement.classList.add('js');
  document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));
  window.dispatchEvent(new Event('resize'));
}
"""

def rota(route):
    u = route.request.url
    if 'fonts.googleapis.com' in u:
        return route.fulfill(status=200, content_type='text/css', body=FONTS_CSS)
    if u.startswith(f'http://localhost:{PORT}') or u.startswith('data:') or u.startswith('blob:'):
        return route.continue_()
    return route.abort()

def abrir(ctx, caminho, antes=None):
    pg = ctx.new_page()
    pg.route('**/*', rota)
    pg.goto(f'http://localhost:{PORT}/{caminho}', wait_until='networkidle')
    if antes:
        pg.evaluate(antes)
    pg.evaluate(LIMPA)
    pg.evaluate('document.fonts.ready')
    pg.wait_for_timeout(600)
    return pg

def ate(pg, seletor, folga=0):
    pg.evaluate(f"""() => {{ const el=document.querySelector('{seletor}'); if(!el) return;
      const h=document.querySelector('header'); const t=el.getBoundingClientRect().top+scrollY-(h?h.offsetHeight:0)-{folga};
      window.scrollTo(0,t); }}""")
    pg.wait_for_timeout(500)

def shot(pg, nome):
    pg.screenshot(path=f'{OUT}/{nome}.png')
    print('ok', nome)

def advocacia(b, n):
    base = f'modelos/advocacia/{n}/index.html'
    for vista, vp, esc in (('cel', {'width': 390, 'height': 844}, 2), ('desk', {'width': 1440, 'height': 900}, 1)):
        ctx = b.new_context(viewport=vp, device_scale_factor=esc, is_mobile=(vista == 'cel'), has_touch=(vista == 'cel'))
        pg = abrir(ctx, base)
        pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
        shot(pg, f'adv{n}-{vista}-capa')
        ate(pg, '#triagem'); shot(pg, f'adv{n}-{vista}-guia1')
        try:
            pg.locator('#chips1 button, #chips1 .chip').first.click(); pg.wait_for_timeout(500)
            ate(pg, '#tri', 12); shot(pg, f'adv{n}-{vista}-guia2')
            pg.locator('#chips2 button, #chips2 .chip').first.click(); pg.wait_for_timeout(700)
            ate(pg, '#tri', 12); shot(pg, f'adv{n}-{vista}-guia3')
        except Exception as e:
            print('guia falhou', n, vista, str(e)[:120])
        for sec in ('areas', 'equipe', 'contato'):
            ate(pg, f'#{sec}'); shot(pg, f'adv{n}-{vista}-{sec}')
        ctx.close()

def barbearia(b):
    base = 'modelos/barb-anon/index.html'
    for vista, vp, esc in (('cel', {'width': 390, 'height': 844}, 2), ('desk', {'width': 1440, 'height': 900}, 1)):
        ctx = b.new_context(viewport=vp, device_scale_factor=esc, is_mobile=(vista == 'cel'), has_touch=(vista == 'cel'))
        pg = abrir(ctx, base)
        pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300)
        shot(pg, f'barb-{vista}-capa')
        for sec in ('clube', 'servicos', 'antes-depois', 'local', 'duvidas'):
            ate(pg, f'#{sec}'); shot(pg, f'barb-{vista}-{sec}')
        ctx.close()

if __name__ == '__main__':
    s = servidor()
    with sync_playwright() as p:
        b = p.chromium.launch()
        alvo = sys.argv[1:] or ['adv1']
        if 'adv1' in alvo: advocacia(b, 1)
        if 'adv2' in alvo: advocacia(b, 2)
        if 'barb' in alvo: barbearia(b)
        b.close()
    s.shutdown()
