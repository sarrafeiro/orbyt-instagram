import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import conversa
SLUG = 'bb04-duvidas'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
def qa(p, r): return conversa('Orbyt Studio', [('eu', p, '09:12'), ('ela', r, '09:13')])
CARDS = [
    dict(tipo='capa', olho='Antes de pedir o seu site', t=100,
         titulo='As 6 dúvidas de todo barbeiro. <em>Respondidas.</em>',
         texto='Salva pra consultar quando for pedir o seu.',
         visual=qa('Quanto eu pago pra começar?', 'Nada. R$ 0. Você só paga depois de aprovar o site pronto.'), centro=True, ponto=False),
    dict(olho='Dúvida 1', titulo='Já tenho o link do app. <em>Preciso de site?</em>',
         visual=qa('Já uso app de agenda. Preciso de site?', 'O app agenda. O site vende: mostra preço, clube e o seu trabalho pra quem ainda não te conhece.'), centro=True, ponto=False),
    dict(olho='Dúvida 2', titulo='Não uso app. <em>Funciona?</em>',
         visual=qa('Não uso app de agendamento. Dá certo?', 'Dá. O botão Agendar do site leva direto pro seu WhatsApp.'), centro=True, ponto=False),
    dict(olho='Dúvida 3', titulo='E se eu não gostar? <em>Você não paga.</em>',
         visual=qa('E se o site não ficar do jeito que eu quero?', 'Você vê o site pronto num link nosso e pode pedir até 2 ajustes. Só paga se aprovar.'), centro=True, ponto=False),
    dict(olho='Dúvida 4', titulo='Não tenho foto boa. <em>E agora?</em>',
         visual=qa('Não tenho foto boa da barbearia.', 'Sem problema. A gente começa com foto de exemplo e troca pelas suas quando você mandar.'), centro=True, ponto=False),
    dict(olho='Dúvida 5', titulo='Tem mensalidade? <em>Não.</em>',
         visual=qa('Vou pagar todo mês?', 'Não. Você paga uma vez, depois de aprovar, no Pix ou no cartão parcelado.'), centro=True, ponto=False),
    dict(olho='Dúvida 6', titulo='O site fica no nome de quem? <em>No seu.</em>',
         visual=qa('O site é meu mesmo?', 'É. Depois do pagamento a gente publica com você, em chamada, numa conta que é sua.'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
