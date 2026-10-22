import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
_os.environ['ORBYT_HANDLE'] = 'orbytstudio_'
from carrossel import tweet
SLUG = 'bb05-desculpas'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
D = '23 out 2026'
CARDS = [
    dict(tipo='capa', tema='papel', olho='Barbearia', t=96,
         titulo='Barbeiro, 4 desculpas pra adiar o site. <em>E a resposta pra cada uma.</em>',
         visual=tweet('"Depois eu vejo isso do site."', data=D, tam=52), centro=True, ponto=False),
    dict(olho='Desculpa 1', titulo='"Já tenho Instagram."',
         visual=tweet('O Instagram mostra o dia a dia. <em>O site mostra preço, clube e agenda</em> pra quem te achou no Google.', data=D), centro=True, ponto=False),
    dict(tema='escuro', olho='Desculpa 2', titulo='"Site é caro."',
         visual=tweet('Site com modelo de barbearia: <em>R$ 399, uma vez só.</em> Menos que 9 cortes de R$ 45.', data=D), centro=True, ponto=False),
    dict(olho='Desculpa 3', titulo='"Não tenho tempo pra isso."',
         visual=tweet('Você manda o nome da barbearia e responde um formulário curto. <em>O resto é com a gente.</em>', data=D), centro=True, ponto=False),
    dict(tema='laranja', olho='Desculpa 4', titulo='"E se ficar ruim?"',
         visual=tweet('Você vê o site pronto num link nosso, pede até 2 ajustes e <em>só paga se aprovar.</em>', data=D), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
