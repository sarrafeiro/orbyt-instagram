import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import numero, checklist, lista, conversa
SLUG = 'p02-resumir-curso'
CARDS = [
    dict(tema='escuro', olho='Salva esse', titulo='Curso parado? <em>A IA assiste por você.</em>',
         visual=numero('54 → 1', '54 aulas viraram uma página de plano de ação', tam=190), centro=True, ponto=False),
    dict(olho='Passo 1', titulo='Veja se as aulas têm <em>legenda.</em>',
         texto='Quase toda plataforma de curso gera legenda automática. A legenda é o texto inteiro da aula. Sem ela, você vai precisar transcrever o áudio.', ponto=False,
         visual=numero('CC', 'o botão de legenda no player', tam=190), centro=True),
    dict(tema='papel', olho='Passo 2', titulo='Junte tudo num <em>texto só.</em>',
         texto='Uma aula embaixo da outra, com o título de cada uma. É isso que a IA vai ler.',
         visual=checklist(['Título da aula', 'Texto da legenda', 'Próxima aula'], marcados=3), centro=True, ponto=False),
    dict(olho='Passo 3', titulo='Conte pra IA <em>quem é você.</em>',
         texto='Sem contexto, ela faz resumo genérico. Com contexto, ela filtra o que serve pro seu negócio.',
         visual=conversa('Assistente de IA', [('eu', 'Eu vendo pra empresa e tenho 3 produtos digitais. Quero crescer no Instagram.', '09:12'), ('ela', 'Entendido. Vou ler as aulas pensando nisso.', '09:12')]), ponto=False),
    dict(tema='destaque', olho='Passo 4, copia esse pedido', t=78, titulo='"Me diz o que aqui serve pro meu caso, o que é enrolação e o que eu faço primeiro."',
         texto='Peça nota por aula e um plano em ordem de prioridade.', ponto=False),
    dict(olho='O que eu recebi', titulo='Só 30% <em>prestava.</em>',
         visual=lista([('As aulas que valem rever', '12 de 54'), ('O que é enrolação', 'e por quê'), ('Plano de ação', 'em ordem, pra começar amanhã')], 'num'), centro=True, ponto=False),
    dict(tipo='final', olho='Resumo', t=80, titulo='Uma manhã no lugar de 10 horas.',
         preco='4', preco_nota='passos<br>pra salvar',
         checks=['Legenda das aulas', 'Tudo num texto só', 'Contexto do seu negócio', 'Pedido de prioridade'],
         cta='Qual curso parado você vai resumir primeiro? <b>Me conta nos comentários.</b>'),
]
