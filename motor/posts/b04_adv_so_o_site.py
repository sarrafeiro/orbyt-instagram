import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, lista
SLUG = 'b04-adv-so-o-site'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=96,
         titulo='Advogado, o Instagram ajuda. Mas <em>4 coisas só o site faz.</em>',
         texto='Confere se o seu escritório já tem as quatro.',
         visual=cel('adv2-cel-capa.png', ch=620)),
    dict(olho='1 de 4', titulo='Mostra tudo <em>num lugar só.</em>',
         texto='Áreas de atuação, equipe com OAB, endereço e contato numa página. No Instagram isso fica espalhado em dezenas de posts.',
         visual=cel('adv1-cel-areas.png', ch=660)),
    dict(olho='2 de 4', titulo='Responde dúvida <em>sem você estar online.</em>',
         texto='Perguntas frequentes e conteúdo informativo trabalham enquanto você está em audiência.',
         visual=cel('adv1-cel-duvidas.png', ch=660)),
    dict(olho='3 de 4', titulo='Leva o cliente ao WhatsApp <em>sabendo o assunto.</em>',
         texto='No guia por assunto ele escolhe o tema em três cliques e já chega dizendo o que precisa.',
         visual=cel('adv2-cel-guia-inss.png', ch=660)),
    dict(olho='4 de 4', titulo='É seu. <em>Não depende de algoritmo.</em>',
         texto='O site fica no seu nome. O cliente encontra você mesmo se o escritório passar um mês sem postar.',
         visual=navegador('adv1-desk-areas.png', 'andradeferraz.adv.br')),
    dict(olho='Resumo', titulo='Salva pra conferir no seu.',
         visual=lista([('Tudo num lugar só', 'Áreas, equipe, endereço e contato'),
                       ('Responde sem você estar online', 'Dúvidas e conteúdo informativo'),
                       ('Leva ao WhatsApp sabendo o assunto', 'Guia por assunto em 3 cliques'),
                       ('É seu', 'No seu nome, sem depender de algoritmo')], 'pode'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
