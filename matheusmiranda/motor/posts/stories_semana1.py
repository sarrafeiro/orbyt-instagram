import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
S = RAIZ + '/saida'
PE = 'post novo no perfil'
L = [
 dict(nome='qui-1-frase', escuro=True, olho='Novidade', titulo='Vou começar a mostrar aqui como eu <em>uso IA pra trabalhar.</em>', t=96, sub='Sem enrolação. <b>Na prática.</b>', pe='@matheusmiranda.ia'),
 dict(nome='qui-2-capa', olho='Minha história', titulo='12 anos vendendo. <em>Agora eu construo com IA.</em>', t=86, capa=f'{S}/p01-estreia/01.png', pe=PE),
 dict(nome='sex-1-frase', escuro=True, olho='Me responde aqui', titulo='O que você <em>nunca</em> deixaria a IA fazer no seu trabalho?', t=96, sub='Hoje eu conto o que <b>eu não entrego de jeito nenhum.</b>', pe='responde esse story'),
 dict(nome='sab-1-frase', escuro=True, olho='Confissão', titulo='Comprei um curso de 54 aulas e <em>não assisti nenhuma.</em>', t=96, sub='Reel novo no perfil.', pe=PE),
 dict(nome='sab-2-frase', olho='Spoiler', titulo='Só <em>30%</em> do curso prestava.', t=120, sub='A IA leu as 54 aulas e me falou <b>o que fazer primeiro.</b>', pe=PE),
 dict(nome='dom-1-capa', olho='Pra salvar', titulo='Como resumir um curso inteiro <em>com IA.</em>', t=86, capa=f'{S}/p02-resumir-curso/01.png', pe=PE),
 dict(nome='dom-2-frase', escuro=True, olho='Semana 1', titulo='O que você quer ver <em>aqui na próxima semana?</em>', t=96, sub='Me manda no direct. <b>Eu leio todas.</b>', pe='responde esse story'),
]
render(L, f'{S}/stories-semana1')
