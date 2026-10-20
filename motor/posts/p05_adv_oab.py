import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, lista
SLUG = 'p05-adv-oab'
CARDS = [
    dict(tipo='capa', olho='Advocacia · Provimento 205/2021', t=92,
         titulo='O que a OAB deixa e o que <em>proíbe</em> no site do seu escritório.',
         texto='Salva esse post pra conferir antes de mexer no seu site.',
         visual=navegador('adv1-desk-guia1.png', 'andradeferraz.adv.br', w=760)),
    dict(olho='Pode', titulo='Pode mostrar quem você é.',
         visual=lista([('Áreas de atuação', 'Explicadas de forma informativa'),
                       ('Equipe', 'Nome e número da OAB de cada advogado'),
                       ('Endereço, horário e contato', 'Inclusive botão de WhatsApp')], 'pode'), centro=True, ponto=False),
    dict(olho='Pode', titulo='Pode informar, sem dar consulta.',
         visual=lista([('Conteúdo educativo', 'Explicar como um assunto funciona, de forma geral'),
                       ('Ferramenta que facilita o contato', 'Um guia por assunto que leva até o advogado'),
                       ('Aviso claro', 'Informação geral não substitui a análise do advogado')], 'pode'), centro=True, ponto=False),
    dict(olho='Não pode', titulo='Não pode prometer nem vender.',
         visual=lista([('Prometer resultado', 'Nem citar casos ganhos'),
                       ('Falar de honorários', 'Valores, descontos ou consulta grátis'),
                       ('Depoimento de cliente', 'Nem resultado de processo')], 'nao'), centro=True, ponto=False),
    dict(olho='Não pode', titulo='Não pode empurrar ninguém pro processo.',
         visual=lista([('Induzir a litigar', 'Frase do tipo "você tem direito a indenização"'),
                       ('Responder consulta no automático', 'Parecer individual pra quem ainda não é cliente'),
                       ('Dizer que o site é aprovado pela OAB', 'A OAB não homologa site nem texto')], 'nao'), centro=True, ponto=False),
    dict(olho='Na prática', titulo='Nossos sites de advocacia já saem dentro dessas regras.',
         texto='A responsabilidade ética do conteúdo continua sendo do advogado: você confere tudo antes de aprovar. Resumo informativo do Provimento 205/2021 e do Código de Ética da OAB.',
         s=32, visual=cel('adv1-cel-guia3.png', ch=560)),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta='Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'),
]
