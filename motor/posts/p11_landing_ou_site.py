import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, ficha, lista, conversa
SLUG = 'p11-landing-ou-site'
CARDS = [
    dict(tipo='capa', olho='Antes de escolher', t=100,
         titulo='Landing page ou site? <em>Qual é o seu caso.</em>',
         texto='Os dois ficam prontos em até 2 dias úteis. A diferença está no que você precisa mostrar.',
         visual=ficha([('Landing page', 'R$ 399'), ('Site com modelo', 'R$ 797')], destaque=True, grande=True), centro=True, ponto=False),
    dict(olho='Landing page', titulo='Uma página. <em>Um objetivo.</em>',
         visual=ficha([('O que é', 'Uma página só, com um serviço e um botão de contato.'), ('Ideal pra', 'Anúncio de um serviço específico.'),
                       ('Prazo', 'Até 2 dias úteis.'), ('Preço', 'R$ 399, preço fechado.')]), centro=True, ponto=False),
    dict(olho='Escolha landing page se', titulo='Você quer vender uma coisa só.',
         visual=lista(['Vai anunciar um serviço específico', 'Quer testar uma oferta rápido', 'Já tem site e precisa de uma página pra campanha'], 'pode'), centro=True, ponto=False),
    dict(olho='Site com modelo', titulo='O seu negócio inteiro <em>num lugar só.</em>',
         visual=ficha([('Advocacia', 'Áreas de atuação, equipe e guia por assunto.'), ('Barbearia', 'Clube, tabela de serviços, antes e depois e Agendar.'),
                       ('Prazo', 'Até 2 dias úteis.'), ('Preço', 'R$ 797, preço fechado.')]), centro=True, ponto=False),
    dict(olho='Escolha site se', titulo='O cliente pesquisa você <em>antes de chamar.</em>',
         visual=lista(['Você tem mais de um serviço ou área', 'Quer um endereço pra bio, cartão e Google', 'Quer mostrar equipe, preços e trabalho'], 'pode'), centro=True, ponto=False),
    dict(olho='Na dúvida', titulo='Pergunta pra gente. <em>A resposta é rápida.</em>',
         visual=conversa('Orbyt Studio', [('eu', 'Oi! Tenho uma barbearia. Landing page ou site?', '10:02'),
                                          ('ela', 'Se você quer mostrar clube, tabela e agenda, site com modelo. R$ 797 e você só paga depois de aprovar.', '10:03')]), centro=True, ponto=False),
    dict(tipo='final', olho='Como começar', t=80,
         titulo='Manda o nome do seu negócio. A gente monta.',
         preco='R$ 0', preco_nota='pra começar<br>você paga só no fim',
         checks=['Landing page R$ 399', 'Site com modelo R$ 797', 'Pronto em até 2 dias úteis', 'Você só paga depois de aprovar'],
         cta='Chama no WhatsApp e conta o que você precisa. <b>Link no perfil.</b>'),
]
