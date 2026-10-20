import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
PE = 'post novo no perfil · @orbyt_studio'
L = [
 dict(nome='s01-p01', olho='Post novo', titulo='Como funciona: seu site em 2 dias <em>e você só paga depois.</em>', t=84, capa=f'{S}/p01-como-funciona/01.png', pe=PE),
 dict(nome='s02-p04', olho='Advocacia', titulo='Seu cliente pesquisa você <em>antes de ligar.</em>', capa=f'{S}/p04-adv-pesquisa/01.png', pe=PE),
 dict(nome='s03-r03', olho='Barbearia', titulo='Olha o site que a sua barbearia <em>pode ter.</em>', t=88, cel='barb-cel-capa.png', pe='reel novo no perfil · @orbyt_studio'),
 dict(nome='s04-p06', olho='Barbearia', titulo='O link do app <em>não é o seu site.</em>', capa=f'{S}/p06-barb-link-app/01.png', pe=PE),
 dict(nome='s05-r02', olho='Advocacia', titulo='O cliente escolhe o assunto <em>em três cliques.</em>', t=88, cel='adv1-cel-guia3.png', pe='reel novo no perfil · @orbyt_studio'),
 dict(nome='s06-p07', olho='Preço sem letra miúda', titulo='Quanto custa um site <em>com a Orbyt?</em>', capa=f'{S}/p07-precos/01.png', pe=PE),
 dict(nome='s07-p08', olho='Antes de contratar', titulo='Três jeitos de ter um site. <em>Compare.</em>', capa=f'{S}/p08-tres-jeitos/01.png', pe=PE),
 dict(nome='s08-frase-pagamento', escuro=True, olho='Sem risco', titulo='A gente trabalha primeiro. <em>Você paga depois.</em>', t=110,
      sub='Você vê o site pronto num link nosso, pede até 2 ajustes e só paga se aprovar. <b>R$ 0 pra começar.</b>', pe='chama no whatsapp · link no perfil'),
 dict(nome='s09-p09', olho='Barbearia', titulo='5 coisas que o site da sua barbearia <em>precisa ter.</em>', t=86, capa=f'{S}/p09-barb-5-coisas/01.png', pe=PE),
 dict(nome='s10-frase-preco', escuro=True, olho='Site com modelo do seu segmento', titulo='Preço fechado.', t=110, preco='R$ 797',
      sub='Pronto em até 2 dias úteis. Pix ou cartão parcelado. <b>Sem mensalidade.</b>', pe='chama no whatsapp · link no perfil'),
 dict(nome='s11-modelo-adv', olho='Modelo de advocacia', titulo='O site do seu escritório <em>pode ser assim.</em>', t=88, cel='adv2-cel-capa.png', pe='chama no whatsapp · link no perfil'),
]
render(L, f'{S}/stories')
