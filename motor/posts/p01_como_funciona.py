import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, pagamento

SLUG = 'p01-como-funciona'
CARDS = [
    dict(tipo='capa', olho='Sites para advocacia e barbearia', t=104, s=46,
         titulo='Seu site no ar em até 2 dias úteis.',
         texto='<b>E você só paga depois de aprovar.</b>',
         visual=cel('adv2-cel-capa.png', ch=690) + cel('barb-cel-capa.png', ch=690)),
    dict(olho='Passo 1', titulo='Você manda o nome do seu negócio no WhatsApp.',
         texto='Escritório ou barbearia. Pra começar, você não paga nada.',
         visual=conversa('Orbyt Studio', [
             ('eu', 'Oi! Quero um site pro meu escritório: Andrade & Ferraz Advocacia.', '09:12'),
             ('ela', 'Fechado! Em até 2 dias úteis te mando o site pronto pra você conferir.', '09:14')])),
    dict(olho='Passo 2', titulo='A gente monta o site no modelo do seu segmento.',
         texto='Com a sua marca, os seus serviços e o WhatsApp em cada parte da página.',
         visual=cel('adv1-cel-guia3.png', ch=640) + cel('barb-cel-clube.png', ch=640)),
    dict(olho='Passo 3', titulo='Você confere tudo <em>num link nosso.</em>',
         texto='Dá pra pedir até 2 ajustes. Nada vai pro ar sem o seu ok.',
         visual=cel('barb-cel-servicos.png', chip='link de aprovação', ch=720)),
    dict(olho='Passo 4', titulo='Aprovou? <em>Só agora</em> você paga.',
         texto='Uma vez só, no Pix ou no cartão parcelado. Sem entrada e sem mensalidade.',
         visual=pagamento(), centro=True, ponto=False),
    dict(olho='Passo 5', titulo='A gente publica o site no seu nome.',
         texto='Em chamada, numa conta que é sua. O site fica com você.',
         visual=navegador('adv2-desk-capa.png', 'andradeferraz.adv.br')),
    dict(tipo='final', olho='Quanto custa', t=84,
         titulo='Site com modelo do seu segmento.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Pronto em até 2 dias úteis', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Manda o nome do seu escritório ou da sua barbearia no WhatsApp. <b>O link está no perfil.</b>'),
]
