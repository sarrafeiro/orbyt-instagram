"""Semana parcial 04/11 a 08/11/2026 (quarta a domingo), antes da tarefa semanal começar.
python3 carrossel.py posts/semana_2026_11_04.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha, par, numero, lista

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 10. Qua 04/11 18:40, mecanismo, capa antes e depois (papel)
('10-receita-pra-6', [
    dict(tema='papel', titulo='Receita pra 6. <em>Janta pra&nbsp;2.</em>', t=88, cima=True,
         visual=par(ficha('Arroz de forno', ['3 xícaras de arroz', '6 ovos', '400 g de queijo', 'forno grande'], rot=-2, fita=False),
                    ficha('Arroz de forno', ['1 xícara de arroz', '2 ovos', '150 g de queijo', 'forma pequena'], rot=1.5, fita=False),
                    rot_a='Como vem', rot_b='Pra 2 pessoas')),
    dict(tema='creme', olho='O problema', titulo='Quase toda receita é feita <em>pra família grande.</em>',
         texto='Aí cê faz tudo e come a mesma coisa a semana inteira. Ou divide no olho e o prato desanda.'),
    dict(tema='escuro', olho='O que não é só dividir', titulo='Diminuiu a receita? <em>O tempo muda também.</em>',
         texto='Forma menor assa mais rápido. Panela com menos coisa ferve antes. Por isso dividir tudo por 3 nem sempre dá certo.'),
    dict(tema='papel', olho='O sal pede atenção', titulo='Tempero vai <em>provando.</em>', cima=True,
         visual=ficha('Regra de casa', ['divide a quantidade', 'põe menos sal no começo', 'prova antes de acertar'], rot=-1, rodape='melhor faltar que sobrar')),
    dict(tema='verde', olho='Como o NuPrato resolve', titulo='Cê fala quantas pessoas. <em>Ele refaz a&nbsp;conta.</em>',
         texto='Quantidade, tamanho da forma e tempo de forno, tudo ajustado pra sua mesa.'),
    FIM,
]),

# 11. Qui 05/11 18:40, educação salvável, capa número (verde)
('11-tres-trens', [
    dict(tema='verde', titulo='', centro=True,
         visual=numero('3', 'trens que viram janta: batata, ovo e cebola', tam=440)),
    dict(tema='papel', olho='O que vai', titulo='Omelete de batata', cima=True,
         visual=ficha('Pra 2 pessoas', ['2 batatas médias', '4 ovos', '1 cebola', 'sal e óleo'], numero='11', rot=1)),
    dict(tema='creme', olho='Passo 1', titulo='Batata em rodela <em>fininha.</em>',
         texto='Na frigideira com um fio de óleo e a cebola, fogo médio, tampada, até a batata ficar macia.'),
    dict(tema='papel', olho='Passo 2', titulo='Ovo por cima, <em>fogo baixo.</em>', cima=True,
         visual=ficha('Faz assim', ['bate os ovos com sal', 'joga por cima da batata', 'tampa e espera firmar'], rot=-1)),
    dict(tema='escuro', olho='Passo 3', titulo='Vira com <em>um prato.</em>',
         texto='Põe um prato por cima da frigideira, vira de uma vez e volta a omelete pra dourar o outro lado.'),
    dict(tema='creme', olho='Faltou um trem?', titulo='Sem cebola, <em>vai sem.</em>',
         texto='Tem queijo, presunto ou tomate? Entra junto. O NuPrato te fala o que combina com o que cê tem.'),
    FIM,
]),

# 12. Sex 06/11 18:40, comunidade, imagem única (papel)
('12-nunca-teve-coragem', [
    dict(tema='papel', titulo='Qual prato cê nunca teve <em>coragem de fazer?</em>', t=84, cima=True,
         visual=ficha('Comenta aqui embaixo', [('o', 'lasanha'), ('o', 'feijoada'), ('o', 'pudim'), ('o', 'aquele da vó')], rot=-1.5),
         nota='o mais pedido vira post'),
]),

# 13. Sáb 07/11 10:40, receita de fim de semana, capa texto (escuro)
('13-tropeiro', [
    dict(tema='escuro', selo='Fim de semana', t=112, titulo='Nunca fez tropeiro? <em>Bora&nbsp;hoje.</em>'),
    dict(tema='papel', olho='O que vai', titulo='Feijão tropeiro', cima=True,
         visual=ficha('Pra 4 pessoas', ['2 xícaras de feijão cozido', '1 xícara de farinha de mandioca', 'bacon ou linguiça', '2 ovos, cebola, alho e couve'], numero='13', rot=1)),
    dict(tema='creme', olho='Passo 1', titulo='Frita o bacon <em>na própria gordura.</em>',
         texto='Depois entra a cebola e o alho na mesma panela. É dali que vem o gosto.'),
    dict(tema='papel', olho='Passo 2', titulo='Ovo mexido <em>ali mesmo.</em>', cima=True,
         visual=ficha('Faz assim', ['abre um espaço na panela', 'mexe os ovos até firmar', 'mistura com o bacon'], rot=-1)),
    dict(tema='verde', olho='Passo 3', titulo='Feijão escorrido e <em>farinha aos poucos.</em>',
         texto='Feijão sem caldo, senão vira papa. A farinha entra mexendo até ficar soltinho. A couve vai no fim.'),
    dict(tema='creme', olho='Faltou um trem?', titulo='Sem bacon, <em>vai linguiça.</em>',
         texto='Sem couve, fica sem. Cê conta o que tem e o NuPrato ajusta o resto.', nota='trem bom de sábado'),
    FIM,
]),
]
