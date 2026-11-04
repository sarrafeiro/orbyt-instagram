"""Stories de 04/11 a 08/11/2026 (quarta a domingo). python3 posts/stories_2026_11_04.py"""
import os as _os, sys; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))); sys.path.insert(0, RAIZ)
from story import render
from carrossel import ficha
S = RAIZ + '/saida'
PN = 'post novo no perfil'
LB = 'link na bio'
L = [
 # qua 11:10 peça solta
 dict(nome='s01-qua-frase', tema='verde', olho='Sem papo de chef', titulo='Cê diz o prato. <em>A gente faz caber na sua cozinha.</em>', t=96,
      sub='Com o que tem na geladeira e a panela que cê tem.', pe=LB),
 # qua 17:10 anuncia o 10
 dict(nome='s02-qua-post', tema='creme', olho='Post novo', titulo='Diminuiu a receita? <em>O tempo muda&nbsp;também.</em>', t=88,
      capa=f'{S}/10-receita-pra-6/01.png', pe=PN),
 # qui 11:10 ficha de troca
 dict(nome='s03-qui-ficha', tema='papel', olho='Salva esse', titulo='Sem farinha de rosca?', t=96,
      visual=ficha('Faz assim', ['bolacha cream cracker', 'esfarela no saco', 'empana do mesmo jeito'], rodape='fica crocante igual'), pe='mais trocas no perfil'),
 # qui 17:10 anuncia o 11
 dict(nome='s04-qui-post', tema='verde', olho='Post novo', titulo='Batata, ovo e cebola. <em>Já é janta.</em>', t=96,
      capa=f'{S}/11-tres-trens/01.png', pe=PN),
 # sex 11:10 frase
 dict(nome='s05-sex-frase', tema='escuro', olho='Receita de mãe', titulo='Um tiquinho de sal é <em>quanto,&nbsp;mãe?</em>', t=100,
      sub='No NuPrato a medida vem do tamanho da sua panela.', pe=LB),
 # sex 17:10 anuncia o 12
 dict(nome='s06-sex-post', tema='creme', olho='Comenta lá', titulo='O mais pedido <em>vira post.</em>', t=100,
      capa=f'{S}/12-nunca-teve-coragem/01.png', pe=PN),
 # sáb 09:10 oferta com selo
 dict(nome='s07-sab-oferta', tema='verde', selo=True, titulo='Sua 1ª receita guiada é <em>por nossa conta.</em>', t=92, pe=LB),
 # sáb 20:10 anuncia o 13
 dict(nome='s08-sab-post', tema='escuro', olho='Receita mineira', titulo='Feijão sem caldo, <em>senão vira&nbsp;papa.</em>', t=92,
      capa=f'{S}/13-tropeiro/01.png', pe=PN),
 # dom 10:10 ficha de troca
 dict(nome='s09-dom-ficha', tema='papel', olho='Domingo de almoço', titulo='Sem panela de pressão?', t=92,
      visual=ficha('Faz assim', ['panela comum tampada', 'mais água e mais tempo', 'feijão de molho na véspera'], rodape='demora mais, fica igual'), pe='mais trocas no perfil'),
 # dom 18:10 frase
 dict(nome='s10-dom-frase', tema='verde', olho='Pra semana que vem', titulo='Livro de receita? <em>Trem do passado, sô.</em>', t=100,
      sub='Fala o prato. O NuPrato adapta e te guia até o fim.', pe=LB),
]
render(L, f'{S}/stories-2026-11-04')
