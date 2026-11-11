"""Camada de marca do motor. Lê motor/marca.json e troca cores, letras, logo, nome e textos fixos.
Os motores (carrossel, story, reel) foram desenhados com os tokens da Orbyt; aqui cada valor vira o da marca.
Nunca mexa nas cores direto nos motores: mude o marca.json.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
_ARQ = os.environ.get('MARCA_JSON', os.path.join(BASE, 'marca.json'))
M = json.load(open(_ARQ, encoding='utf-8'))
C = M['cores']

# valor original no motor -> chave no marca.json
_MAPA = [
    ('#F1F3F5', 'fundo'), ('#f1f3f5', 'fundo'),
    ('#FFFFFF', 'papel'),
    ('#E6EAEE', 'nevoa'),
    ('#16181B', 'escuro'), ('#16181b', 'escuro'),
    ('#59606A', 'texto_sec'),
    ('#9AA1AB', 'texto_sec_escuro'), ('#B9C0C8', 'texto_sec_escuro'),
    ('#D9DEE3', 'linha'),
    ('#2C3036', 'linha_escuro'), ('#2E3238', 'linha_escuro'),
    ('#FF5A1F', 'destaque'),
    ('#FFF1EB', 'destaque_claro'),
    ('#FFE7DD', 'texto_no_destaque'), ('#FFD9C9', 'texto_no_destaque'), ('#FFE0D1', 'texto_no_destaque'),
    ('#EEF1F4', 'linha_papel'),
]

def _rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def css(s):
    """Aplica a marca num CSS ou HTML escrito com os tokens da Orbyt."""
    for velho, chave in _MAPA:
        if chave in C:
            s = s.replace(velho, C[chave])
    r, g, b = _rgb(C['destaque']); s = s.replace('rgba(255,90,31,', f'rgba({r},{g},{b},')
    r, g, b = _rgb(C['escuro']); s = s.replace('rgba(22,24,27,', f'rgba({r},{g},{b},')
    L = M['letras']
    s = s.replace('BricolageGrotesque.ttf', L['titulo']).replace('InstrumentSans.ttf', L['texto']).replace('MartianMono.ttf', L['mono'])
    # largura condensada do título: só faz sentido em letra variável com eixo de largura
    if not L.get('titulo_condensa', True):
        s = s.replace('font-stretch:88%;', '')
    return s

def nome_html():
    a, b = M['nome']
    return f'{a} <span>{b}</span>' if b else a

def logo(bg, fg, dot=None):
    """SVG do logo. Placeholders no marca.json: {bg} fundo atrás, {fg} cor do traço, {dot} destaque."""
    return M['logo_svg'].format(bg=bg, fg=fg, dot=dot or C['destaque'])

HANDLE = M['handle']
ARRASTE = M.get('textos', {}).get('arraste', 'arraste →')
LINK = M.get('textos', {}).get('fim', 'link no perfil')
FONTES = os.path.join(BASE, 'fontes')
