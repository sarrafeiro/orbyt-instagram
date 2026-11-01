import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, conversa, numero, busca, lista, tweet
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
FINAL = dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV)
SLUG = 'p18-adv-google-sem-site'
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=92,
         titulo='O cliente achou seu escritório no Google. <em>E não achou mais nada.</em>',
         visual=busca('andrade ferraz advocacia', [('bom', 'Perfil no Google', 'Endereço, telefone e horário'), ('ruim', 'Site do escritório', 'Nenhum resultado'), ('ruim', 'Áreas e equipe', 'Nenhum resultado')]), ponto=False),
    dict(tipo='texto', tema='escuro', selo='O que ele pensa 1', t=110,
         titulo='"Será que esse escritório <em>ainda atende?"</em>',
         texto='Só endereço e telefone, sem mais nada, parece escritório parado.'),
    dict(olho='O que ele pensa 2', titulo='"Será que atende <em>o meu caso?"</em>',
         texto='O perfil do Google não mostra áreas nem exemplos. O site mostra.',
         visual=cel('adv1-cel-areas.png', ch=600), ponto=False),
    dict(tema='papel', olho='O que ele pensa 3', titulo='"Quem vai <em>me atender?"</em>',
         texto='Nome e OAB de cada advogado passam confiança antes da ligação.',
         visual=cel('adv1-cel-equipe.png', ch=600), ponto=False),
    dict(tipo='texto', tema='laranja', selo='O que ele pensa 4', t=120,
         titulo='"Vou ver <em>o próximo da lista."</em>',
         texto='E o próximo da lista tinha site.'),
    dict(olho='Resumo', titulo='O que o site completa no seu perfil do Google.',
         visual=lista([('Áreas com exemplos', 'Ele vê que você atende o caso dele'), ('Equipe com nome e OAB', 'Ele sabe quem vai atender'),
                       ('Dúvidas frequentes', 'Informativas, seguindo o Provimento 205/2021'), ('WhatsApp a um toque', 'Pra quem quer falar agora')], 'pode'), centro=True, ponto=False),
    FINAL,
]
