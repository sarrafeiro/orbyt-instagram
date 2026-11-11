import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import numero, lista, tweet
SLUG = 'p01-estreia'
CARDS = [
    dict(tipo='texto', tema='destaque', selo='Prazer, Matheus', t=128,
         titulo='12 anos vendendo. <em>Agora eu construo com IA.</em>', rodape='minha história · 8 cards'),
    dict(tema='escuro', olho='2013', titulo='Comecei vendendo <em>imóvel.</em>',
         texto='Na Lopes, fiquei entre os 5 melhores de mais de 400 consultores. Depois virei gerente de uma equipe de até 20 pessoas.',
         visual=numero('TOP 5', 'entre mais de 400 consultores', tam=180), centro=True, ponto=False),
    dict(olho='2019 a 2022', titulo='Depois, venda de <em>software.</em>',
         texto='Venda consultiva pra empresa, com meta todo mês.',
         visual=lista([('Sólides', 'cerca de 270% da meta no onboarding'), ('Take Blip', 'SaaS e comunicação'), ('Lojacorr', 'mais de 120% da meta por sete meses')], 'num'), centro=True, ponto=False),
    dict(tema='papel', olho='2023 a 2025', titulo='Montei uma área comercial <em>do zero.</em>',
         texto='Na PAAG, como Head Comercial: mais de 100 parcerias. Participei de um crescimento de receita que passou de 4.000% em cerca de 14 meses.',
         visual=numero('+4.000%', 'de receita em cerca de 14 meses', tam=165), centro=True, ponto=False),
    dict(tipo='texto', tema='escuro', t=110, titulo='Essas viagens que vocês viam aqui? <em>Quase todas a trabalho.</em>',
         rodape='vender pra empresa me levou longe'),
    dict(olho='A virada', titulo='Aí a IA entrou na <em>rotina.</em>',
         texto='E eu vi que dava pra fazer sozinho o que antes precisava de um time inteiro.',
         visual=tweet('Proposta, resumo de reunião, pesquisa e roteiro: a IA faz o primeiro rascunho. <em>Quem decide sou eu.</em>'), centro=True, ponto=False),
    dict(tema='papel', olho='Hoje', titulo='Abri a OrbitTech com <em>meu sócio.</em>',
         texto='Uma software house de IA. Os produtos no ar:',
         visual=lista([('MedQueen', 'IA de estudo pra estudante de Medicina'), ('NuPrato', 'fala o prato e a IA adapta pra sua cozinha'), ('PromoSnap', 'promosnap.com.br')], 'num'), centro=True, ponto=False),
    dict(tipo='final', olho='O que vem por aí', t=80, titulo='IA na prática pra quem vende e toca negócio.',
         preco='IA', preco_nota='na prática<br>sem enrolação',
         checks=['Como eu uso IA pra vender', 'Ferramenta testada de verdade', 'O que deu errado também', 'Bastidor dos meus produtos'],
         cta='Se você vende ou tem negócio, <b>segue @matheusmiranda.ia</b>'),
]
