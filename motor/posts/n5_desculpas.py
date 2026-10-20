import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tweet
SLUG = 'n5-desculpas'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', tema='papel', olho='Advocacia', t=96,
         titulo='4 desculpas pra adiar o site. <em>E a resposta pra cada uma.</em>',
         visual=tweet('"Depois eu vejo isso do site."', tam=52), centro=True, ponto=False),
    dict(olho='Desculpa 1', titulo='"Não tenho tempo pra cuidar disso."',
         visual=tweet('Você manda o nome do escritório e responde um formulário curto. <em>O resto é com a gente.</em>'), centro=True, ponto=False),
    dict(tema='escuro', olho='Desculpa 2', titulo='"Site é caro."',
         visual=tweet('Site com modelo de advocacia: <em>R$ 797, uma vez só.</em> Sem entrada e sem mensalidade.'), centro=True, ponto=False),
    dict(olho='Desculpa 3', titulo='"Não sei se a OAB deixa."',
         visual=tweet('Deixa. O site segue o <em>Provimento 205/2021</em>: conteúdo informativo, áreas, equipe e contato. Sem promessa de resultado.'), centro=True, ponto=False),
    dict(tema='laranja', olho='Desculpa 4', titulo='"E se ficar ruim?"',
         visual=tweet('Você vê o site pronto num link nosso, pede até 2 ajustes e <em>só paga se aprovar.</em>'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
