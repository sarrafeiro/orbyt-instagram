import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, busca, lista
SLUG = 'p04-adv-pesquisa'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=92,
         titulo='Advogado, seu cliente pesquisa você <em>antes de ligar.</em>',
         texto='O que ele encontra decide se ele chama você ou o próximo da lista.',
         visual=busca('advogado trabalhista em bh', [
             ('ruim', 'Seu escritório · Instagram', 'Último post há 8 meses'),
             ('ruim', 'Seu escritório · Mapa', 'Sem site e sem horário de atendimento'),
             ('bom', 'Outro escritório · Site', 'Áreas, equipe e WhatsApp num lugar só')]), ponto=False),
    dict(olho='O que ele procura', titulo='Em poucos segundos, ele quer 3 respostas.',
         visual=lista([('Você atende o meu assunto?', 'Áreas de atuação claras'),
                       ('Quem vai me atender?', 'Equipe com nome e número da OAB'),
                       ('Como eu falo com vocês agora?', 'WhatsApp num toque')], 'num'), centro=True, ponto=False),
    dict(olho='O site', titulo='O seu site responde as três antes da primeira mensagem.',
         texto='Áreas de atuação, equipe e WhatsApp em cada parte da página.',
         visual=cel('adv1-cel-areas.png', ch=640) + cel('adv1-cel-equipe.png', ch=640)),
    dict(olho='Guia por assunto', titulo='O cliente escolhe o assunto <em>em três cliques.</em>',
         texto='Vê como funciona e quais documentos costumam ser pedidos. E chega no seu WhatsApp sabendo com quem falar.',
         visual=cel('adv1-cel-guia2.png', ch=600) + cel('adv1-cel-guia3.png', ch=600)),
    dict(olho='Regras da OAB', titulo='Feito seguindo o Provimento 205/2021.',
         texto='Conteúdo informativo, sem promessa de resultado, sem falar de honorários e sem induzir ninguém a processar.',
         visual=navegador('adv1-desk-guia3.png', 'andradeferraz.adv.br')),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
