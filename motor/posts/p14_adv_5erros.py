import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, numero, site_antigo, lista, checklist, par, tweet
SLUG = 'p14-adv-5erros'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', tema='laranja', olho='Advocacia', t=92,
         titulo='5 erros no site do escritório <em>que espantam cliente.</em>',
         visual=numero('5', 'motivos pra ele fechar a aba e ligar pro próximo', tam=300), centro=True, ponto=False),
    dict(tema='papel', olho='Erro 1', titulo='Não abre direito <em>no celular.</em>',
         texto='Precisa dar zoom, o menu cobre a tela. É no celular que o cliente pesquisa você.',
         visual=site_antigo(), ponto=False),
    dict(olho='Erro 2', titulo='Contato só por <em>telefone fixo.</em>',
         texto='Quem pesquisa às 22h não liga. Ele quer um botão de WhatsApp a um toque.',
         visual=cel('adv2-cel-capa.png', chip='WhatsApp na primeira tela', ch=600), ponto=False),
    dict(tema='escuro', olho='Erro 3', titulo='"Atuamos nas mais diversas <em>áreas do Direito."</em>',
         texto='Frase que não diz nada. O cliente quer ler o problema dele: demissão, divórcio, INSS.',
         visual=cel('adv1-cel-areas.png', ch=600), ponto=False),
    dict(olho='Erro 4', titulo='Ninguém sabe <em>quem são os advogados.</em>',
         texto='Sem nome, foto e número da OAB, falta confiança pra mandar a primeira mensagem.',
         visual=cel('adv1-cel-equipe.png', ch=600), ponto=False),
    dict(tema='papel', olho='Erro 5', titulo='Prometer o que <em>não pode.</em>',
         visual=lista([('"Garantimos o resultado"', 'Promessa de resultado é vedada'), ('"Consulta grátis"', 'Captação que o Código de Ética proíbe'), ('"Entre com sua ação hoje"', 'Induzir a processar também não pode')], 'nao'), centro=True, ponto=False),
    dict(olho='Resumo', titulo='Salva e confere <em>no seu site.</em>',
         visual=checklist(['Abre direito no celular', 'WhatsApp a um toque', 'Áreas escritas com o problema do cliente', 'Equipe com nome e OAB', 'Nada de promessa de resultado'], marcados=0), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
