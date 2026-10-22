import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, busca, lista
SLUG = 'bbr-b05-barb-cliente-novo'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Barbearia', t=96,
         titulo='Barbeiro, de onde vem o seu <em>cliente novo?</em>',
         texto='Ele chega por um de três caminhos. E nos três procura as mesmas coisas.',
         visual=busca('barbearia perto de mim', [
             ('ruim', 'Sua barbearia · Mapa', 'Sem site, sem preço e sem horário'),
             ('bom', 'Outra barbearia · Site', 'Preços, clube e botão de agendar')]), ponto=False),
    dict(olho='Caminho 1: Google', titulo='Ele pesquisa <em>"barbearia perto de mim".</em>',
         texto='Entre as opções do mapa, sai na frente quem mostra preço e foto do trabalho.',
         visual=navegador('barb-desk-capa.png', 'suabarbearia.com.br')),
    dict(olho='Caminho 2: Instagram', titulo='Ele vê um corte seu e <em>toca no link do perfil.</em>',
         texto='Se o link abre só a agenda do app, ele não vê o clube, os seus cortes nem a cara da sua barbearia.',
         visual=cel('barb-cel-antes-depois.png', ch=660)),
    dict(olho='Caminho 3: indicação', titulo='Um cliente seu <em>manda o link</em> pro amigo.',
         texto='O amigo abre, vê o preço, vê o clube e já agenda. Sem precisar te perguntar nada.',
         visual=cel('barb-cel-clube.png', ch=660)),
    dict(olho='Nos três caminhos', titulo='Ele quer as mesmas 3 respostas.',
         visual=lista([('Quanto custa?', 'Preço de cada serviço'),
                       ('Dá pra agendar agora?', 'Botão Agendar na primeira tela'),
                       ('O trabalho é bom?', 'Antes e depois dos seus cortes')], 'num'), centro=True, ponto=False),
    dict(olho='Um link só', titulo='O seu site responde as três <em>em qualquer caminho.</em>',
         texto='No Google, na bio do Instagram e no WhatsApp: o mesmo link.',
         visual=cel('barb-cel-servicos.png', ch=620) + cel('barb-cel-tabela.png', ch=620)),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Sua barbearia com site e agenda online em 2 dias úteis.',
         preco='R$ 399', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'],
         cta=CTA_BARB),
]
