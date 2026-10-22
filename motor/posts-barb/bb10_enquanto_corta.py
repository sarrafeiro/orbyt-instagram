import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import conversa, checklist
# Carrossel só de argumento (sem print de celular): a dor do barbeiro que não consegue responder enquanto corta.
SLUG = 'bb10-enquanto-corta'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='capa', tema='papel', olho='Barbearia', t=100,
         titulo='Barbeiro, enquanto você corta, <em>quem responde o cliente?</em>',
         visual=conversa('Cliente novo', [('ela', 'Boa tarde! Quanto tá o corte?', '14:02'), ('ela', 'Tem horário hoje ainda?', '14:09')], pessoa=True), ponto=False),
    dict(tema='escuro', titulo='Você tá com a máquina na mão. <em>O celular vibra.</em>',
         texto='Cliente na cadeira vem primeiro. A mensagem fica pra depois.', gigante=True, t=124, s=44, ponto=False),
    dict(olho='Meia hora depois', titulo='Ele já perguntou pra <em>outras duas barbearias.</em>',
         visual=conversa('Cliente novo', [('ela', 'Quanto tá o corte?', '14:02'), ('eu', 'Opa! R$ 50. Tenho às 18h, pode ser?', '14:33'), ('ela', 'Ah, já marquei em outra. Valeu!', '14:34')], pessoa=True), centro=True, ponto=False),
    dict(tema='papel', olho='O site responde por você', titulo='Antes de ele perguntar:',
         visual=checklist(['Preço de cada serviço', 'Botão Agendar que abre a sua agenda', 'Antes e depois dos seus cortes', 'Endereço, estacionamento e se atende criança'], marcados=4), centro=True, ponto=False),
    dict(tipo='texto', tema='laranja', t=128,
         titulo='O site não corta cabelo. <em>Mas atende enquanto você corta.</em>'),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
