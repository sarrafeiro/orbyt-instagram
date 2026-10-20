import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, applink
SLUG = 'p06-barb-link-app'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Barbearia', t=92,
         titulo='Barbeiro, o link do app de agendamento <em>não é o seu site.</em>',
         texto='Ele marca horário. Mas não mostra por que o cliente deveria escolher você.',
         visual=applink(ch=600, chip='link do app') + cel('barb-cel-capa.png', chip='seu site', ch=600)),
    dict(olho='O link do app', titulo='No link do app, você é mais um na lista.',
         texto='O mesmo layout de todo mundo: sem a sua marca, sem foto do seu trabalho, sem a sua história.',
         visual=applink(ch=700, chip='link do app')),
    dict(olho='O seu site', titulo='No seu site, o cliente vê a sua barbearia.',
         texto='Sua marca, suas cores e o seu espaço logo na primeira tela.',
         visual=cel('barb-cel-capa.png', ch=720)),
    dict(olho='Clube de assinatura', titulo='Seus planos com preço e economia na cara.',
         texto='Quem assina volta todo mês. O site mostra por que vale a pena.',
         visual=cel('barb-cel-clube.png', ch=720)),
    dict(olho='Serviços', titulo='Tabela completa, com preço de tudo.',
         texto='O cliente escolhe o serviço e já toca em Agendar.',
         visual=cel('barb-cel-servicos.png', ch=720)),
    dict(olho='Antes e depois', titulo='O seu trabalho falando por você.',
         texto='Antes e depois que o cliente arrasta com o dedo.',
         visual=cel('barb-cel-antes-depois.png', ch=720)),
    dict(olho='Agenda', titulo='O botão Agendar leva pro seu app ou direto pro seu WhatsApp.',
         texto='Você escolhe. Nada muda na sua rotina.',
         visual=cel('barb-cel-servicos.png', chip='seu site', ch=600) + applink(ch=600, chip='sua agenda')),
    dict(tipo='final', olho='Quanto custa', t=76,
         titulo='Sua barbearia com site e agenda online em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta=CTA_BARB),
]
