"""Folha de contato: python3 folha.py saida/<slug> ... -> saida/_folhas/<slug>.jpg"""
import sys, os, glob
from PIL import Image
os.makedirs('saida/_folhas', exist_ok=True)
for d in sys.argv[1:]:
    fs = sorted(glob.glob(f'{d}/[0-9][0-9].png')); w = 360; h = 450
    im = Image.new('RGB', (w*len(fs) + 10*(len(fs)+1), h+20), '#888')
    for i, f in enumerate(fs):
        im.paste(Image.open(f).convert('RGB').resize((w, h)), (10 + i*(w+10), 10))
    im.save(f'saida/_folhas/{os.path.basename(d)}.jpg', quality=85)
