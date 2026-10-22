import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import ficha, lista
SLUG = 'bb03-tres-jeitos'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='capa', olho='Antes de contratar', t=100,
         titulo='Barbeiro, três jeitos de ter um site.',
         texto='A diferença aparece no prazo, no bolso e em quem fica dono do site no final.',
         visual=lista([('Fazer sozinho', ''), ('Agência tradicional', ''), ('Orbyt Studio', '')], 'num'), centro=True, ponto=False),
    dict(olho='Jeito 1', titulo='Fazer sozinho.', texto='Num construtor de sites, entre um corte e outro.',
         visual=ficha([('Prazo', 'Suas noites e folgas, sem data pra acabar.'), ('Mensalidade', 'Da plataforma, enquanto o site existir.'),
                       ('Seu risco', 'Gastar tempo e não gostar do resultado.'), ('Dono do site', 'Fica preso à plataforma.')]), centro=True, ponto=False),
    dict(tema='papel', olho='Jeito 2', titulo='Agência tradicional.', texto='Reunião, orçamento, briefing e espera.',
         visual=ficha([('Prazo', 'Semanas, às vezes meses.'), ('Preço', 'Sob orçamento, só depois de reunião.'),
                       ('Mensalidade', 'É comum cobrar manutenção ou hospedagem.'), ('Seu risco', 'Pagar entrada sem ter visto nada pronto.')]), centro=True, ponto=False),
    dict(olho='Jeito 3', titulo='Orbyt Studio.', texto='Modelo de barbearia pronto, preço publicado e tudo pelo WhatsApp.',
         visual=ficha([('Prazo', 'Até 2 dias úteis com o modelo de barbearia.'), ('Preço', 'Site R$ 797. Landing R$ 399.'),
                       ('Mensalidade', 'Nenhuma. Você paga uma vez.'), ('Seu risco', 'Nenhum adiantamento: só paga depois de aprovar.'),
                       ('Dono do site', 'Você. Publicado na sua conta, no seu nome.')], destaque=True), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
