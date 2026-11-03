"""Copia o que foi gerado em nuprato/motor/saida/<pasta> para nuprato/<destino> e mostra as URLs públicas.
Uso: python3 publicar.py <pasta em saida> <destino dentro de nuprato/>
  ex: python3 publicar.py 04-cinco-trocas posts/2026-11-03-04-cinco-trocas
      python3 publicar.py stories-2026-11-09 stories/2026-11-09
PNG vira JPG (qualidade 93). Depois: git add, commit e push na raiz do repositório.
Opção --hash: imprime as URLs com o hash do último commit (use isso no Trypost; o link da branch pode vir velho do cache).
"""
import sys, os, json, glob, subprocess
from PIL import Image
MOTOR = os.path.dirname(os.path.abspath(__file__)); NP = os.path.dirname(MOTOR); REPO = os.path.dirname(NP)
args = [a for a in sys.argv[1:] if a != '--hash']
ref = 'main'
if '--hash' in sys.argv:
    ref = subprocess.check_output(['git', '-C', REPO, 'rev-parse', 'HEAD'], text=True).strip()
RAW = f'https://raw.githubusercontent.com/sarrafeiro/orbyt-instagram/{ref}/nuprato/'
orig, dest = args[0], args[1].strip('/')
src = os.path.join(MOTOR, 'saida', orig); out = os.path.join(NP, dest); os.makedirs(out, exist_ok=True)
urls = []
for f in sorted(glob.glob(f'{src}/*.png')):
    j = os.path.basename(f)[:-4] + '.jpg'
    if '--hash' not in sys.argv:
        Image.open(f).convert('RGB').save(f'{out}/{j}', quality=93, optimize=True)
    urls.append(RAW + f'{dest}/{j}')
print(json.dumps(urls, indent=1))
