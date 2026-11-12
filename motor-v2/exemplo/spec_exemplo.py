import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from carrossel_v2 import fluxo, busca
SLUG = 'exemplo'
CARDS = [
 dict(fundo='escuro', titulo='Gancho curto com <b>a palavra que importa.</b>', pilula='Salva esse', t=110),
 dict(pre='Pergunta curta', num='320', pilula='rótulo do número'),
 dict(fundo='destaque', titulo='Uma ideia <b>por card.</b>', t=110),
 dict(titulo='Processo <b>em passos.</b>', t=100, visual=fluxo(['Passo 1','Passo 2','Resultado'])),
 dict(titulo='Antes de clicar, <b>ele busca.</b>', t=96, visual=busca('termo que o cliente digita',[('bom','Página que resolve'),('ruim','Página que só vende')])),
 dict(fundo='escuro', titulo='Pergunta final <b>pra comentar?</b>', pilula='Comenta aqui', t=100),
]
