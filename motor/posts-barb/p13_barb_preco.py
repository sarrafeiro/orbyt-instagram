import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, lista, conversa
SLUG = 'bbr-p13-barb-preco'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Barbearia', t=92,
         titulo='Barbeiro, cliente que não acha seu preço <em>vai pra outra barbearia.</em>',
         texto='Ninguém gosta de perguntar quanto custa.',
         visual=cel('barb-cel-servicos.png', chip='preço de tudo', ch=590)),
    dict(olho='Cliente novo', titulo='Antes de ir, ele quer saber 3 coisas.',
         visual=lista([('Quanto custa', 'Corte, barba, combo'), ('Se tem horário', 'Hoje ou amanhã cedo'), ('Se o corte é bom', 'Foto do trabalho de verdade')], 'num'), centro=True, ponto=False),
    dict(olho='Quando ele tem que perguntar', titulo='Ele manda mensagem pra três <em>e fica com quem responde primeiro.</em>', t=84,
         visual=conversa('Sua Barbearia', [('eu', 'Boa noite! Quanto tá corte e barba?', '22:14'), ('eu', 'Tem horário amanhã cedo?', '22:15')]), centro=True, ponto=False),
    dict(olho='No seu site', titulo='Os mais pedidos, <em>com preço, logo de cara.</em>',
         texto='Ele vê, escolhe e toca em Agendar.',
         visual=cel('barb-cel-servicos.png', ch=700)),
    dict(olho='Tabela completa', titulo='E todos os serviços <em>num toque.</em>',
         texto='Com busca e filtro: corte, barba, combo, química.',
         visual=cel('barb-cel-tabela.png', ch=700)),
    dict(olho='Clube de assinatura', titulo='Quem quer economizar <em>vê o clube.</em>',
         texto='Plano, preço por mês e quanto ele economiza.',
         visual=cel('barb-cel-clube.png', ch=700)),
    dict(tipo='final', olho='Quanto custa', t=76,
         titulo='Sua barbearia com preço, agenda e site em 2 dias úteis.',
         preco='R$ 399', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta=CTA_BARB),
]
