"""Carrossel de fotos pro TikTok do NuPrato (formato descoberta), 1080x1920.

Uso: python3 -I carrossel_tiktok.py config.json
Opcional: SO=nome-do-carrossel pra gerar só um.

config.json:
{
  "fotos": "pasta com os pratos em PNG 1:1 (nome-do-prato.png)",
  "selo": "caminho do selo-ouro.png",
  "card": "caminho do card-final-generico.jpg",
  "cenas": "pasta com as cenas 9:16 geradas (nome.png), só se usar o tipo cena",
  "out": "pasta de saída",
  "carrosseis": {
    "c6-exemplo": [
      {"tipo": "liso", "texto": "...", "cor": "verde", "tam": 84, "sub": "linha amarela opcional"},
      {"tipo": "foto", "foto": "pao-de-queijo", "texto": "...", "zoom": 1.0},
      {"tipo": "chat", "contato": "mãe", "msgs": [["eu", "..."], ["ele", "..."]]},
      {"tipo": "cena", "img": "nome-da-cena", "texto": "...", "sub": "opcional", "corta_topo": 0.0},
      {"tipo": "revela", "texto": "..."},
      {"tipo": "card"}
    ]
  }
}
cena = foto 9:16 em tela cheia com degradê escuro em cima e frase com contorno (corta_topo tira uma faixa ruim do topo).
cor do liso: verde, grafite ou creme. zoom > 1 aproxima o prato (efeito "pouco tempo depois").
Saída: out/{nome}__{i}.jpg e out/folha-{nome}.jpg (folha de contato pra conferir).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, CX = 1080, 1920, 520  # CX fora do centro pra fugir dos botões da direita do TikTok
VERDE = (94, 156, 118); GRAFITE = (46, 49, 51); CREME = (250, 247, 242); AMARELO = (244, 211, 94)
CORES = {'verde': VERDE, 'grafite': GRAFITE, 'creme': CREME}


def fonte(peso):
    for p in (f'/usr/share/fonts/truetype/google-fonts/Poppins-{peso}.ttf',
              f'/usr/share/fonts/truetype/poppins/Poppins-{peso}.ttf',
              '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if peso == 'Bold' else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
        if os.path.exists(p):
            return p
    raise SystemExit('fonte não encontrada: instale Poppins (pip/fonts-google) ou DejaVu')


F_B, F_M = fonte('Bold'), fonte('Medium')


def wrap(d, t, f, maxw):
    ls, cur = [], ''
    for w in t.split():
        x = (cur + ' ' + w).strip()
        if d.textlength(x, font=f) <= maxw: cur = x
        else: ls.append(cur); cur = w
    ls.append(cur); return ls


def texto(img, t, y, tam=70, cor=(255, 255, 255), contorno=True, maxw=860, fnt=None):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(fnt or F_B, tam); lh = int(tam * 1.2)
    ls = wrap(d, t, f, maxw)
    for i, l in enumerate(ls):
        x = CX - d.textlength(l, font=f) / 2
        if contorno:
            d.text((x, y + i * lh), l, font=f, fill=cor, stroke_width=max(4, tam // 14), stroke_fill=(0, 0, 0))
        else:
            d.text((x, y + i * lh), l, font=f, fill=cor)
    return y + len(ls) * lh


class Carrossel:
    def __init__(self, cfg):
        self.cfg = cfg

    def foto(self, s):
        src = Image.open(os.path.join(self.cfg['fotos'], s['foto'] + '.png')).convert('RGB')
        lado0 = src.width
        # fundo: canto da bancada ampliado e desfocado (nunca o prato desfocado)
        fundo = src.crop((0, 0, int(lado0 * .22), int(lado0 * .22))).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(10))
        zoom = float(s.get('zoom', 1.0)); lado = int(1000 * zoom); p = src.resize((lado, lado), Image.LANCZOS)
        if zoom > 1:
            c = (lado - 1000) // 2; p = p.crop((c, c, c + 1000, c + 1000))
        fundo.paste(p, ((W - 1000) // 2, 720))
        texto(fundo, s['texto'], 330, s.get('tam', 72))
        return fundo

    def liso(self, s):
        cor = CORES.get(s.get('cor', 'grafite'), GRAFITE)
        cor_txt = GRAFITE if cor == CREME else (255, 255, 255)
        img = Image.new('RGB', (W, H), cor)
        y = texto(img, s['texto'], 640, s.get('tam', 84), cor=cor_txt, contorno=False)
        if s.get('sub'):
            texto(img, s['sub'], y + 40, 56, cor=VERDE if cor == CREME else AMARELO, contorno=False, fnt=F_M)
        return img

    def revela(self, s):
        img = Image.new('RGB', (W, H), VERDE)
        y = texto(img, s['texto'], 360, s.get('tam', 76), contorno=False)
        selo = Image.open(self.cfg['selo']).convert('RGBA'); selo = selo.crop(selo.getbbox()).resize((640, 640), Image.LANCZOS)
        img.paste(selo, ((W - 640) // 2, max(y + 80, 820)), selo)
        return img

    def chat(self, s):
        img = Image.new('RGB', (W, H), (236, 229, 221)); d = ImageDraw.Draw(img)
        f = ImageFont.truetype(F_M, 50)
        d.rectangle([0, 0, W, 360], fill=(32, 120, 104))
        d.text((60, 260), s.get('contato', 'mãe'), font=ImageFont.truetype(F_B, 56), fill=(255, 255, 255))
        y = 460
        for quem, t in s['msgs']:
            ls = wrap(d, t, f, 620); bw = int(max(d.textlength(l, font=f) for l in ls) + 70); bh = len(ls) * 66 + 50
            x = W - 70 - bw if quem == 'eu' else 70
            d.rounded_rectangle([x, y, x + bw, y + bh], radius=28, fill=(217, 253, 211) if quem == 'eu' else (255, 255, 255))
            for i, l in enumerate(ls): d.text((x + 35, y + 22 + i * 66), l, font=f, fill=(30, 30, 30))
            y += bh + 34
        return img

    def cena(self, s):
        """Foto 9:16 ocupando a tela toda, degradê escuro em cima e frase com contorno."""
        src = Image.open(os.path.join(self.cfg['cenas'], s['img'] + '.png')).convert('RGB')
        ct = float(s.get('corta_topo', 0))
        if ct:
            src = src.crop((0, int(src.height * ct), src.width, src.height))
        esc = max(W / src.width, H / src.height)
        src = src.resize((int(src.width * esc + 1), int(src.height * esc + 1)), Image.LANCZOS)
        x0 = (src.width - W) // 2; y0 = (src.height - H) // 2 if not ct else 0
        img = src.crop((x0, y0, x0 + W, y0 + H)).convert('RGBA')
        grad = Image.new('L', (1, H), 0)
        alto = int(H * s.get('degrade', 0.42))
        for y in range(alto):
            grad.putpixel((0, y), int(175 * (1 - y / alto) ** 1.3))
        sombra = Image.new('RGBA', (W, H), (0, 0, 0, 255)); sombra.putalpha(grad.resize((W, H)))
        img = Image.alpha_composite(img, sombra).convert('RGB')
        y = texto(img, s['texto'], s.get('y', 300), s.get('tam', 72))
        if s.get('sub'):
            texto(img, s['sub'], y + 24, 54, cor=AMARELO)
        if s.get('selo'):
            # selo dourado solto sobre a cena (slide de revela com imagem); posição e tamanho ajustáveis
            tam = int(s.get('selo_tam', 340))
            selo = Image.open(self.cfg['selo']).convert('RGBA'); selo = selo.crop(selo.getbbox()).resize((tam, tam), Image.LANCZOS)
            img.paste(selo, (int(s.get('selo_x', W - tam - 48)), int(s.get('selo_y', y + 60))), selo)
        return img

    def card(self, s):
        return Image.open(self.cfg['card']).convert('RGB').resize((W, H), Image.LANCZOS)

    def slide(self, s):
        return getattr(self, s['tipo'])(s)


def folha(imgs, destino):
    th = [i.resize((270, 480)) for i in imgs]
    f = Image.new('RGB', (270 * len(th) + 10 * (len(th) + 1), 500), (255, 255, 255))
    for k, t in enumerate(th): f.paste(t, (10 + k * 280, 10))
    f.save(destino, quality=85)


def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = cfg['out']; os.makedirs(out, exist_ok=True)
    c = Carrossel(cfg); so = os.environ.get('SO')
    for nome, slides in cfg['carrosseis'].items():
        if so and nome != so: continue
        imgs = [c.slide(s) for s in slides]
        if slides[-1]['tipo'] != 'card':
            imgs.append(c.card({}))
        for i, im in enumerate(imgs, 1):
            im.save(os.path.join(out, f'{nome}__{i}.jpg'), quality=90)
        folha(imgs, os.path.join(out, f'folha-{nome}.jpg'))
        print(nome, len(imgs))


if __name__ == '__main__':
    main()
