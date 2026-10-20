"""Prints extras da semana de 26/10: artigos (adv1), tabela de servicos aberta (barb), duvidas adv1."""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
import capturar as C
from playwright.sync_api import sync_playwright
s = C.servidor()
with sync_playwright() as p:
    b = p.chromium.launch()
    for vista, vp, esc in (('cel', {'width': 390, 'height': 844}, 2), ('desk', {'width': 1440, 'height': 900}, 1)):
        ctx = b.new_context(viewport=vp, device_scale_factor=esc, is_mobile=(vista == 'cel'), has_touch=(vista == 'cel'))
        pg = C.abrir(ctx, 'modelos/advocacia/1/index.html')
        pg.evaluate("document.documentElement.style.scrollBehavior='auto'"); pg.wait_for_timeout(300)
        C.ate(pg, '#conteudo'); pg.wait_for_timeout(900); C.ate(pg, '#conteudo'); pg.wait_for_timeout(600); C.shot(pg, f'adv1-{vista}-conteudo')
        C.ate(pg, '#duvidas'); pg.wait_for_timeout(900); C.ate(pg, '#duvidas'); pg.wait_for_timeout(600); C.shot(pg, f'adv1-{vista}-duvidas')
        pg = C.abrir(ctx, 'modelos/barb-anon/index.html')
        C.ate(pg, '#servicos'); pg.locator('#abrirTabela').click(); pg.wait_for_timeout(800)
        C.shot(pg, f'barb-{vista}-tabela')
        ctx.close()
    b.close()
s.shutdown()
