import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel
SLUG = 'bbr-p09-barb-5-coisas'
CARDS = [
    dict(tipo='capa', olho='Barbearia', t=96,
         titulo='5 coisas que o site da sua barbearia <em>precisa ter.</em>',
         texto='Salva pra conferir no seu.',
         visual=cel('barb-cel-capa.png', ch=620) + cel('barb-cel-clube.png', ch=620)),
    dict(olho='1 de 5', titulo='Preço de cada serviço.', texto='O cliente quer saber quanto custa antes de marcar.',
         visual=cel('barb-cel-servicos.png', ch=720)),
    dict(olho='2 de 5', titulo='Botão de agendar logo na primeira tela.', texto='Do primeiro toque até o horário marcado, sem procurar.',
         visual=cel('barb-cel-capa.png', ch=720)),
    dict(olho='3 de 5', titulo='Clube de assinatura em destaque.', texto='Planos com preço e economia. É o cliente que volta todo mês.',
         visual=cel('barb-cel-clube.png', ch=720)),
    dict(olho='4 de 5', titulo='Antes e depois dos seus cortes.', texto='O seu trabalho convence melhor que qualquer texto.',
         visual=cel('barb-cel-antes-depois.png', ch=720)),
    dict(olho='5 de 5', titulo='Resposta pras dúvidas de sempre.', texto='Precisa agendar? Atende criança? Tem estacionamento? O site responde antes de você.',
         visual=cel('barb-cel-duvidas.png', ch=680)),
    dict(tipo='final', olho='Quanto custa', t=76,
         titulo='Sua barbearia com site e agenda online em 2 dias úteis.',
         preco='R$ 399', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'),
]
