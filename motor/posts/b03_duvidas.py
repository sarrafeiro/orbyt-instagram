import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import conversa
SLUG = 'b03-duvidas'
def qa(p, r): return conversa('Orbyt Studio', [('eu', p, '09:12'), ('ela', r, '09:13')])
CARDS = [
    dict(tipo='capa', olho='Antes de pedir o seu site', t=100,
         titulo='As 6 dúvidas que todo mundo tem. <em>Respondidas.</em>',
         texto='Salva pra consultar quando for pedir o seu.',
         visual=qa('Quanto eu pago pra começar?', 'Nada. R$ 0. Você só paga depois de aprovar o site pronto.'), centro=True, ponto=False),
    dict(olho='Dúvida 1', titulo='Preciso pagar pra começar? <em>Não.</em>',
         visual=qa('Tem entrada ou sinal?', 'Não. Você assina um termo, sem pagar nada, e responde um formulário com as informações do seu negócio.'), centro=True, ponto=False),
    dict(olho='Dúvida 2', titulo='E se eu não gostar? <em>Você não paga.</em>',
         visual=qa('E se o site não ficar do jeito que eu quero?', 'Você vê o site pronto num link nosso e pode pedir até 2 ajustes. Só paga se aprovar.'), centro=True, ponto=False),
    dict(olho='Dúvida 3', titulo='Fica pronto em quanto tempo?',
         visual=qa('Demora quanto?', 'Landing page e site com modelo do seu segmento: até 2 dias úteis. Site 100% personalizado: até 5 dias úteis.'), centro=True, ponto=False),
    dict(olho='Dúvida 4', titulo='Como eu pago? <em>Uma vez só.</em>',
         visual=qa('Tem mensalidade?', 'Não. Você paga uma vez, depois de aprovar, no Pix ou no cartão parcelado.'), centro=True, ponto=False),
    dict(olho='Dúvida 5', titulo='O site fica no nome de quem? <em>No seu.</em>',
         visual=qa('O site é meu mesmo?', 'É. Depois do pagamento a gente publica com você, em chamada, numa conta que é sua.'), centro=True, ponto=False),
    dict(olho='Dúvida 6', titulo='Preciso entender de site? <em>Não.</em>',
         visual=qa('Eu não entendo nada de site. Tem problema?', 'Nenhum. Você manda o nome do seu negócio no WhatsApp e responde o formulário. O resto é com a gente.'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site com modelo do seu segmento.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Pronto em até 2 dias úteis', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Manda o nome do seu escritório ou da sua barbearia no WhatsApp. <b>O link está no perfil.</b>'),
]
