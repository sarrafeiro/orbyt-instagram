import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero, busca, lista, tweet as _tw
def tweet(t, tam=None): return _tw(t, data='6 nov 2026', tam=tam)
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
FINAL = dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV)
SLUG = 'p21-primeiro-site'
CARDS = [
    dict(tipo='capa', tema='escuro', olho='Advocacia', t=94,
         titulo='Nunca teve site? <em>As 5 perguntas de quem vai começar.</em>',
         visual=tweet('"Nunca tive site. Nem sei por onde começar."', tam=52), centro=True, ponto=False),
    dict(olho='Pergunta 1', titulo='"Não entendo nada <em>de site."</em>',
         visual=tweet('Não precisa. Você manda o nome do escritório e responde um formulário curto. <em>O resto é com a gente.</em>'), centro=True, ponto=False),
    dict(tema='papel', olho='Pergunta 2', titulo='"Vou ficar preso <em>numa mensalidade?"</em>',
         visual=tweet('Não. Você <em>paga uma vez</em>, no Pix ou no cartão parcelado, e só depois de aprovar.'), centro=True, ponto=False),
    dict(tema='escuro', olho='Pergunta 3', titulo='"O site fica <em>no nome de quem?"</em>',
         visual=tweet('No seu. A gente publica com você, em chamada, <em>numa conta do escritório.</em>'), centro=True, ponto=False),
    dict(olho='Pergunta 4', titulo='"Só preciso de <em>uma página."</em>',
         visual=tweet('Então é landing page: <em>R$ 399</em>, preço fechado, pronta em até 2 dias úteis.'), centro=True, ponto=False),
    dict(tema='laranja', olho='Pergunta 5', titulo='"Quero algo <em>só meu."</em>',
         visual=tweet('Site 100% personalizado a partir de <em>R$ 1.497</em>, em até 5 dias úteis.'), centro=True, ponto=False),
    FINAL,
]
