# Capa de Reel: quadro do video + titulo em painel solido embaixo, dentro da area do grid 3:4 (y 240 a 1680).
# Uso: python3 capa_reel.py quadro.png "Titulo com <b>destaque</b>" saida.png
import sys
from playwright.sync_api import sync_playwright
import os
F="file://"+os.path.dirname(os.path.abspath(__file__))+"/fontes"
quadro, titulo, out = sys.argv[1], sys.argv[2], sys.argv[3]
html=f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{background:url(file://{quadro}) center/cover}}
.topo{{display:none}}
.base{{position:absolute;inset:auto 0 0 0;height:1000px;background:linear-gradient(rgba(30,43,74,0),#1E2B4A 34%)}}
h1{{position:absolute;left:90px;right:90px;top:1250px;text-align:center;font-family:B;font-weight:800;font-stretch:88%;letter-spacing:-.03em;line-height:1;font-size:118px;color:#fff;text-wrap:balance}}
h1 b{{color:#E2492F}}
</style></head><body><div class=topo></div><div class=base></div><h1>{titulo}</h1></body></html>"""
open('/tmp/capa_reel.html','w').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920}); pg.goto('file:///tmp/capa_reel.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=out); b.close()
