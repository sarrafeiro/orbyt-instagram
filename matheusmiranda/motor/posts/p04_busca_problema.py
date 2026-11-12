import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import numero, busca
SLUG = 'p04-busca-problema'
CARDS = [
    dict(tema='escuro', olho='Salva esse', titulo='Ninguém procura <em>teu produto</em> no Google.', ponto=False, t=132),
    dict(olho='Meu app de receitas', titulo='"App de receitas"',
         visual=numero('320', 'buscas por mês no Brasil', tam=190), centro=True, ponto=False),
    dict(tema='papel', olho='Agora o problema', titulo='"Bolo sem ovo"',
         visual=numero('33.100', 'buscas por mês no Brasil', tam=170), centro=True, ponto=False),
    dict(tema='destaque', olho='A regra', titulo='As pessoas buscam o problema. <em>Não a solução.</em>', ponto=False, t=96),
    dict(olho='Na prática', titulo='Fala a língua <em>da busca.</em>',
         visual=busca('strogonoff sem creme de leite', [('bom', 'Página da receita resolvendo isso', 'é o que o Google mostra'), ('ruim', 'Página falando do app', 'ninguém digitou isso')]), ponto=False),
    dict(tema='papel', olho='O que eu vou fazer', titulo='Uma página <em>por prato.</em>',
         visual=numero('5', 'páginas no ar, medindo por 12 semanas', tam=190), centro=True, ponto=False),
    dict(tipo='final', olho='Sua vez', t=84, titulo='O que teu cliente digita no Google?',
         preco='1', preco_nota='busca<br>por página',
         checks=['Busca do problema', 'Página que resolve', 'Produto no fim', 'Medir antes de escalar'],
         cta='Me fala o teu nicho que eu te digo o que ele busca. <b>Comenta aqui.</b>'),
]
