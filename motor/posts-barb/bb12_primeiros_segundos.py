import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, cel, ficha, checklist
# Educação salvável (qui 29/10/2026). Único carrossel da semana com print: 1 card de prova com o antes e depois.
SLUG = 'bb12-primeiros-segundos'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='capa', olho='Salva pra conferir', t=100,
         titulo='O que o cliente novo procura <em>nos primeiros segundos.</em>',
         visual=lista([('Se o corte é bom', ''), ('Quanto custa', ''), ('Se tem horário', ''), ('Onde fica', '')], 'num'), centro=True, ponto=False),
    dict(olho='Primeiro', titulo='Se o corte é bom. <em>Ele quer ver o trabalho.</em>',
         texto='No site ele arrasta o antes e depois do seu degradê e decide sozinho.',
         visual=cel('barb-cel-antes-depois.png', ch=720), centro=True, ponto=False),
    dict(tema='escuro', titulo='Depois, <em>quanto custa.</em>',
         texto='Se tem que perguntar, ele pergunta pra três barbearias e fica com quem responde primeiro.', gigante=True, t=124, s=44, ponto=False),
    dict(tema='papel', olho='Por último', titulo='Horário e endereço.',
         visual=ficha([('Horário', 'Botão Agendar logo na primeira tela, sem precisar mandar mensagem.'),
                       ('Endereço', 'Mapa, estacionamento e se atende criança.')]), centro=True, ponto=False),
    dict(tipo='texto', tema='laranja', t=128,
         titulo='Não achou rápido? <em>Ele volta pra busca e clica na próxima.</em>'),
    dict(tema='papel', olho='Confere hoje', titulo='O cliente acha isso no seu link?',
         visual=checklist(['Foto ou antes e depois dos seus cortes', 'Preço de cada serviço', 'Botão Agendar sem mandar mensagem', 'Endereço e como chegar'], marcados=0), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
