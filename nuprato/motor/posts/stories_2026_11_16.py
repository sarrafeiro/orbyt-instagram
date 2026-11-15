"""Stories de 16/11 a 22/11/2026. python3 posts/stories_2026_11_16.py
Seg, qua e sex: o das 17:10 anuncia o post das 12:40 (já no ar). Ter e qui: anuncia o das 18:40. Sáb 18:10 anuncia o de 10:40.
"""
import os as _os, sys; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))); sys.path.insert(0, RAIZ)
from story import render
from carrossel import ficha
S = RAIZ + '/saida'
PN = 'post novo no perfil'
LB = 'link na bio'
MT = 'mais trocas no perfil'
L = [
 # seg 11:10 frase
 dict(nome='s01-seg-frase', tema='verde', olho='Pra 1, pra 2 ou pra família', titulo='Cê fala pra quantos.<br><em>A&nbsp;receita acompanha.</em>', t=84,
      sub='Quantidade e tempo de panela ajustados pra sua mesa.', pe=LB),
 # seg 17:10 anuncia o 25
 dict(nome='s02-seg-post', tema='creme', olho='Post novo', titulo='Feijão sem pressão:<br><em>molho na&nbsp;véspera.</em>', t=92,
      capa=f'{S}/25-feijao-sem-pressao/01.png', pe=PN),
 # ter 11:10 ficha de troca
 dict(nome='s03-ter-ficha', tema='papel', olho='Salva esse', titulo='Sem alho?', t=104,
      visual=ficha('Faz assim', ['alho em pó, bem pouquinho', 'entra junto com a cebola', 'vai provando'], rodape='menos é mais'), pe=MT),
 # ter 17:10 anuncia o 27
 dict(nome='s04-ter-post', tema='escuro', olho='Post novo', titulo='Refoga o arroz<br><em>antes da&nbsp;água.</em>', t=96,
      capa=f'{S}/27-lavar-arroz/01.png', pe=PN),
 # qua 11:10 frase
 dict(nome='s05-qua-frase', tema='escuro', olho='Do jeito que cê fala', titulo='Fala o prato.<br><em>Sem termo de&nbsp;chef.</em>', t=100,
      sub='Cê conta o que tem e quantas pessoas. O NuPrato adapta o resto.', pe=LB),
 # qua 17:10 anuncia o 28
 dict(nome='s06-qua-post', tema='creme', olho='Post novo', titulo='Ele adapta e<br><em>explica o que&nbsp;mudou.</em>', t=92,
      capa=f'{S}/28-fala-do-seu-jeito/01.png', pe=PN),
 # qui 11:10 ficha de troca
 dict(nome='s07-qui-ficha', tema='papel', olho='Salva esse', titulo='Sem farinha pra engrossar?', t=88,
      visual=ficha('Faz assim', ['amido de milho', 'dissolvido em água fria', 'entra no fim, mexendo'], rodape='engrossa rapidinho'), pe=MT),
 # qui 17:10 anuncia o 30
 dict(nome='s08-qui-post', tema='verde', olho='Post novo', titulo='Com isso em casa,<br><em>sempre tem&nbsp;janta.</em>', t=96,
      capa=f'{S}/30-sete-trens/01.png', pe=PN),
 # sex 11:10 frase (feriado)
 dict(nome='s09-sex-frase', tema='escuro', olho='Feriado', titulo='Dia de cozinhar<br><em>sem&nbsp;pressa.</em>', t=104,
      sub='Escolhe o prato. O NuPrato te guia até o fim.', pe=LB),
 # sex 17:10 anuncia o 31
 dict(nome='s10-sex-post', tema='creme', olho='Post novo', titulo='Comenta o número<br><em>do seu&nbsp;prato.</em>', t=96,
      capa=f'{S}/31-prato-do-feriado/01.png', pe=PN),
 # sáb 09:10 oferta com selo
 dict(nome='s11-sab-oferta', tema='verde', selo=True, titulo='Fala o prato do almoço.<br><em>A 1ª receita guiada é&nbsp;grátis.</em>', t=80, pe=LB),
 # sáb 18:10 anuncia o 33
 dict(nome='s12-sab-post', tema='escuro', olho='Post novo', titulo='Sem forno?<br><em>Tampa a&nbsp;frigideira.</em>', t=86,
      capa=f'{S}/33-panqueca/01.png', pe=PN),
 # dom 10:10 ficha de troca
 dict(nome='s13-dom-ficha', tema='papel', olho='Domingo de almoço', titulo='Sem manteiga pro refogado?', t=88,
      visual=ficha('Faz assim', ['óleo', 'um pouco menos que a manteiga', 'refoga igual'], rodape='gosto mais neutro'), pe=MT),
 # dom 18:10 frase
 dict(nome='s14-dom-frase', tema='verde', olho='Semana que vem', titulo='Segunda tem janta.<br><em>Cê só fala o&nbsp;prato.</em>', t=96,
      sub='O NuPrato adapta pra sua cozinha e te guia até o fim.', pe=LB),
]
render(L, f'{S}/stories-2026-11-16')
