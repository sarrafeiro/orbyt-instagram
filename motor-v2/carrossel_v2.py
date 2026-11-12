# Motor de carrossel v2 (generico): texto centralizado em piramide, pouco texto por card, uma cor de destaque.
# Uso: MARCA_JSON=/caminho/marca.json python3 carrossel_v2.py spec.py  (sai em ./saida/<SLUG>/01.png...)
# marca.json: {"nome":"Fulano","sobrenome":"Silva","cores":{"escuro":"#..","papel":"#..","destaque":"#.."}}
import sys, os, importlib.util, html as H
from playwright.sync_api import sync_playwright
import json
AQUI=os.path.dirname(os.path.abspath(__file__))
F='file://'+AQUI+'/fontes'
MARCA=json.load(open(os.environ.get('MARCA_JSON', AQUI+'/exemplo/marca.json')))
C=dict(escuro=MARCA['cores']['escuro'], papel=MARCA['cores']['papel'], branco='#FFFFFF', azul=MARCA['cores']['escuro'], coral=MARCA['cores']['destaque'], cinza='#6B7078')
GRAD=C["coral"]
CSS=f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:{C['papel']};color:{C['escuro']};font-family:I;position:relative}}
body.escuro{{background:{C['escuro']};color:#F3F1EC}}
.grao{{position:absolute;inset:0;opacity:.35;mix-blend-mode:multiply;pointer-events:none}}
.escuro .grao,.laranja .grao{{opacity:.10;mix-blend-mode:screen}}
.fita{{position:absolute;top:0;height:1350px;pointer-events:none}}
.topo{{position:absolute;top:200px;left:0;right:0;text-align:center;font-family:B;font-weight:700;font-size:28px;letter-spacing:-.01em;z-index:3}}
.topo span{{font-weight:400;opacity:.6}}
.miolo{{position:absolute;left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;z-index:2;gap:34px}}
h1{{font-family:B;font-weight:400;font-stretch:90%;letter-spacing:-.03em;line-height:1.04;font-size:var(--t,104px);text-wrap:balance}}
h1 b,.num{{font-weight:800;color:{C['coral']}}}
.laranja{{background:{C['coral']};color:#fff}} .laranja h1 b,.laranja .num{{color:{C['escuro']}}} .laranja .pilula{{background:{C['escuro']}}}
.fluxo{{display:flex;flex-direction:column;align-items:center;gap:10px}} .fluxo span{{font-family:B;font-weight:700;font-size:38px;padding:18px 30px;border-radius:20px;background:#fff;color:{C['escuro']};box-shadow:0 14px 40px rgba(30,43,74,.12)}} .fluxo em{{font-style:normal;font-size:44px;color:{C['coral']};font-weight:800}}
.escuro .fluxo span{{background:#2A3960;color:#fff;box-shadow:none}}
.pre{{font-family:B;font-weight:500;font-size:46px;letter-spacing:-.02em;opacity:.75;text-wrap:balance}}
.num{{font-family:B;font-stretch:85%;font-size:var(--n,300px);line-height:.9;letter-spacing:-.05em}}
.pilula{{display:inline-block;font-family:I;font-weight:600;font-size:34px;padding:14px 30px;border-radius:999px;background:{C['coral']};color:#fff;text-wrap:balance;max-width:820px}}
.sub{{font-size:38px;line-height:1.35;opacity:.7;max-width:780px;text-wrap:balance}}
.pe{{position:absolute;bottom:180px;left:0;right:0;display:flex;justify-content:center;gap:12px;z-index:3}}
.pe i{{width:12px;height:12px;border-radius:50%;background:currentColor;opacity:.25}} .pe i.on{{opacity:1;width:36px;border-radius:6px}}
.busca{{background:#fff;color:#111;border-radius:28px;box-shadow:0 30px 80px rgba(0,0,0,.12);width:820px;padding:30px;text-align:left}}
.busca .campo{{border:2px solid #E3E5E8;border-radius:999px;padding:18px 28px;font-size:34px;margin-bottom:18px}}
.busca .res{{display:flex;gap:18px;align-items:center;padding:18px 20px;border-radius:18px;font-size:30px}}
.busca .res.bom{{background:#EEF2FF}} .busca .res i{{font-style:normal;font-weight:700;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;color:#fff;flex:none}}
.busca .bom i{{background:{C['azul']}}} .busca .ruim i{{background:{C['coral']}}} .busca .ruim{{opacity:.6}}
"""
GRAO='<svg class="grao" width="1080" height="1350"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .55 0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>'
def fita(i, n):
    # arcos que atravessam a emenda entre dois cards (estilo Onside): capa->2 por baixo, penultimo->final por cima
    W=1080*n; d=''
    for k,(lado) in [(1,'baixo'),(n-1,'cima')]:
        x=k*1080
        if lado=='baixo': d+=f"M {x-760} 1500 C {x-520} 1020 {x-180} 1010 {x} 1040 C {x+200} 1070 {x+520} 1100 {x+760} 1500 "
        else: d+=f"M {x-760} -150 C {x-520} 330 {x-180} 340 {x} 310 C {x+200} 280 {x+520} 250 {x+760} -150 "
    return f'<svg class="fita" style="left:{-i*1080}px;width:{W}px" viewBox="0 0 {W} 1350"><defs><linearGradient id="fg" gradientUnits="userSpaceOnUse" x1="0" x2="{W}" y1="0" y2="0"><stop offset="0" stop-color="{C["azul"]}"/><stop offset=".5" stop-color="#8B5CF6"/><stop offset="1" stop-color="{C["coral"]}"/></linearGradient></defs><path d="{d}" fill="none" stroke="url(#fg)" stroke-width="120" stroke-linecap="round"/></svg>'
def fluxo(itens):
    return '<div class="fluxo">'+'<em>↓</em>'.join(f'<span>{H.escape(t)}</span>' for t in itens)+'</div>'
def busca(q, res):
    r=''.join(f'<div class="res {c}"><i>{"✓" if c=="bom" else "✕"}</i><div>{H.escape(t)}</div></div>' for c,t in res)
    return f'<div class="busca"><div class="campo">🔍 {H.escape(q)}</div>{r}</div>'
def pagina(c, i, n, comfita):
    st=''.join(f'--{k}:{c[k]}px;' for k in ('t','n') if c.get(k))
    partes=[]
    if c.get('pre'): partes.append(f'<p class="pre">{c["pre"]}</p>')
    if c.get('titulo'): partes.append(f'<h1>{c["titulo"]}</h1>')
    if c.get('num'): partes.append(f'<div class="num">{c["num"]}</div>')
    if c.get('visual'): partes.append(c['visual'])
    if c.get('sub'): partes.append(f'<p class="sub">{c["sub"]}</p>')
    if c.get('pilula'): partes.append(f'<span class="pilula">{c["pilula"]}</span>')
    pts=''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1,n+1))
    f=''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{ {"destaque":"laranja"}.get(c.get("fundo","papel"), c.get("fundo","papel")) }" style="{st}">{GRAO}{f}<div class="topo">{MARCA["nome"]} <span>{MARCA.get("sobrenome","")}</span></div><div class="miolo">{"".join(partes)}</div><div class="pe">{pts}</div></body></html>'
def render(spec):
    s=importlib.util.spec_from_file_location('s',spec); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    out=os.path.join(os.getcwd(),'saida',m.SLUG); os.makedirs(out,exist_ok=True); n=len(m.CARDS)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for i,c in enumerate(m.CARDS,1):
            f=f'{out}/_c{i}.html'; open(f,'w',encoding='utf-8').write(pagina(c,i,n,getattr(m,'FITA',True)))
            pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}/{i:02d}.png')
        b.close()
    print('ok',out)
if __name__=='__main__': render(sys.argv[1])
