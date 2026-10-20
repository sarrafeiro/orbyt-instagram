import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
PE = 'post novo no perfil · @orbyt_studio'
PR = 'reel novo no perfil · @orbyt_studio'
WA = 'chama no whatsapp · link no perfil'
L = [
 dict(nome='s01-seg-clube', olho='Barbearia', titulo='Clube de assinatura <em>com preço e economia.</em>', t=88, cel='barb-cel-clube.png', pe=WA),
 dict(nome='s02-seg-frase-mensalidade', escuro=True, olho='Pagamento único', titulo='Sem entrada. <em>Sem mensalidade.</em>', t=110,
      sub='Você paga uma vez, só depois de aprovar o site pronto. <b>Pix ou cartão parcelado.</b>', pe=WA),
 dict(nome='s03-ter-duvida-dono', escuro=True, olho='Dúvida frequente', titulo='O site fica no nome de quem? <em>No seu.</em>', t=104,
      sub='A publicação é feita em chamada, numa conta sua. <b>E sem mensalidade.</b>', pe=WA),
 dict(nome='s04-ter-p10', olho='Advocacia', titulo='Seu site abre direito <em>no celular?</em>', capa=f'{S}/p10-adv-celular/01.png', pe=PE),
 dict(nome='s05-qua-guia', olho='Advocacia', titulo='O cliente chega no WhatsApp <em>sabendo o que levar.</em>', t=86, cel='adv1-cel-guia3.png', pe=WA),
 dict(nome='s06-qua-r04', olho='Barbearia', titulo='Preço de tudo, <em>num toque só.</em>', t=88, cel='barb-cel-tabela.png', pe=PR),
 dict(nome='s07-qui-frase-landing', escuro=True, olho='Landing page', titulo='Uma página. <em>Um objetivo.</em>', t=110, preco='R$ 399',
      sub='Pronta em até 2 dias úteis. <b>Você só paga depois de aprovar.</b>', pe=WA),
 dict(nome='s08-qui-p11', olho='Antes de escolher', titulo='Landing page ou site? <em>Qual é o seu caso.</em>', t=88, capa=f'{S}/p11-landing-ou-site/01.png', pe=PE),
 dict(nome='s09-sex-bastidor', escuro=True, olho='Como começa', titulo='Você manda o nome. <em>A gente monta o resto.</em>', t=104,
      sub='Em até 2 dias úteis você recebe o link do site pronto pra conferir e pedir até 2 ajustes.', pe=WA),
 dict(nome='s10-sex-p12', olho='Advocacia', titulo='Pode publicar artigo no site? <em>Pode.</em>', t=88, capa=f'{S}/p12-adv-artigo/01.png', pe=PE),
 dict(nome='s11-sab-p13', olho='Barbearia', titulo='Cliente que não acha o preço <em>vai pra outra.</em>', t=88, capa=f'{S}/p13-barb-preco/01.png', pe=PE),
 dict(nome='s12-sab-r05', olho='Advocacia', titulo='Dúvida de INSS? <em>O seu site responde.</em>', t=88, cel='adv2-cel-guia-inss.png', pe=PR),
 dict(nome='s13-dom-equipe', olho='Advocacia', titulo='Equipe com nome e OAB <em>passa confiança.</em>', t=88, cel='adv1-cel-equipe.png', pe=WA),
 dict(nome='s14-dom-antes-depois', olho='Barbearia', titulo='O seu corte <em>vende sozinho.</em>', t=96, cel='barb-cel-antes-depois.png', pe=WA),
]
render(L, f'{S}/stories-2026-10-26')
