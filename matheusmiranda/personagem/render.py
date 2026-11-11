import sys, os, importlib.util
from playwright.sync_api import sync_playwright
BASE = os.path.dirname(os.path.abspath(__file__))
F = 'file:///home/claude/insta-pessoal/motor/fontes'
COR = dict(papel='#FCF4E1', navy='#1E2B4A', laranja='#E2492F', amarelo='#F2C94C', tinta='#2B2B2B')
CSS = f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:{COR['papel']};color:{COR['navy']};font-family:I;position:relative}}
body.navy{{background:{COR['navy']};color:{COR['papel']}}}
body.laranja{{background:{COR['laranja']};color:{COR['papel']}}}
.il{{position:absolute;inset:33px;border-radius:4px;background-size:cover;background-position:center bottom}}
.txt{{position:absolute;left:90px;right:90px;top:110px;z-index:2}}
.gigante .txt{{top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}}
.tag{{display:inline-block;font-family:M;font-weight:600;font-size:24px;letter-spacing:.08em;text-transform:uppercase;background:{COR['amarelo']};color:{COR['navy']};padding:10px 18px;border:3px solid {COR['navy']};transform:rotate(-2deg);margin-bottom:30px}}
h1{{font-family:B;font-weight:800;font-stretch:85%;letter-spacing:-.035em;line-height:.98;font-size:var(--t,92px)}}
h1 em{{font-style:normal;color:{COR['laranja']}}}
.navy h1 em{{color:{COR['amarelo']}}} .laranja h1 em{{color:{COR['navy']}}}
.sub{{font-size:var(--s,44px);line-height:1.3;margin-top:26px;max-width:880px;opacity:.85}}
.painel{{position:absolute;inset:30px;border:6px solid {COR['navy']};border-radius:6px;z-index:3;pointer-events:none}}
.navy .painel{{border-color:{COR['papel']}}} .laranja .painel{{border-color:{COR['navy']}}}
.pe{{position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-family:M;font-size:22px;letter-spacing:.05em;z-index:2}}
.il-card .pe{{display:none}}
.pts{{display:flex;gap:10px}} .pts i{{width:12px;height:12px;border-radius:50%;border:2px solid currentColor}} .pts i.on{{background:currentColor}}
"""
def pagina(c, i, n):
    cls = c.get('fundo', 'papel') + (' gigante' if not c.get('il') else ' il-card')
    il = f'<div class="il" style="background-image:url(file://{BASE}/{c["il"]})"></div>' if c.get('il') else ''
    st = (f'--t:{c["t"]}px;' if c.get('t') else '') + (f'--s:{c["s"]}px;' if c.get('s') else '')
    tag = f'<div><span class="tag">{c["tag"]}</span></div>' if c.get('tag') else ''
    sub = f'<p class="sub">{c["sub"]}</p>' if c.get('sub') else ''
    pts = ''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1, n+1))
    pe = f'<div class="pe"><span>@matheusmiranda.ia</span><span class="pts">{pts}</span></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}" style="{st}">{il}<div class="painel"></div><div class="txt">{tag}<h1>{c["titulo"]}</h1>{sub}</div>{pe}</body></html>'
def render(spec):
    s = importlib.util.spec_from_file_location('s', spec); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    out = f'{BASE}/saida/{m.SLUG}'; os.makedirs(out, exist_ok=True); n = len(m.CARDS)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350})
        for i, c in enumerate(m.CARDS, 1):
            f = f'{out}/_c{i}.html'; open(f,'w',encoding='utf-8').write(pagina(c,i,n))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}/{i:02d}.png')
        b.close()
    print('ok', out)
if __name__ == '__main__': render(sys.argv[1])
