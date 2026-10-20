import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, ficha, lista
SLUG = 'p07-precos'
CARDS = [
    dict(tipo='capa', olho='Preço sem letra miúda', t=100,
         titulo='Quanto custa um site com a Orbyt?',
         texto='Preço publicado, pagamento único e <b>só depois de aprovar.</b>',
         visual=ficha([('Landing page', 'R$ 399'), ('Site com modelo', 'R$ 797'), ('Personalizado', '<small style="font-size:24px;font-weight:400;letter-spacing:0">a partir de</small><br>R$ 1.497')], destaque=True, grande=True), centro=True, ponto=False),
    dict(olho='Landing page', titulo='<em>R$ 399</em>, preço fechado.',
         texto='Uma página só, simples e direta, pra um serviço ou uma campanha.',
         visual=ficha([('Prazo', 'Até 2 dias úteis'), ('Ideal pra', 'Anúncio de um serviço específico'), ('Pagamento', 'Uma vez, depois de aprovar')]), centro=True, ponto=False),
    dict(olho='Site com modelo', titulo='<em>R$ 797</em>, preço fechado.',
         texto='Site completo no modelo do seu segmento: advocacia ou barbearia.',
         visual=cel('adv2-cel-capa.png', ch=600) + cel('barb-cel-capa.png', ch=600)),
    dict(olho='Site personalizado', titulo='A partir de <em>R$ 1.497.</em>',
         texto='Feito do zero pro seu negócio. Primeira versão em 3 dias úteis, pronto em até 5.',
         visual=navegador('adv1-desk-guia3.png', 'seunegocio.com.br')),
    dict(olho='Em todos', titulo='O que vale pra qualquer um deles.',
         visual=lista([('R$ 0 pra começar', 'Sem sinal e sem entrada'),
                       ('Você só paga depois de aprovar', 'Pix ou cartão parcelado'),
                       ('Sem mensalidade', 'E o site fica no seu nome')], 'pode'), centro=True, ponto=False),
    dict(tipo='final', olho='Como começar', t=80,
         titulo='Manda o nome do seu negócio. A gente monta.',
         preco='R$ 0', preco_nota='pra começar<br>você paga só no fim',
         checks=['Pronto em até 2 dias úteis', 'Até 2 ajustes antes de aprovar', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Chama no WhatsApp e manda o nome do seu escritório ou da sua barbearia. <b>Link no perfil.</b>'),
]
