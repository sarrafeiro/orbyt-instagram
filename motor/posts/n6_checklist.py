import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import checklist
SLUG = 'n6-checklist'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
I = [('Abre direito no celular', 'É onde o cliente pesquisa você'), ('WhatsApp a um toque', 'Em cada parte da página'), ('Áreas de atuação explicadas', 'Em linguagem que o cliente entende'), ('Equipe com nome e OAB', 'Quem vai atender, com registro'),
     ('Endereço e horário', 'Pra quem quer ir até você'), ('Dúvidas frequentes', 'Respondidas antes do contato'), ('Conteúdo informativo', 'Seguindo o Provimento 205/2021')]
CARDS = [
    dict(tipo='capa', tema='papel', olho='Checklist', t=100,
         titulo='O site do seu escritório <em>tem estes 7 itens?</em>',
         texto='Salva e marca quantos o seu tem hoje.',
         visual=checklist([a for a, b in I[:3]]), centro=True, ponto=False),
    dict(tema='papel', olho='Itens 1 a 4', titulo='O básico que o cliente procura.', visual=checklist(I[:4]), centro=True, ponto=False),
    dict(tema='papel', olho='Itens 5 a 7', titulo='O que faz ele chamar você.', visual=checklist(I[4:]), centro=True, ponto=False),
    dict(tipo='texto', tema='laranja', t=128, titulo='Faltou algum? <em>O nosso modelo já vem com os 7.</em>',
         texto='Pronto em até 2 dias úteis.'),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
