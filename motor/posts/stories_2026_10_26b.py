import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
PE = 'post novo no perfil · @orbyt_studio'
PR = 'reel novo no perfil · @orbyt_studio'
WA = 'chama no whatsapp · link no perfil'
L = [
 dict(nome='s01-seg-frase-pix', escuro=True, olho='Pagamento', titulo='Pix ou cartão parcelado. <em>Só depois de aprovar.</em>', t=100,
      sub='Uma vez só. <b>Sem entrada e sem mensalidade.</b>', pe=WA),
 dict(nome='s02-seg-duvidas', olho='Advocacia', titulo='As dúvidas do cliente <em>respondidas antes do contato.</em>', t=84, cel='adv1-cel-duvidas.png', pe=WA),
 dict(nome='s03-ter-duvida-ajuste', escuro=True, olho='Dúvida frequente', titulo='Posso pedir ajuste? <em>Até 2, antes de pagar.</em>', t=104,
      sub='Você confere o site pronto num link nosso. <b>Nada vai pro ar sem o seu ok.</b>', pe=WA),
 dict(nome='s04-ter-p14', olho='Advocacia', titulo='5 erros no site <em>que espantam cliente.</em>', t=88, capa=f'{S}/p14-adv-5erros/01.png', pe=PE),
 dict(nome='s05-qua-frase-personalizado', escuro=True, olho='Site 100% personalizado', titulo='Do seu jeito, <em>do zero.</em>', t=120,
      sub='A partir de R$&nbsp;1.497, pronto em até 5 dias úteis. <b>Você só paga depois de aprovar.</b>', pe=WA),
 dict(nome='s06-qua-r06', olho='Advocacia', titulo='Dúvida de divórcio? <em>O seu site explica.</em>', t=88, cel='adv1-cel-guia-familia.png', pe=PR),
 dict(nome='s07-qui-frase-brasil', escuro=True, olho='Base em BH', titulo='Atendemos escritórios <em>do Brasil todo.</em>', t=104,
      sub='Tudo pelo WhatsApp e por chamada. <b>O site fica numa conta sua.</b>', pe=WA),
 dict(nome='s08-qui-p15', olho='Como funciona', titulo='Por que a gente monta <em>antes de você pagar?</em>', t=86, capa=f'{S}/p15-monta-antes/01.png', pe=PE),
 dict(nome='s09-sex-guia', olho='Advocacia', titulo='Ele chega no WhatsApp <em>com a mensagem pronta.</em>', t=86, cel='adv2-cel-guia3.png', pe=WA),
 dict(nome='s10-sex-p16', olho='Provimento 205/2021', titulo='Áreas de atuação <em>sem ferir o Código de Ética.</em>', t=84, capa=f'{S}/p16-adv-areas/01.png', pe=PE),
 dict(nome='s11-sab-p17', olho='Advocacia', titulo='4 frases que todo advogado <em>fala do site.</em>', t=86, capa=f'{S}/p17-adv-objecoes/01.png', pe=PE),
 dict(nome='s12-sab-r07', olho='Advocacia', titulo='Em audiência? <em>O seu site responde.</em>', t=90, cel='adv1-cel-conteudo.png', pe=PR),
 dict(nome='s13-dom-capa', olho='Advocacia', titulo='O seu escritório <em>no celular do cliente.</em>', t=88, cel='adv2-cel-capa.png', pe=WA),
 dict(nome='s14-dom-frase-escolher', escuro=True, olho='Landing page ou site', titulo='Não sabe qual? <em>A gente te ajuda a escolher.</em>', t=100,
      sub='Landing page R$&nbsp;399, site com modelo R$&nbsp;797. <b>Chama no WhatsApp e conta o que você precisa.</b>', pe=WA),
]
render(L, f'{S}/stories-2026-10-26b')
