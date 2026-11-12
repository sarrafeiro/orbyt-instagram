import sys; sys.path.insert(0,'/home/claude/insta-pessoal/v2')
from v2 import busca
SLUG='p04-busca-problema-v2'
CARDS=[
 dict(fundo='escuro', titulo='Ninguém procura <b>teu produto</b> no Google.', pilula='Salva esse', t=112),
 dict(pre='Quantas vezes o Brasil busca<br>"app de receitas" por mês?', num='320', pilula='buscas por mês'),
 dict(pre='E "bolo sem ovo"?', num='33.100', n=250, pilula='buscas por mês'),
 dict(fundo='escuro', titulo='As pessoas buscam <b>o problema.</b> Não a solução.', t=108),
 dict(titulo='Fala a língua <b>da busca.</b>', t=96, visual=busca('strogonoff sem creme de leite',[('bom','A receita que resolve isso'),('ruim','A página falando do app')])),
 dict(titulo='Uma página <b>por prato.</b>', t=96, num='5', pilula='páginas no ar, medindo por 12 semanas'),
 dict(fundo='escuro', titulo='O que teu cliente <b>digita no Google?</b>', pilula='Comenta teu nicho', t=104),
]
