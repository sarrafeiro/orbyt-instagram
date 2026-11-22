"""Stories de 23/11 a 29/11/2026. python3 posts/stories_2026_11_23.py
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
 dict(nome='s01-seg-frase', tema='verde', olho='Segunda-feira', titulo='Janta simples<br><em>também é&nbsp;janta.</em>', t=96,
      sub='Cê conta o que tem. O NuPrato monta o prato com isso.', pe=LB),
 # seg 17:10 anuncia o 35
 dict(nome='s02-seg-post', tema='escuro', olho='Post novo', titulo='Óleo na água?<br><em>Fica&nbsp;boiando.</em>', t=96,
      capa=f'{S}/35-oleo-macarrao/01.png', pe=PN),
 # ter 11:10 ficha de troca
 dict(nome='s03-ter-ficha', tema='papel', olho='Salva esse', titulo='Sem leite pro purê?', t=96,
      visual=ficha('Faz assim', ['um pouco da água do cozimento', 'uma colher de manteiga', 'amassa com a batata quente'], rodape='vai pondo aos poucos'), pe=MT),
 # ter 17:10 anuncia o 37
 dict(nome='s04-ter-post', tema='creme', olho='Post novo', titulo='Frigideira lotada<br><em>vira sopa de&nbsp;carne.</em>', t=90,
      capa=f'{S}/37-bife-duro/01.png', pe=PN),
 # qua 11:10 frase
 dict(nome='s05-qua-frase', tema='escuro', olho='Do jeito que tá', titulo='Fala o que tem<br><em>na&nbsp;geladeira.</em>', t=100,
      sub='O NuPrato adapta a receita e explica o que mudou.', pe=LB),
 # qua 17:10 anuncia o 38
 dict(nome='s06-qua-post', tema='verde', olho='Post novo', titulo='Ele monta o prato<br><em>com o que&nbsp;tem.</em>', t=92,
      capa=f'{S}/38-tinha-isso/01.png', pe=PN),
 # qui 11:10 ficha de troca
 dict(nome='s07-qui-ficha', tema='papel', olho='Salva esse', titulo='Sem caldo em tablete?', t=92,
      visual=ficha('Faz assim', ['refoga bem cebola e alho', 'sal na medida, provando', 'cheiro-verde no fim'], rodape='o refogado dá o gosto'), pe=MT),
 # qui 17:10 anuncia o 40
 dict(nome='s08-qui-post', tema='creme', olho='Post novo', titulo='Sobrou feijão?<br><em>Vira&nbsp;tutu.</em>', t=100,
      capa=f'{S}/40-sobrou-feijao/01.png', pe=PN),
 # sex 11:10 frase (Black Friday)
 dict(nome='s09-sex-frase', tema='escuro', olho='Black Friday', titulo='Estoca o que<br><em>cê já&nbsp;usa.</em>', t=104,
      sub='O resto vira coisa vencida no fundo do armário.', pe=LB),
 # sex 17:10 anuncia o 41
 dict(nome='s10-sex-post', tema='verde', olho='Post novo', titulo='Os mais antigos<br><em>vão pra&nbsp;frente.</em>', t=96,
      capa=f'{S}/41-black-friday/01.png', pe=PN),
 # sáb 09:10 oferta com selo
 dict(nome='s11-sab-oferta', tema='verde', selo=True, titulo='Escolhe o prato do sábado.<br><em>A 1ª receita guiada é&nbsp;grátis.</em>', t=78, pe=LB),
 # sáb 18:10 anuncia o 43
 dict(nome='s12-sab-post', tema='escuro', olho='Post novo', titulo='Fala o prato.<br><em>Vai pro&nbsp;fogão.</em>', t=100,
      capa=f'{S}/43-prato-do-sabado/01.png', pe=PN),
 # dom 10:10 ficha de troca
 dict(nome='s13-dom-ficha', tema='papel', olho='Domingo de almoço', titulo='Sem queijo ralado?', t=96,
      visual=ficha('Faz assim', ['muçarela picadinha', 'bem miúda', 'derrete por cima igual'], rodape='gosto mais suave'), pe=MT),
 # dom 18:10 frase
 dict(nome='s14-dom-frase', tema='creme', olho='Amanhã é segunda', titulo='Cê fala o prato.<br><em>A&nbsp;semana&nbsp;agradece.</em>', t=84,
      sub='O NuPrato adapta pra sua cozinha e te guia até o fim.', pe=LB),
]
render(L, f'{S}/stories-2026-11-23')
