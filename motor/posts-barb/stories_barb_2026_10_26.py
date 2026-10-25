import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
# Stories da semana de 26/10/2026 (2 por dia). Celular só em 2 (s02 antes e depois, s06 espaço).
S = RAIZ + '/saida'
REPO = _os.path.dirname(RAIZ)
PE = 'post novo no perfil · @orbytstudio_'
PR = 'reel novo no perfil · @orbytstudio_'
WA = 'whatsapp no link do perfil · @orbytstudio_'
L = [
 dict(nome='s01-seg-frase-cadeira', escuro=True, olho='Terça à tarde', titulo='Cadeira vazia <em>também custa.</em>', t=112,
      sub='O site mostra o seu horário livre pra quem procura agora. <b>Agendar num toque.</b>', pe=WA),
 dict(nome='s02-seg-antes-depois', olho='Antes e depois', titulo='Arrasta <em>pra comparar.</em>', t=100,
      cel='barb-cel-antes-depois.png', pe='antes e depois · reel no perfil · @orbytstudio_'),
 dict(nome='s03-ter-frase-app', escuro=True, olho='Já tenho o link do app', titulo='O app agenda. <em>O site vende.</em>', t=112,
      sub='O cliente vê a sua marca, o seu preço e os seus cortes antes de marcar. <b>E o Agendar leva pro seu app.</b>', pe=WA),
 dict(nome='s04-ter-enquanto-corta', olho='Barbearia', titulo='O celular vibra. <em>A mensagem fica pra depois.</em>', t=88,
      capa=f'{REPO}/barbearia/posts/2026-10-26-bb10-enquanto-corta/01.jpg', pe=PE),
 dict(nome='s05-qua-frase-conta', escuro=True, olho='Faz a conta', titulo='5 cortes <em>ou o site?</em>', t=118, preco='R$ 399',
      sub='5 cortes de R$ 80 dão R$ 400. O site custa menos, uma vez só. <b>Sem mensalidade.</b>', pe=WA),
 dict(nome='s06-qua-reel-equipe', olho='Barbearia', titulo='Quem vai cortar. <em>E agendar direto com ele.</em>', t=88,
      cel='barb-cel-espaco2.png', pe=PR),
 dict(nome='s07-qui-frase-foto', escuro=True, olho='Sem foto boa?', titulo='A gente começa <em>com foto de exemplo.</em>', t=104,
      sub='E troca pelas suas quando você mandar. <b>Você só paga depois de aprovar.</b>', pe=WA),
 dict(nome='s08-qui-faz-a-conta', olho='Cliente que volta', titulo='17 cortes por ano. <em>De um cliente só.</em>', t=92,
      capa=f'{REPO}/barbearia/posts/2026-10-28-bb09-faz-a-conta/01.jpg', pe=PE),
 dict(nome='s09-sex-frase-nome', escuro=True, olho='O site é seu', titulo='Publicado <em>no seu nome.</em>', t=118,
      sub='A gente publica com você, numa conta sua. <b>Sem mensalidade pra Orbyt.</b>', pe=WA),
 dict(nome='s10-sex-segundos', olho='Salva pra conferir', titulo='Ele quer <em>ver o trabalho.</em>', t=100,
      capa=f'{S}/bb12-primeiros-segundos/01.png', pe=PE),
 dict(nome='s11-sab-mitos', olho='Mito', titulo='O boca a boca <em>já resolve?</em>', t=100,
      capa=f'{REPO}/barbearia/posts/2026-10-30-bb08-mitos/01.jpg', pe=PE),
 dict(nome='s12-sab-reel-agendar', escuro=True, olho='Antes e depois', titulo='Gostou do corte? <em>Toca em Agendar.</em>', t=108,
      sub='O cliente arrasta, vê o seu degradê e marca na hora. <b>Reel novo no perfil.</b>', pe=PR),
 dict(nome='s13-dom-frase-ajustes', escuro=True, olho='Como funciona', titulo='Quer mudar algo? <em>Pede até 2 ajustes.</em>', t=104,
      sub='Você vê o site pronto num link nosso e só depois paga. <b>Pix ou cartão parcelado.</b>', pe=WA),
 dict(nome='s14-dom-frase-semana', escuro=True, olho='Semana nova', titulo='Manda o nome <em>da sua barbearia.</em>', t=108,
      sub='Em até 2 dias úteis você vê o site pronto. <b>Sem entrada nenhuma.</b>', pe=WA),
]
render(L, f'{S}/stories-barb-2026-10-26')
