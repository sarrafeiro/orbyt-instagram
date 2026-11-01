import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero, busca, lista, tweet
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
FINAL = dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV)
SLUG = 'p19-depois-aprovar'
CARDS = [
    dict(tipo='texto', tema='laranja', selo='Depois do sim', t=132,
         titulo='Você aprovou o site. <em>E agora?</em>',
         rodape='Site para advogados · o que acontece depois'),
    dict(tema='escuro', olho='Passo 1', titulo='Você paga <em>uma vez só.</em>',
         visual=numero('1x', 'Pix ou cartão parcelado. Sem entrada antes e sem mensalidade depois.', tam=230), centro=True, ponto=False),
    dict(olho='Passo 2', titulo='A gente marca <em>uma chamada.</em>',
         texto='E publica o site junto com você.',
         visual=conversa('Orbyt Studio', [('eu', 'Aprovei! Quando a gente publica?', '10:02'), ('ela', 'Amanhã às 14h, por chamada. Vai pra uma conta do seu escritório.', '10:04')])),
    dict(tema='papel', olho='Passo 3', titulo='O site fica <em>no seu nome.</em>',
         texto='Publicado numa conta do próprio escritório, não numa conta nossa.',
         visual=navegador('adv1-desk-capa.png', 'andradeferraz.adv.br')),
    dict(olho='Passo 4', titulo='Coloca o link <em>onde o cliente procura.</em>',
         visual=lista([('Bio do Instagram', 'Quem chega pelo perfil vê o site'), ('Perfil do Google', 'Pra quem pesquisa o nome do escritório'),
                       ('Saudação do WhatsApp', 'Quem chama já recebe o link'), ('Assinatura de e-mail', 'Em toda mensagem que você manda')], 'num'), centro=True, ponto=False),
    FINAL,
]
