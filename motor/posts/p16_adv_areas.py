import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, lista, checklist, par, tweet
SLUG = 'p16-adv-areas'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Provimento 205/2021', t=92,
         titulo='Como mostrar suas áreas de atuação <em>sem ferir o Código de Ética.</em>',
         visual=navegador('adv1-desk-areas.png', 'andradeferraz.adv.br/#areas'), ponto=False),
    dict(tema='papel', olho='Passo 1', titulo='Escreva o problema, <em>não o ramo do Direito.</em>',
         visual=par(tweet('Direito Civil, Direito do Trabalho, Direito Previdenciário.', tam=34), tweet('<em>Trabalho e demissão:</em> rescisão, horas extras, vínculo.', tam=34), 'Assim não', 'Assim sim'), ponto=False),
    dict(olho='Passo 2', titulo='Dê exemplos <em>de situações atendidas.</em>',
         texto='Três exemplos por área bastam. O cliente se reconhece e entende que é com você.',
         visual=cel('adv1-cel-areas.png', ch=620), ponto=False),
    dict(tema='escuro', olho='Passo 3', titulo='Informe, <em>não convença.</em>',
         texto='Conteúdo informativo é permitido: como funciona o direito, quais documentos costumam ser pedidos.',
         visual=cel('adv1-cel-guia3.png', ch=600), ponto=False),
    dict(olho='Fica de fora', titulo='O que não entra <em>na página de áreas.</em>',
         visual=lista([('Promessa de resultado', '"Ganhe sua causa"'), ('Valor de honorários', 'Nem "preço baixo"'), ('Consulta grátis', 'Nem como chamariz'), ('Incentivo a processar', '"Não perca seu direito, entre hoje"')], 'nao'), centro=True, ponto=False),
    dict(tema='papel', olho='Resumo', titulo='Salva pra revisar <em>a sua página.</em>',
         visual=checklist(['Área escrita com o problema do cliente', '3 exemplos de situação por área', 'Texto informativo, linguagem simples', 'Sem promessa, sem honorário, sem consulta grátis'], marcados=4), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
