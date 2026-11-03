"""Stories do NuPrato (1080x1920). Mesma marca do carrossel (cores, letras, logo, selo).
Uso num script:  from story import render;  render(LISTA, pasta)
Campos de cada story (dict):
  nome    nome do arquivo (s01-seg-frase-...)
  tema    'verde' | 'escuro' | 'creme' | 'papel'
  olho    linha pequena acima do título
  titulo  HTML; <em> vira marca-texto amarelo
  sub     apoio curto (até 25 palavras)
  nota    anotação à mão (Caveat)
  capa    caminho absoluto da capa (01.jpg/01.png) do post que o story anuncia
  visual  HTML de um helper do carrossel (ficha, conversa, busca, numero, lista)
  selo    True = selo dourado "Nu, que prato!" (só em story de oferta ou receita que deu certo)
  pe      texto da pílula de baixo (ex.: 'post novo no perfil', 'link na bio')
  t, s    tamanho do título e do sub
Texto fica a pelo menos 250 px do topo e da base (área segura do story).
"""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, BASE)
import carrossel as K

C = K.C; M = K.M
CSS_STORY = K.CSS.replace('html,body{width:1080px;height:1350px;overflow:hidden}', 'html,body{width:1080px;height:1920px;overflow:hidden}') + f"""
.stopo{{position:absolute;left:0;right:0;top:230px;display:flex;justify-content:center;align-items:center;gap:12px;font-weight:700;font-size:36px;letter-spacing:-.02em;z-index:3}}
.sbloco{{position:absolute;left:90px;right:90px;top:360px;bottom:380px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;z-index:2}}
.sbloco h1{{font-size:var(--t,104px)}}
.sbloco .sub{{font-size:var(--s,44px)}}
.scapa{{margin-top:56px;width:640px;transform:rotate(-2deg);border-radius:10px;overflow:hidden;box-shadow:0 40px 70px -30px rgba(30,40,32,.55),0 0 0 10px {C['papel']}}}
.scapa img{{width:100%;display:block}}
.sselo{{width:420px;height:420px;margin-bottom:40px;transform:rotate(-8deg);filter:drop-shadow(0 22px 26px rgba(20,40,28,.35))}}
.svisual{{margin-top:50px;width:100%;display:flex;justify-content:center}}
.spe{{position:absolute;left:0;right:0;bottom:250px;display:flex;justify-content:center;z-index:3}}
.spe span{{background:{C['grafite']};color:{C['creme']};border-radius:999px;padding:18px 36px;font-weight:700;font-size:30px}}
.verde .spe span,.escuro .spe span{{background:{C['creme']};color:{C['grafite']}}}
body.papel.story:before{{left:70px}}
"""
GRAO = K.GRAO.replace('viewBox="0 0 1080 1350"', 'viewBox="0 0 1080 1920"').replace('height="1350"', 'height="1920"')

def pagina(s):
    tema = s.get('tema', 'creme'); T = K.TEMAS[tema]
    var = ';'.join(f'--{k}:{v}' for k, v in T.items() if k in ('bg', 'fg', 'sec', 'olho', 'mao'))
    if s.get('t'): var += f';--t:{s["t"]}px'
    if s.get('s'): var += f';--s:{s["s"]}px'
    bglogo = C['papel'] if tema == 'papel' else T['bg']
    c = f'<div class="stopo">{K.logo(T["logo_fg"], bglogo, 62)}<span>{M["nome"]}</span></div><div class="sbloco">'
    if s.get('selo'): c += f'<img class="sselo" src="{K.SELO}" alt="">'
    if s.get('olho'): c += f'<div class="olho">{s["olho"]}</div>'
    c += f'<h1>{s["titulo"]}</h1>'
    if s.get('sub'): c += f'<p class="sub">{s["sub"]}</p>'
    if s.get('nota'): c += f'<div class="mao">{s["nota"]}</div>'
    if s.get('capa'): c += f'<div class="scapa"><img src="file://{s["capa"]}"></div>'
    if s.get('visual'): c += f'<div class="svisual">{s["visual"]}</div>'
    c += '</div>'
    if s.get('pe'): c += f'<div class="spe"><span>{s["pe"]}</span></div>'
    grao = GRAO if tema in ('verde', 'escuro') else ''
    return (f'<!doctype html><html class="story"><head><meta charset="utf-8"><style>{CSS_STORY}</style></head>'
            f'<body class="{tema} story" style="{var}">{grao}{c}</body></html>')

def render(lista, pasta):
    os.makedirs(pasta, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        for s in lista:
            f = f'{pasta}/{s["nome"]}.html'; open(f, 'w', encoding='utf-8').write(pagina(s))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
            vaza = pg.evaluate('''() => { const m = document.querySelector('.sbloco'); return m.scrollHeight > m.clientHeight + 2 ? m.scrollHeight - m.clientHeight : 0 }''')
            if vaza: print(f'AVISO {s["nome"]}: passa {vaza}px da área segura')
            pg.screenshot(path=f'{pasta}/{s["nome"]}.png'); print('ok', s['nome'])
        b.close()
