import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, lista
SLUG = 'p10-adv-celular'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=100,
         titulo='Advogado, seu site abre direito <em>no celular?</em>',
         texto='É no celular que o cliente pesquisa você. Quase sempre com pressa.',
         visual=cel('adv2-cel-capa.png', ch=660) + cel('adv1-cel-guia1.png', ch=660)),
    dict(olho='O que faz ele desistir', titulo='Ele fecha a página em segundos quando:',
         visual=lista(['Precisa dar zoom pra ler', 'O menu cobre a tela ou não abre', 'O telefone não dá pra tocar', 'A página demora e fica em branco'], 'nao'), centro=True, ponto=False),
    dict(olho='Teste de 1 minuto', titulo='Abra o seu site no celular agora.',
         visual=lista([('Dá pra ler sem zoom?', 'Texto e botões no tamanho do dedo'),
                       ('Acha as áreas de atuação em um toque?', 'Sem caçar no menu'),
                       ('O botão do WhatsApp abre a conversa?', 'Se não abre, o cliente não chama')], 'num'), centro=True, ponto=False),
    dict(olho='No nosso modelo', titulo='Áreas e equipe <em>no tamanho do polegar.</em>',
         texto='Tudo cabe na tela pequena, sem zoom e sem menu escondido.',
         visual=cel('adv1-cel-areas.png', ch=640) + cel('adv1-cel-equipe.png', ch=640)),
    dict(olho='Guia por assunto', titulo='Feito pra quem pesquisa <em>com uma mão só.</em>',
         texto='O cliente toca no assunto, vê os documentos que costumam ser pedidos e chega no seu WhatsApp.',
         visual=cel('adv1-cel-guia2.png', ch=600) + cel('adv1-cel-guia3.png', ch=600)),
    dict(olho='E no computador', titulo='O mesmo site, inteiro na tela grande.',
         texto='Seguindo o Provimento 205/2021, nos dois.',
         visual=navegador('adv2-desk-capa.png', 'andradeferraz.adv.br')),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
