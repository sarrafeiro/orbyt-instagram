import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero, busca, lista, tweet
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
FINAL = dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV)
SLUG = 'p20-antes-de-ligar'
CARDS = [
    dict(tipo='capa', olho='Salva esse', t=94,
         titulo='O que o cliente quer ver <em>antes de ligar pro escritório.</em>',
         texto='5 coisas, na ordem em que ele procura.',
         visual=cel('adv2-cel-capa.png', ch=620), ponto=False),
    dict(olho='1 de 5', titulo='Se você atende <em>o caso dele.</em>',
         texto='Áreas explicadas com exemplos, na língua do cliente.',
         visual=cel('adv1-cel-areas.png', ch=600), ponto=False),
    dict(tema='escuro', olho='2 de 5', titulo='Quem vai <em>atender.</em>',
         texto='Nome, cargo e OAB de cada advogado.',
         visual=cel('adv1-cel-equipe.png', ch=600), ponto=False),
    dict(tema='papel', olho='3 de 5', titulo='Como funciona <em>o primeiro contato.</em>',
         texto='Um guia por assunto mostra o caminho e o que levar.',
         visual=cel('adv1-cel-guia1.png', ch=600), ponto=False),
    dict(olho='4 de 5', titulo='Respostas pras <em>dúvidas de sempre.</em>',
         texto='Sem valores e sem promessa, como pede o Provimento 205/2021.',
         visual=cel('adv1-cel-duvidas.png', ch=600), ponto=False),
    dict(tema='laranja', olho='5 de 5', titulo='Um jeito fácil <em>de chamar.</em>',
         texto='WhatsApp a um toque, com a mensagem pronta.',
         visual=cel('adv2-cel-guia3.png', ch=600), ponto=False),
    FINAL,
]
