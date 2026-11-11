"""Copia o que foi gerado em motor/saida/<pasta> pro repositório e mostra as URLs públicas.
Uso: python3 publicar.py <pasta em saida> <destino no repo>
  ex: python3 publicar.py p10-tema posts/2026-11-10-p10-tema
PNG vira JPG (qualidade 95). MP4 vai como reel.mp4.
Depois: git add, commit e push. Agende com o link do COMMIT (rode de novo com --hash depois do push),
porque o link da branch pode servir arquivo velho do cache por uns minutos.
"""
import sys, os, json, glob, shutil, subprocess, re
from PIL import Image
MOTOR = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(MOTOR)
def raw_base(usar_hash):
    url = subprocess.run(['git', '-C', REPO, 'remote', 'get-url', 'origin'], capture_output=True, text=True).stdout.strip()
    m = re.search(r'github\.com[:/](.+?)/(.+?)(\.git)?$', url)
    ref = subprocess.run(['git', '-C', REPO, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip() if usar_hash else 'main'
    return f'https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{ref}/'
args = [a for a in sys.argv[1:] if a != '--hash']; usar_hash = '--hash' in sys.argv
orig, dest = args[0], args[1].strip('/')
src = os.path.join(MOTOR, 'saida', orig); out = os.path.join(REPO, dest); os.makedirs(out, exist_ok=True)
RAW = raw_base(usar_hash); urls = []
for f in sorted(glob.glob(f'{src}/*.png')):
    nome = os.path.basename(f)
    if nome.startswith(('f', 'camada')) and glob.glob(f'{src}/*.mp4'):
        continue  # fundos do reel não são publicados
    j = nome[:-4] + '.jpg'
    Image.open(f).convert('RGB').save(f'{out}/{j}', quality=95, optimize=True)
    urls.append(RAW + f'{dest}/{j}')
for f in sorted(glob.glob(f'{src}/*.mp4')):
    shutil.copy(f, f'{out}/reel.mp4'); urls.append(RAW + f'{dest}/reel.mp4')
print(json.dumps(urls, indent=1))
