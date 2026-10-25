import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, pagamento, ficha
SLUG = 'p15-monta-antes'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='texto', tema='escuro', selo='Como funciona', t=120,
         titulo='Por que a gente monta o site <em>antes de você pagar?</em>',
         rodape='Site para advogados · R$ 0 pra começar'),
    dict(olho='Motivo 1', titulo='Você decide <em>vendo o site pronto.</em>',
         texto='Nada de escolher pelo orçamento ou pela promessa. Você abre o link e vê o seu escritório no ar.',
         visual=navegador('adv1-desk-capa.png', 'orbytstudio.com.br · prévia do seu site')),
    dict(tema='papel', olho='Motivo 2', titulo='O risco <em>fica com a gente.</em>',
         visual=ficha([('Pra começar', 'R$ 0'), ('Entrada', 'nenhuma'), ('Se não aprovar', 'não paga')], destaque=True, grande=True), centro=True, ponto=False),
    dict(tema='escuro', olho='Motivo 3', titulo='Ajuste antes, <em>não depois.</em>',
         visual=conversa('Orbyt Studio', [('eu', 'Dá pra trocar a ordem das áreas e pôr a foto da equipe nova?', '10:02'), ('ela', 'Dá sim. Você tem até 2 ajustes antes de aprovar. Te mando o link atualizado.', '10:05')]), centro=True, ponto=False),
    dict(olho='Motivo 4', titulo='Aprovou? <em>Paga uma vez.</em>',
         visual=pagamento(), centro=True, ponto=False),
    dict(tema='papel', olho='E depois', titulo='A gente publica com você, <em>em chamada.</em>',
         texto='Numa conta que é sua. O site fica no seu nome, sem mensalidade.',
         visual=cel('adv1-cel-guia1.png', chip='no ar', ch=620), ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
