import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
PE = 'post novo no perfil · @orbyt_studio'
PR = 'reel novo no perfil · @orbyt_studio'
WA = 'chama no whatsapp · link no perfil'
L = [
 dict(nome='s01-seg-frase-prazo', escuro=True, olho='Prazo', titulo='Pediu hoje? <em>Em 2 dias úteis está pronto.</em>', t=100,
      sub='Site com modelo de advocacia, R$&nbsp;797. <b>Você só paga depois de aprovar.</b>', pe=WA),
 dict(nome='s02-seg-p18', olho='Advocacia', titulo='Ele achou você no Google. <em>E não achou mais nada.</em>', t=84, capa=f'{S}/p18-adv-google-sem-site/01.png', pe=PE),
 dict(nome='s03-ter-areas', olho='Advocacia', titulo='Áreas explicadas <em>na língua do cliente.</em>', t=88, cel='adv1-cel-areas.png', pe=WA),
 dict(nome='s04-ter-r08', olho='Advocacia', titulo='Plano de saúde negou? <em>O seu site explica.</em>', t=88, cel='adv2-cel-guia-consumidor.png', pe=PR),
 dict(nome='s05-qua-frase-sozinho', escuro=True, olho='Dúvida frequente', titulo='Atende escritório pequeno? <em>Advogado sozinho também.</em>', t=96,
      sub='Landing page R$&nbsp;399 ou site com modelo R$&nbsp;797. <b>Você só paga depois de aprovar.</b>', pe=WA),
 dict(nome='s06-qua-p19', olho='Como funciona', titulo='Você aprovou o site. <em>E agora?</em>', t=96, capa=f'{S}/p19-depois-aprovar/01.png', pe=PE),
 dict(nome='s07-qui-guia', olho='Advocacia', titulo='O cliente escolhe o assunto <em>em 3 cliques.</em>', t=86, cel='adv1-cel-guia2.png', pe=WA),
 dict(nome='s08-qui-p20', olho='Salva esse', titulo='O que o cliente quer ver <em>antes de ligar.</em>', t=86, capa=f'{S}/p20-antes-de-ligar/01.png', pe=PE),
 dict(nome='s09-sex-frase-ver-pronto', escuro=True, olho='Como funciona', titulo='Você vê o site pronto <em>antes de decidir.</em>', t=100,
      sub='Num link nosso, no celular e no computador. <b>R$&nbsp;0 pra começar.</b>', pe=WA),
 dict(nome='s10-sex-p21', olho='Advocacia', titulo='Nunca teve site? <em>Começa por aqui.</em>', t=96, capa=f'{S}/p21-primeiro-site/01.png', pe=PE),
 dict(nome='s11-sab-guia1', olho='Advocacia', titulo='Um guia que organiza <em>o primeiro contato.</em>', t=86, cel='adv1-cel-guia1.png', pe=WA),
 dict(nome='s12-sab-r09', olho='Advocacia', titulo='"Quem vai me atender?" <em>O seu site mostra.</em>', t=86, cel='adv1-cel-equipe.png', pe=PR),
 dict(nome='s13-dom-frase-provimento', escuro=True, olho='Provimento 205/2021', titulo='Informar pode. <em>Prometer resultado, não.</em>', t=100,
      sub='O nosso modelo de advocacia <b>já vem dentro das regras.</b>', pe=WA),
 dict(nome='s14-dom-guia3', olho='Advocacia', titulo='Domingo à noite <em>alguém pesquisa o seu nome.</em>', t=86, cel='adv1-cel-guia3.png', pe=WA),
]
render(L, f'{S}/stories-2026-11-02')
