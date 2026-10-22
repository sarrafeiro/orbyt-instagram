import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, pagamento
SLUG = 'bbr-b02-fixado-barb'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Site para barbearia', t=98,
         titulo='Barbeiro, este é o site da <em>sua barbearia.</em>',
         texto='<b>Pronto em até 2 dias úteis. Você só paga depois de aprovar.</b>',
         visual=cel('barb-cel-capa.png', ch=650) + cel('barb-cel-clube.png', ch=650)),
    dict(olho='Primeira tela', titulo='Sua marca e o botão Agendar <em>logo de cara.</em>',
         texto='O Agendar leva pro app que você já usa ou direto pro seu WhatsApp.',
         visual=navegador('barb-desk-capa.png', 'suabarbearia.com.br')),
    dict(olho='Clube de assinatura', titulo='Seus planos com <em>preço e economia.</em>',
         texto='Quem assina volta todo mês. O site mostra quanto o cliente economiza.',
         visual=navegador('barb-desk-clube.png', 'suabarbearia.com.br')),
    dict(olho='Serviços', titulo='O preço de cada serviço, <em>num toque.</em>',
         texto='Os mais pedidos em destaque e a tabela completa com busca.',
         visual=cel('barb-cel-servicos.png', ch=640) + cel('barb-cel-tabela.png', ch=640)),
    dict(olho='Antes e depois', titulo='Seus cortes <em>em antes e depois.</em>',
         texto='O cliente arrasta com o dedo e vê a diferença.',
         visual=cel('barb-cel-antes-depois.png', ch=720)),
    dict(olho='Dúvidas', titulo='As perguntas de sempre <em>respondidas no site.</em>',
         texto='Precisa agendar? Como funciona o clube? Tem estacionamento? Menos mensagem repetida no seu WhatsApp.',
         visual=cel('barb-cel-duvidas.png', ch=680)),
    dict(olho='Como funciona', titulo='A gente monta primeiro. <em>Você paga depois.</em>',
         texto='Você confere o site pronto num link nosso e pede até 2 ajustes. Aprovou? Paga uma vez, no Pix ou no cartão parcelado.',
         visual=pagamento(), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Sua barbearia com site e agenda online.',
         preco='R$ 399', preco_nota='preço fechado<br>pagamento único',
         checks=['Pronto em até 2 dias úteis', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'],
         cta=CTA_BARB),
]
