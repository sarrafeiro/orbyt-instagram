"""Motor de reels da Orbyt (1080x1920, 30 fps, sem áudio).
O roteiro (spec) define: legendas (fundos), trechos da tela do celular, toques e cartão final.
Tudo é composto em PIL e mandado para o ffmpeg.
"""
import os, subprocess, math, json
from PIL import Image, ImageDraw, ImageFilter
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
F = f'file://{BASE}/www/fonts'
W, H, FPS = 1080, 1920, 30
# geometria do celular na cena
SX, SY, SW, SH = 305, 650, 470, 1017      # tela
BZ = 15                                     # moldura
RAIO_T, RAIO_O = 62, 76

CSS = f"""
@font-face{{font-family:B;src:url({F}/BricolageGrotesque.ttf);font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:I;src:url({F}/InstrumentSans.ttf);font-weight:400 700}}
@font-face{{font-family:M;src:url({F}/MartianMono.ttf);font-weight:100 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:#F1F3F5;color:#16181B;font-family:I;position:relative}}
.txt{{position:absolute;left:84px;right:84px;top:250px;height:360px;display:flex;flex-direction:column;justify-content:flex-end}}
.olho{{font-family:M;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#FF5A1F;margin-bottom:18px}}
h1{{font-family:B;font-weight:700;font-stretch:88%;letter-spacing:-.04em;line-height:.98;font-size:var(--t,86px)}}
h1 em{{font-style:normal;color:#FF5A1F}}
.cel{{position:absolute;left:{SX-BZ}px;top:{SY-BZ}px;width:{SW+2*BZ}px;height:{SH+2*BZ}px;border-radius:{RAIO_O}px;
 background:linear-gradient(145deg,#8E9196,#3B3E43 30%,#6C6F75 55%,#2A2C30 80%,#7A7D82);box-shadow:0 50px 90px -50px rgba(22,24,27,.6)}}
.cel i{{position:absolute;left:{BZ}px;top:{BZ}px;width:{SW}px;height:{SH}px;border-radius:{RAIO_T}px;background:#000}}
.orb{{position:absolute;inset:0}}
.marca{{position:absolute;left:84px;top:150px;display:flex;align-items:center;gap:14px;font-family:B;font-weight:700;font-stretch:88%;font-size:36px;letter-spacing:-.035em}}
.marca span{{font-weight:400;color:#59606A}}
.marca svg{{width:42px;height:42px}}
/* cartão final (camada transparente) */
body.camada{{background:transparent}}
.fim{{position:absolute;left:150px;right:150px;top:1180px;background:#16181B;color:#F1F3F5;border-radius:40px;padding:44px 46px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}}
.fim .preco{{font-family:M;font-weight:600;font-size:96px;letter-spacing:-.05em;line-height:.9}}
.fim .preco small{{font-size:24px;letter-spacing:.06em;color:#B9C0C8;margin-left:14px;text-transform:uppercase}}
.fim p{{font-size:34px;line-height:1.3;margin-top:22px;color:#D9DEE3}}
.fim p b{{color:#FF5A1F;font-weight:600}}
"""
LOGO = '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10.5" fill="none" stroke="#16181B" stroke-width="3.4"/><circle cx="24.4" cy="8.6" r="4.8" fill="#F1F3F5"/><circle cx="24.4" cy="8.6" r="3.1" fill="#FF5A1F"/></svg>'
ORB = '<svg class="orb" viewBox="0 0 1080 1920"><circle cx="1040" cy="900" r="640" fill="none" stroke="rgba(22,24,27,.06)" stroke-width="2"/></svg>'

def html_fundo(titulo, olho='', t=86):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="--t:{t}px">{ORB}
<div class="marca">{LOGO}Orbyt <span>Studio</span></div>
<div class="txt">{f'<div class="olho">{olho}</div>' if olho else ''}<h1>{titulo}</h1></div>
<div class="cel"><i></i></div></body></html>'''

def html_fim(preco, nota, linhas):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="camada">
<div class="fim"><div class="preco">{preco}<small>{nota}</small></div>{''.join(f'<p>{l}</p>' for l in linhas)}</div></body></html>'''

def renderizar_html(pares, pasta):
    """pares: [(nome, html, transparente)] -> PNGs"""
    os.makedirs(pasta, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for nome, h, transp in pares:
            f = f'{pasta}/{nome}.html'; open(f, 'w', encoding='utf-8').write(h)
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
            pg.screenshot(path=f'{pasta}/{nome}.png', omit_background=transp)
        b.close()

def mascara_tela():
    m = Image.new('L', (SW * 4, SH * 4), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, SW * 4 - 1, SH * 4 - 1), radius=RAIO_T * 4, fill=255)
    return m.resize((SW, SH), Image.LANCZOS)

def suave(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

class Reel:
    def __init__(self, pasta, duracao):
        self.pasta = pasta; self.dur = duracao
        self.fundos = []    # (t0, t1, png)
        self.telas = []     # (t0, t1, [arquivos])  sequência espalhada no trecho
        self.toques = []    # (t, x, y) em pixels da captura (780x1688)
        self.camadas = []   # (t0, t1, png transparente)
        self.arrastes = []  # (t0, t1, [(x,y),...]) dedo arrastando
        self._cache = {}

    def img(self, f, tam=None):
        k = (f, tam)
        if k not in self._cache:
            im = Image.open(f).convert('RGBA' if f.endswith('.png') and 'camada' in f else 'RGB')
            if tam: im = im.resize(tam, Image.LANCZOS)
            if len(self._cache) > 400: self._cache.clear()
            self._cache[k] = im
        return self._cache[k]

    def tela_em(self, t):
        for i, (t0, t1, fs) in enumerate(self.telas):
            if t0 <= t < t1:
                k = min(len(fs) - 1, int((t - t0) / max(1e-6, (t1 - t0)) * len(fs)))
                atual = self.img(fs[k], (SW, SH))
                # transição suave para o próximo trecho (0,25 s)
                if i + 1 < len(self.telas) and t > t1 - 0.25 and self.telas[i + 1][0] == t1:
                    prox = self.img(self.telas[i + 1][2][0], (SW, SH))
                    a = suave((t - (t1 - 0.25)) / 0.25)
                    return Image.blend(atual, prox, a)
                return atual
        return self.img(self.telas[-1][2][-1], (SW, SH))

    def fundo_em(self, t):
        for i, (t0, t1, f) in enumerate(self.fundos):
            if t0 <= t < t1:
                bg = self.img(f)
                if i > 0 and t < t0 + 0.3:
                    a = suave((t - t0) / 0.3)
                    return Image.blend(self.img(self.fundos[i - 1][2]), bg, a)
                return bg
        return self.img(self.fundos[-1][2])

    def quadro(self, t, masc):
        q = self.fundo_em(t).copy()
        q.paste(self.tela_em(t), (SX, SY), masc)
        d = ImageDraw.Draw(q, 'RGBA')
        for (tt, x, y) in self.toques:
            dt = t - tt
            if -0.35 <= dt <= 0.45:
                cx, cy = SX + x * SW / 780, SY + y * SH / 1688
                if dt < 0:   # aproxima
                    r = 26; al = int(200 * suave((dt + 0.35) / 0.35))
                else:        # toca e some com anel
                    r = 26 * (1 - 0.25 * suave(dt / 0.15)); al = int(220 * (1 - suave((dt - 0.2) / 0.25)))
                    rr = 26 + 60 * suave(dt / 0.45); d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=(255, 90, 31, int(160 * (1 - dt / 0.45))), width=5)
                d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 90, 31, al), outline=(255, 255, 255, al), width=4)
        for (t0, t1, pts) in self.arrastes:
            if t0 - 0.3 <= t <= t1 + 0.3:
                u = (min(max(t, t0), t1) - t0) / max(1e-6, t1 - t0) * (len(pts) - 1)
                k = min(int(u), len(pts) - 2); f = u - k
                x = pts[k][0] + (pts[k + 1][0] - pts[k][0]) * f; y = pts[k][1] + (pts[k + 1][1] - pts[k][1]) * f
                cx, cy = SX + x * SW / 780, SY + y * SH / 1688
                al = int(220 * (suave((t - (t0 - 0.3)) / 0.3) if t < t0 else (1 - suave((t - t1) / 0.3)) if t > t1 else 1))
                d.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), fill=(255, 90, 31, al), outline=(255, 255, 255, al), width=4)
        for (t0, t1, f) in self.camadas:
            if t0 <= t < t1:
                c = self.img(f)
                a = suave((t - t0) / 0.35)
                if a < 1:
                    c = c.copy(); al = c.getchannel('A').point(lambda v: int(v * a)); c.putalpha(al)
                q.paste(c, (0, 0), c)
        return q.convert('RGB')

    def gravar(self, saida):
        masc = mascara_tela()
        n = int(self.dur * FPS)
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
               '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', saida]
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for k in range(n):
            pr.stdin.write(self.quadro(k / FPS, masc).tobytes())
        pr.stdin.close(); pr.wait()
        # capa (quadro do meio do primeiro fundo)
        self.quadro(1.2, masc).save(saida.replace('.mp4', '-capa.jpg'), quality=92)
        print('ok', saida, n, 'quadros')
