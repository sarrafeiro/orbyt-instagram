import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import ficha, lista
SLUG = 'p08-tres-jeitos'
CARDS = [
    dict(tipo='capa', olho='Antes de contratar', t=100,
         titulo='Três jeitos de ter um site.',
         texto='A diferença aparece no prazo, no bolso e em quem fica dono do site no final.',
         visual=lista([('Fazer sozinho', ''), ('Agência tradicional', ''), ('Orbyt Studio', '')], 'num'), centro=True, ponto=False),
    dict(olho='Jeito 1', titulo='Fazer sozinho.', texto='Num construtor de sites, nas horas vagas.',
         visual=ficha([('Prazo', 'Suas noites e fins de semana, sem data pra acabar.'), ('Mensalidade', 'Da plataforma, enquanto o site existir.'),
                       ('Seu risco', 'Gastar tempo e não gostar do resultado.'), ('Dono do site', 'Fica preso à plataforma.')]), centro=True, ponto=False),
    dict(olho='Jeito 2', titulo='Agência tradicional.', texto='Reunião, orçamento, briefing e espera.',
         visual=ficha([('Prazo', 'Semanas, às vezes meses.'), ('Preço', 'Sob orçamento, só depois de reunião.'),
                       ('Mensalidade', 'É comum cobrar manutenção ou hospedagem.'), ('Seu risco', 'Pagar entrada sem ter visto nada pronto.')]), centro=True, ponto=False),
    dict(olho='Jeito 3', titulo='Orbyt Studio.', texto='Modelo do seu segmento, preço publicado e tudo pelo WhatsApp.',
         visual=ficha([('Prazo', 'Até 2 dias úteis com modelo, 5 no personalizado.'), ('Preço', 'Landing R$ 399, site R$ 797.'),
                       ('Mensalidade', 'Nenhuma. Você paga uma vez.'), ('Seu risco', 'Nenhum adiantamento: só paga depois de aprovar.'),
                       ('Dono do site', 'Você. Publicado na sua conta, no seu nome.')], destaque=True), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site com modelo do seu segmento.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Pronto em até 2 dias úteis', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Manda o nome do seu escritório ou da sua barbearia no WhatsApp. <b>Link no perfil.</b>'),
]
