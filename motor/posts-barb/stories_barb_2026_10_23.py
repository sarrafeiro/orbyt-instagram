import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
REPO = _os.path.dirname(RAIZ)
PE = 'post novo no perfil · @orbytstudio_'
PR = 'reel novo no perfil · @orbytstudio_'
WA = 'chama no whatsapp · link no perfil'
L = [
 dict(nome='s01-sex-frase-depois', escuro=True, olho='Como funciona', titulo='A gente monta primeiro. <em>Você paga depois.</em>', t=104,
      sub='Em até 2 dias úteis você vê o site pronto num link nosso. <b>Só paga se aprovar.</b>', pe=WA),
 dict(nome='s02-sex-fixado', olho='Barbearia', titulo='Este é o site <em>da sua barbearia.</em>', t=96,
      capa=f'{REPO}/posts/2026-10-20-b02-fixado-barb/01.jpg', pe=PE),
 dict(nome='s03-sab-desculpas', olho='Barbearia', titulo='4 desculpas pra adiar o site. <em>E a resposta.</em>', t=88,
      capa=f'{S}/bb05-desculpas/01.png', pe=PE),
 dict(nome='s04-sab-reel', olho='Antes e depois', titulo='O seu corte <em>vende sozinho.</em>', t=96, cel='barb-cel-antes-depois.png', pe=PR),
 dict(nome='s05-dom-clube', olho='Barbearia', titulo='Clube de assinatura <em>com preço e economia.</em>', t=88, cel='barb-cel-clube.png', pe=WA),
 dict(nome='s06-dom-frase-preco', escuro=True, olho='Preço fechado', titulo='Menos que <em>5 cortes.</em>', t=118, preco='R$ 399',
      sub='Uma vez só, depois de aprovar. <b>Sem entrada e sem mensalidade.</b>', pe=WA),
]
render(L, f'{S}/stories-barb-2026-10-23')
