import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, pagamento
SLUG = 'b01-fixado-adv'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Site para advocacia', t=98,
         titulo='Advogado, este é o site do <em>seu escritório.</em>',
         texto='<b>Pronto em até 2 dias úteis. Você só paga depois de aprovar.</b>',
         visual=cel('adv2-cel-capa.png', ch=650) + cel('adv1-cel-guia3.png', ch=650)),
    dict(olho='Primeira tela', titulo='Quem você é, o que atende e <em>como falar com você.</em>',
         texto='Áreas de atuação, cidade e o botão do WhatsApp logo de cara, no celular e no computador.',
         visual=navegador('adv2-desk-capa.png', 'andradeferraz.adv.br')),
    dict(olho='Guia por assunto', titulo='O cliente escolhe o assunto <em>em três cliques.</em>',
         texto='Vê como funciona, quais documentos costumam ser pedidos e chega no seu WhatsApp sabendo com quem falar.',
         visual=cel('adv2-cel-guia1.png', ch=600) + cel('adv2-cel-guia3.png', ch=600)),
    dict(olho='Áreas de atuação', titulo='Cada área explicada <em>em linguagem simples.</em>',
         texto='O cliente entende se você atende o caso dele antes da primeira mensagem.',
         visual=cel('adv1-cel-areas.png', ch=720)),
    dict(olho='Equipe', titulo='Advogados com nome e <em>número da OAB.</em>',
         texto='Quem vai atender, com foto e registro. É o que passa confiança antes da primeira conversa.',
         visual=cel('adv1-cel-equipe.png', ch=720)),
    dict(olho='Conteúdo e dúvidas', titulo='Artigos e perguntas frequentes <em>no seu site.</em>',
         texto='Conteúdo informativo, seguindo o Provimento 205/2021.',
         visual=cel('adv1-cel-conteudo.png', ch=660) + cel('adv1-cel-duvidas.png', ch=660)),
    dict(olho='Como funciona', titulo='A gente monta primeiro. <em>Você paga depois.</em>',
         texto='Você confere o site pronto num link nosso e pede até 2 ajustes. Aprovou? Paga uma vez, no Pix ou no cartão parcelado.',
         visual=pagamento(), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório com modelo de advocacia.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Pronto em até 2 dias úteis', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
