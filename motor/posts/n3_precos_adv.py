import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import ficha, checklist
SLUG = 'n3-precos-adv'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='texto', tema='escuro', selo='Preço publicado', t=118,
         titulo='Quanto custa o site do seu escritório? <em>Sem letra miúda.</em>'),
    dict(olho='Os preços', titulo='Três opções. <em>Preço fechado.</em>',
         visual=ficha([('Landing page', 'R$ 399'), ('Site com modelo de advocacia', 'R$ 797'), ('Site 100% personalizado', '<small style="font-size:26px;display:block">a partir de</small>R$ 1.497')], destaque=True, grande=True), centro=True, ponto=False),
    dict(tema='papel', olho='No site com modelo', titulo='O que vem incluído:',
         visual=checklist(['Guia por assunto em 3 cliques', 'Áreas de atuação explicadas', 'Equipe com nome e número da OAB', 'Artigos e dúvidas frequentes', 'WhatsApp em cada parte da página', 'Publicação em chamada, no seu nome'], marcados=6), centro=True, ponto=False),
    dict(tipo='texto', tema='laranja', t=140, titulo='Sem entrada. <em>Sem mensalidade.</em>',
         texto='Você paga uma vez, depois de aprovar o site pronto.'),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
