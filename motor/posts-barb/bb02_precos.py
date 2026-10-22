import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import ficha, checklist, numero
SLUG = 'bb02-precos'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='texto', tema='escuro', selo='Preço publicado', t=118,
         titulo='Quanto custa o site da sua barbearia? <em>Sem letra miúda.</em>'),
    dict(olho='Os preços', titulo='Três opções. <em>Preço fechado.</em>',
         visual=ficha([('Landing page', 'R$ 199'), ('Site com modelo de barbearia', 'R$ 399'), ('Site 100% personalizado', '<small style="font-size:26px;display:block">a partir de</small>R$ 1.497')], destaque=True, grande=True), centro=True, ponto=False),
    dict(tema='papel', olho='No site com modelo', titulo='O que vem incluído:',
         visual=checklist(['Botão Agendar logo na primeira tela', 'Tabela de serviços com preço', 'Clube de assinatura com a economia', 'Antes e depois dos seus cortes', 'Avaliações, espaço e como chegar', 'Publicação em chamada, no seu nome'], marcados=6), centro=True, ponto=False),
    dict(tema='laranja', olho='Faz a conta', titulo='Menos que <em>5 cortes.</em>',
         visual=numero('R$ 399', '5 cortes de R$ 80 dão R$ 400. E o site trabalha pra você todo dia.', tam=195), centro=True, ponto=False),
    dict(tipo='texto', tema='escuro', t=140, titulo='Sem entrada. <em>Sem mensalidade.</em>',
         texto='Você paga uma vez, depois de aprovar o site pronto.'),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
