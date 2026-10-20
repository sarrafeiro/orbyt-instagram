import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import conversa
SLUG = 'n2-duvidas-adv'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
def qa(p, r): return conversa('Orbyt Studio', [('eu', p, '09:12'), ('ela', r, '09:13')])
CARDS = [
    dict(tipo='capa', olho='Antes de pedir o site', t=100,
         titulo='Advogado, as 6 dúvidas de sempre. <em>Respondidas.</em>',
         texto='Salva pra consultar quando for pedir o do seu escritório.',
         visual=qa('Quanto eu pago pra começar?', 'Nada. R$ 0. Você só paga depois de aprovar o site pronto.'), ponto=False),
    dict(olho='Dúvida 1', titulo='A OAB deixa ter site? <em>Deixa.</em>',
         visual=qa('Advogado pode ter site?', 'Pode. O Provimento 205/2021 permite site com áreas de atuação, equipe e conteúdo informativo. O que não pode é prometer resultado.'), centro=True, ponto=False),
    dict(olho='Dúvida 2', titulo='E se eu não gostar? <em>Você não paga.</em>',
         visual=qa('E se o site não ficar do jeito que eu quero?', 'Você vê o site pronto num link nosso e pode pedir até 2 ajustes. Só paga se aprovar.'), centro=True, ponto=False),
    dict(olho='Dúvida 3', titulo='Fica pronto em quanto tempo?',
         visual=qa('Demora quanto?', 'Com o modelo de advocacia, em até 2 dias úteis. Site 100% personalizado, em até 5 dias úteis.'), centro=True, ponto=False),
    dict(olho='Dúvida 4', titulo='Tem mensalidade? <em>Não.</em>',
         visual=qa('Como eu pago?', 'Uma vez só, depois de aprovar, no Pix ou no cartão parcelado. Sem entrada e sem mensalidade.'), centro=True, ponto=False),
    dict(olho='Dúvida 5', titulo='O site fica no nome de quem? <em>No seu.</em>',
         visual=qa('O site é do escritório mesmo?', 'É. Depois do pagamento a gente publica com você, em chamada, numa conta que é sua.'), centro=True, ponto=False),
    dict(olho='Dúvida 6', titulo='Preciso cuidar de alguma coisa? <em>Quase nada.</em>',
         visual=qa('Não tenho tempo pra isso.', 'Você manda o nome do escritório e responde um formulário curto. O resto é com a gente.'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
