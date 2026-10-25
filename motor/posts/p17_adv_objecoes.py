import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import conversa, cel, numero
SLUG = 'p17-adv-objecoes'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
def qa(p, r): return conversa('Orbyt Studio', [('eu', p, '18:40'), ('ela', r, '18:42')])
CARDS = [
    dict(tipo='capa', olho='O que a gente mais ouve', t=94,
         titulo='4 frases que todo advogado fala do site. <em>E a resposta pra cada uma.</em>',
         visual=qa('Meu cliente vem todo por indicação. Preciso de site?', 'Quem foi indicado pesquisa o seu nome antes de ligar. O site é o que ele encontra.'), ponto=False),
    dict(olho='Frase 1', titulo='"Meu cliente vem <em>por indicação."</em>',
         visual=qa('Mas eu nunca precisei de site.', 'A indicação traz o nome. O site confirma que você atende o caso dele e mostra o WhatsApp a um toque.'), centro=True, ponto=False),
    dict(tema='escuro', olho='Frase 2', titulo='"Meu sobrinho <em>faz pra mim."</em>',
         visual=qa('Meu sobrinho mexe com isso, vou pedir pra ele.', 'Pode ser. Aqui fica pronto em até 2 dias úteis, já seguindo o Provimento 205/2021, e você só paga se aprovar.'), centro=True, ponto=False),
    dict(olho='Frase 3', titulo='"Não sei o que <em>escrever no site."</em>',
         visual=qa('Não tenho tempo de escrever texto.', 'Não precisa. O modelo de advocacia já vem com áreas, guia por assunto e dúvidas. Você só confere.'), centro=True, ponto=False),
    dict(tema='laranja', olho='Frase 4', titulo='"Deixa pro <em>ano que vem."</em>',
         visual=numero('2 dias', 'úteis pra ficar pronto. E R$ 0 pra começar.', tam=200), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
