import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero
SLUG = 'n1-como-funciona'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='texto', tema='laranja', selo='Como funciona', t=128,
         titulo='R$ 0 pra começar. <em>Você só paga depois de aprovar.</em>',
         rodape='Site para advogados · 5 passos'),
    dict(tema='escuro', olho='Passo 1', titulo='Você manda o nome do escritório no WhatsApp.',
         texto='Assina um termo sem pagar nada e responde um formulário curto.',
         visual=conversa('Orbyt Studio', [('eu', 'Oi! Quero o site do Andrade & Ferraz Advocacia.', '09:12'), ('ela', 'Fechado. Em até 2 dias úteis te mando o site pronto pra conferir.', '09:14')])),
    dict(olho='Passo 2', titulo='Em até 2 dias úteis o site fica pronto.',
         texto='No modelo de advocacia, com as suas áreas, a sua equipe e o guia por assunto.',
         visual=cel('adv2-cel-capa.png', ch=620) + cel('adv2-cel-guia3.png', ch=620)),
    dict(tema='papel', olho='Passo 3', titulo='Você confere tudo <em>num link nosso.</em>',
         texto='Pode pedir até 2 ajustes. Nada vai pro ar sem o seu ok.',
         visual=navegador('adv2-desk-capa.png', 'orbytstudio.com.br · prévia do seu site')),
    dict(tema='laranja', olho='Passo 4', titulo='Aprovou? <em>Só agora você paga.</em>',
         visual=numero('R$ 797', 'Uma vez só, no Pix ou no cartão parcelado. Sem mensalidade.', tam=230), centro=True, ponto=False),
    dict(olho='Passo 5', titulo='A gente publica com você, <em>em chamada.</em>',
         texto='Numa conta que é sua. O site fica no seu nome.',
         visual=cel('adv1-cel-areas.png', chip='no ar', ch=640)),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
