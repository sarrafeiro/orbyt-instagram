"""Stories de 09/11 a 15/11/2026. python3 posts/stories_2026_11_09.py"""
import os as _os, sys; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))); sys.path.insert(0, RAIZ)
from story import render
from carrossel import ficha
S = RAIZ + '/saida'
PN = 'post novo no perfil'
LB = 'link na bio'
MT = 'mais trocas no perfil'
L = [
 # seg 11:10 frase
 dict(nome='s01-seg-frase', tema='verde', olho='Sem papo de chef', titulo='Faltou um trem? <em>A receita se&nbsp;vira.</em>', t=104,
      sub='Cê fala o que tem. O NuPrato adapta o resto.', pe=LB),
 # seg 17:10 anuncia o 14
 dict(nome='s02-seg-post', tema='creme', olho='Post novo', titulo='Arroz empapado <em>vira&nbsp;bolinho.</em>', t=96,
      capa=f'{S}/14-arroz-empapou/01.png', pe=PN),
 # ter 11:10 ficha de troca
 dict(nome='s03-ter-ficha', tema='papel', olho='Salva esse', titulo='Sem extrato de tomate?', t=92,
      visual=ficha('Faz assim', ['tomate bem maduro', 'picado sem semente', 'apura no fogo até virar molho'], rodape='fica com mais gosto'), pe=MT),
 # ter 17:10 anuncia o 15
 dict(nome='s04-ter-post', tema='escuro', olho='Post novo', titulo='5 minutinhos <em>antes de&nbsp;cortar.</em>', t=96,
      capa=f'{S}/15-carne-descansa/01.png', pe=PN),
 # qua 11:10 frase
 dict(nome='s05-qua-frase', tema='escuro', olho='Do seu jeito', titulo='Receita boa é a que <em>cabe na sua&nbsp;cozinha.</em>', t=96,
      sub='Fogão, forno, air fryer ou panela de pressão: cê conta o que tem.', pe=LB),
 # qua 17:10 anuncia o 16
 dict(nome='s06-qua-post', tema='creme', olho='Post novo', titulo='Menos graus, <em>menos&nbsp;tempo.</em>', t=100,
      capa=f'{S}/16-sem-forno/01.png', pe=PN),
 # qui 11:10 ficha de troca
 dict(nome='s07-qui-ficha', tema='papel', olho='Salva esse', titulo='Sem creme de leite?', t=96,
      visual=ficha('Faz assim', ['requeijão cremoso', 'entra no fim, fogo baixo', 'mexe até ficar cremoso'], rodape='strogonoff aprovado'), pe=MT),
 # qui 17:10 anuncia o 17
 dict(nome='s08-qui-post', tema='verde', olho='Post novo', titulo='Sem fermento, <em>não&nbsp;faz.</em>', t=104,
      capa=f'{S}/17-bolo-trocas/01.png', pe=PN),
 # sex 11:10 frase
 dict(nome='s09-sex-frase', tema='escuro', olho='Antes do delivery', titulo='Mercado às 20h? <em>Abre a geladeira&nbsp;primeiro.</em>', t=92,
      sub='Cê conta o que tem. O NuPrato monta o prato.', pe=LB),
 # sex 17:10 anuncia o 18
 dict(nome='s10-sex-post', tema='creme', olho='Post novo', titulo='Ovo, arroz e meia cebola <em>é&nbsp;janta.</em>', t=88,
      capa=f'{S}/18-o-que-tem-pra-janta/01.png', pe=PN),
 # sáb 09:10 oferta com selo
 dict(nome='s11-sab-oferta', tema='verde', selo=True, titulo='Escolhe o prato.<br><em>A 1ª receita guiada é&nbsp;grátis.</em>', t=84, pe=LB),
 # sáb 18:10 anuncia o 19
 dict(nome='s12-sab-post', tema='escuro', olho='Post novo', titulo='Sobrou frango? <em>Vira&nbsp;farofa.</em>', t=100,
      capa=f'{S}/19-frango-sobrou/01.png', pe=PN),
 # dom 10:10 ficha de troca
 dict(nome='s13-dom-ficha', tema='papel', olho='Domingo de almoço', titulo='Sem ovo pra empanar?', t=92,
      visual=ficha('Faz assim', ['leite com farinha de trigo', 'vira uma pastinha mole', 'passa e empana igual'], rodape='gruda do mesmo jeito'), pe=MT),
 # dom 18:10 frase
 dict(nome='s14-dom-frase', tema='verde', olho='Pra semana que vem', titulo='Semana nova, <em>janta&nbsp;resolvida.</em>', t=104,
      sub='Fala o prato. O NuPrato adapta e te guia até o fim.', pe=LB),
]
render(L, f'{S}/stories-2026-11-09')
