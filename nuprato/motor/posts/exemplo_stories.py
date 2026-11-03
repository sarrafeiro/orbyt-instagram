"""Exemplo dos 4 tipos de story do NuPrato. Copie, troque o texto e rode:
python3 posts/exemplo_stories.py   -> saida/stories-exemplo/
"""
import os as _os, sys; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))); sys.path.insert(0, RAIZ)
from story import render
from carrossel import ficha
NP = _os.path.dirname(RAIZ)
L = [
 # 1. frase de argumento (verde ou escuro)
 dict(nome='s01-frase', tema='verde', olho='Sem papo de chef', titulo='Faltou um trem? <em>A receita se vira.</em>', t=108,
      sub='Cê fala o que tem. O NuPrato adapta o resto.', pe='link na bio'),
 # 2. anuncia o post do dia (capa do post)
 dict(nome='s02-capa', tema='creme', olho='Post novo', titulo='Isso aí <em>já é janta.</em>', t=96,
      capa=f'{NP}/posts/2026-11-03-02-geladeira/01.jpg', pe='post novo no perfil'),
 # 3. ficha de receita (educação salvável)
 dict(nome='s03-ficha', tema='papel', olho='Salva esse', titulo='Sem creme de leite?', t=96,
      visual=ficha('Faz assim', ['leite', 'um pouco de amido de milho', 'engrossa no fogo baixo'], rodape='fica cremoso igual'), pe='mais trocas no perfil'),
 # 4. oferta com o selo dourado
 dict(nome='s04-oferta', tema='verde', selo=True, titulo='Sua 1ª receita é <em>por nossa conta.</em>', t=96, pe='link na bio'),
]
render(L, f'{RAIZ}/saida/stories-exemplo')
