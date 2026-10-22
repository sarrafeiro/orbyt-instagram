import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import numero
# Carrossel só de argumento (sem print de celular): a conta de um cliente que volta.
# Conta de exemplo e explícita: corte de R$ 80, a cada 3 semanas = 17 cortes no ano (52/3) = R$ 1.360.
SLUG = 'bb09-faz-a-conta'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='texto', tema='laranja', selo='Faz a conta', t=132,
         titulo='Barbeiro, quanto vale <em>um cliente que volta?</em>',
         rodape='Site para barbearia · conta de 1 minuto'),
    dict(olho='A conta', titulo='Corte de R$ 80, <em>a cada 3 semanas.</em>',
         visual=numero('17 cortes', 'no ano, de um cliente só. Troca pelo seu preço: a conta continua boa.', tam=150), centro=True, ponto=False),
    dict(tema='escuro', olho='17 × R$ 80', titulo='Um cliente fiel deixa isso <em>por ano.</em>',
         visual=numero('R$ 1.360', 'E ainda indica o irmão, o primo e o amigo do trabalho.', tam=150), centro=True, ponto=False),
    dict(tema='papel', olho='Agora o site', titulo='R$ 399, <em>uma vez só.</em>',
         texto='Se ele trouxer um cliente que volta, já se pagou mais de 3 vezes no primeiro ano.', gigante=True, t=120, s=44, ponto=False),
    dict(olho='E tem o clube', titulo='Quem assina o clube <em>volta todo mês sem você pedir.</em>',
         texto='No site, cada plano aparece com o preço e quanto o cliente economiza.', gigante=True, t=100, s=40, ponto=False),
    dict(tipo='texto', tema='escuro', t=112,
         titulo='A pergunta não é se o site é caro. <em>É quantos clientes você perde sem ele.</em>'),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
