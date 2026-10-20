import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, navegador, lista, busca
SLUG = 'p12-adv-artigo'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=80,
         titulo='Advogado, pode publicar artigo no site do escritório? <em>Pode.</em>',
         texto='E ajuda quem tem dúvida a achar você no Google.',
         visual=navegador('adv1-desk-conteudo.png', 'andradeferraz.adv.br/conteudo')),
    dict(olho='O que pode', titulo='Conteúdo informativo, <em>seguindo o Provimento 205/2021.</em>', t=84,
         visual=lista(['Explicar como funciona um direito', 'Dizer quais documentos costumam ser pedidos', 'Responder dúvidas frequentes', 'Comentar uma mudança na lei'], 'pode'), centro=True, ponto=False),
    dict(olho='O que fica de fora', titulo='O artigo informa. <em>Não capta.</em>',
         visual=lista(['Prometer resultado ou prazo de processo', 'Falar de honorários ou valores', 'Induzir o leitor a entrar na Justiça', 'Resolver o caso de alguém no texto'], 'nao'), centro=True, ponto=False),
    dict(olho='Por que ajuda', titulo='Quem tem dúvida pesquisa a dúvida.',
         texto='Um artigo seu que responde essa pergunta pode aparecer pra quem busca por ela.',
         visual=busca('aposentadoria negada pelo inss o que fazer', [
             ('bom', 'Andrade & Ferraz · Artigo', 'Aposentadoria negada pelo INSS: quais são os próximos passos')]), centro=True, ponto=False),
    dict(olho='No nosso modelo', titulo='Os artigos já têm lugar <em>no seu site.</em>',
         texto='Seção de conteúdo por área, com leitura fácil no celular.',
         visual=cel('adv1-cel-conteudo.png', ch=700)),
    dict(olho='Por onde começar', titulo='Três artigos que todo escritório pode ter.',
         visual=lista([('A dúvida que você mais ouve no atendimento', ''), ('Os documentos que o cliente sempre esquece', ''),
                       ('O que mudou na lei da sua área', '')], 'num'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Sem entrada e sem mensalidade', 'Pix ou cartão parcelado', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
