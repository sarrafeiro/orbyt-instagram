import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, lista, par, site_antigo
SLUG = 'n4-antes-depois'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Antes e depois', t=96,
         titulo='O site do seu escritório <em>ainda parece de 2015?</em>',
         visual=par(site_antigo(), cel('adv2-cel-capa.png', ch=560)), ponto=False),
    dict(tema='papel', olho='Antes', titulo='É isso que o cliente encontra.',
         texto='Visitante nº 000123, letra miúda e telefone fixo em horário comercial.',
         visual=site_antigo(), centro=True, ponto=False),
    dict(olho='3 sinais de site velho', titulo='Se tem um desses, <em>o cliente desconfia.</em>',
         visual=lista([('Não abre direito no celular', 'É ali que o cliente pesquisa você'), ('Contato só por telefone fixo', 'Sem WhatsApp, ele não chama'), ('Não diz quem são os advogados', 'Sem nome e OAB, falta confiança')], 'nao'), centro=True, ponto=False),
    dict(tema='escuro', olho='Depois', titulo='O mesmo escritório, <em>com site novo.</em>',
         visual=cel('adv2-cel-capa.png', ch=640) + cel('adv1-cel-equipe.png', ch=640)),
    dict(olho='O que muda', titulo='Agora o cliente encontra:',
         visual=lista([('Site que abre perfeito no celular', ''), ('WhatsApp em cada parte da página', ''), ('Equipe com nome e número da OAB', ''), ('Guia por assunto em 3 cliques', '')], 'pode'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
