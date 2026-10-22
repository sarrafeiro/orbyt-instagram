import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero
SLUG = 'bb01-como-funciona'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='texto', tema='laranja', selo='Como funciona', t=128,
         titulo='R$ 0 pra começar. <em>Você só paga depois de aprovar.</em>',
         rodape='Site para barbearia · 5 passos'),
    dict(tema='escuro', olho='Passo 1', titulo='Você manda o nome da barbearia no WhatsApp.',
         texto='Assina um termo sem pagar nada e responde um formulário curto.',
         visual=conversa('Orbyt Studio', [('eu', 'Oi! Quero o site da Sua Barbearia, lá do Centro.', '09:12'), ('ela', 'Fechado. Em até 2 dias úteis te mando o site pronto pra conferir.', '09:14')])),
    dict(olho='Passo 2', titulo='Em até 2 dias úteis o site fica pronto.',
         texto='Com a sua marca, os seus serviços, o clube e o antes e depois dos seus cortes.',
         visual=cel('barb-cel-capa.png', ch=620) + cel('barb-cel-clube.png', ch=620)),
    dict(tema='papel', olho='Passo 3', titulo='Você confere tudo <em>num link nosso.</em>',
         texto='Pode pedir até 2 ajustes. Nada vai pro ar sem o seu ok.',
         visual=navegador('barb-desk-capa.png', 'orbytstudio.com.br · prévia do seu site')),
    dict(tema='laranja', olho='Passo 4', titulo='Aprovou? <em>Só agora você paga.</em>',
         visual=numero('R$ 399', 'Uma vez só, no Pix ou no cartão parcelado. Sem mensalidade.', tam=195), centro=True, ponto=False),
    dict(olho='Passo 5', titulo='A gente publica com você, <em>em chamada.</em>',
         texto='Numa conta que é sua. O site fica no seu nome.',
         visual=cel('barb-cel-servicos.png', chip='no ar', ch=640)),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
