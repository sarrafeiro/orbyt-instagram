"""Semana 09/11 a 15/11/2026 (tarefa semanal). Ordem = ordem de publicação.
python3 carrossel.py posts/semana_2026_11_09.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha, par, conversa, numero

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 14. Seg 09/11 18:40, dor, capa ficha (papel)
('14-arroz-empapou', [
    dict(tema='papel', titulo='Arroz empapou? <em>Ainda dá&nbsp;janta.</em>', t=88, cima=True,
         visual=ficha('Arroz empapado', [('o', 'seca no fogo baixo'), ('o', 'vira bolinho de arroz'), ('o', 'vira arroz cremoso com queijo')], rot=1.2)),
    dict(tema='creme', olho='Primeiro', titulo='Não joga fora. <em>Tem&nbsp;jeito.</em>',
         texto='Arroz empapado é só arroz com água demais. Dá pra secar um pouco ou virar outro prato.'),
    dict(tema='escuro', olho='Pra salvar agora', titulo='Destampa e <em>deixa a água&nbsp;sair.</em>',
         texto='Fogo bem baixo, panela aberta, uns minutos sem mexer. Mexer agora só deixa mais grudado.'),
    dict(tema='papel', olho='Ou vira outro prato', titulo='Bolinho de arroz', cima=True,
         visual=ficha('Faz assim', ['arroz empapado frio', '1 ovo e queijo ralado', 'farinha até dar ponto', 'frita às colheradas'], numero='14', rot=-1)),
    dict(tema='verde', olho='Pra próxima', titulo='A água certa <em>depende da&nbsp;panela.</em>',
         texto='Arroz branco comum costuma ir com 2 de água pra 1 de arroz. Fogo baixo e tampa até secar.'),
    dict(tema='creme', olho='Como o NuPrato resolve', titulo='Receita guiada,<br><em>do começo ao&nbsp;fim.</em>',
         texto='Quantidade de água pra sua panela, tempo de fogo e o que fazer se der errado no meio.'),
    FIM,
]),

# 15. Ter 10/11 18:40, educação salvável, imagem única, carimbo (escuro)
('15-carne-descansa', [
    dict(tema='escuro', carimbo=('VERDADE', 'verdade'), t=92, titulo='"Carne tem que descansar <em>antes de&nbsp;cortar."</em>',
         texto='Uns 5 minutos fora do fogo e o caldo fica dentro da carne. Cortou na hora, ele escorre pro prato. <b>Vale pra bife grosso e carne assada.</b>',
         nota='paciência também é tempero'),
]),

# 16. Qua 11/11 18:40, mecanismo, capa antes e depois (creme)
('16-sem-forno', [
    dict(tema='creme', titulo='Sem forno? <em>A receita muda&nbsp;junto.</em>', t=86, cima=True,
         visual=par(ficha('Coxa com batata', ['forno a 200 graus', 'forma grande', 'uns 50 minutos', 'tudo de uma vez'], rot=-2, fita=False),
                    ficha('Coxa com batata', ['air fryer a 180 graus', 'cesto sem encher', 'uns 30 minutos', 'em 2 levas'], rot=1.5, fita=False),
                    rot_a='Receita de caderno', rot_b='Pra air fryer')),
    dict(tema='escuro', olho='O problema', titulo='Receita de forno <em>não ensina air&nbsp;fryer.</em>',
         texto='Cê copia o tempo do forno e vira chute: sai seco por fora ou cru perto do osso.'),
    dict(tema='creme', olho='O que muda', titulo='Menos graus, <em>menos&nbsp;tempo.</em>',
         texto='A air fryer é pequena e o ar quente passa perto da comida. Por isso costuma pedir menos graus e menos minutos.'),
    dict(tema='papel', olho='Não enche o cesto', titulo='Em 2 levas <em>fica&nbsp;crocante.</em>', cima=True,
         visual=ficha('Regra da air fryer', ['uma camada só', 'vira na metade do tempo', 'confere perto do osso'], rot=-1, rodape='caldo claro, tá pronto')),
    dict(tema='verde', olho='Como o NuPrato resolve', titulo='Cê fala o que tem. <em>Ele ajusta o&nbsp;tempo.</em>',
         texto='Forno, air fryer, fogão ou panela de pressão: a receita vem pro que tem na sua cozinha.'),
    FIM,
]),

# 17. Qui 12/11 18:40, educação salvável, capa número (verde)
('17-bolo-trocas', [
    dict(tema='verde', titulo='', centro=True,
         visual=numero('4', 'trocas no bolo: 3 que dão certo e 1 que não tem jeito', tam=440)),
    dict(tema='creme', olho='Antes de tudo', titulo='Bolo pede <em>mais&nbsp;cuidado.</em>',
         texto='Fermento e proporção mexem na química. Troca um trem de cada vez e não mexe na quantidade de farinha.'),
    dict(tema='papel', olho='Troca 1', titulo='Sem leite?', cima=True,
         visual=ficha('Faz assim', ['água ou suco de laranja', 'na mesma quantidade', 'bolo simples aceita bem'], rodape='fica mais leve')),
    dict(tema='creme', olho='Troca 2', titulo='Sem manteiga?', cima=True,
         visual=ficha('Faz assim', ['óleo', 'um pouco menos que a manteiga', 'entra junto com o líquido'], rot=1)),
    dict(tema='papel', olho='Troca 3', titulo='Sem açúcar refinado?', cima=True,
         visual=ficha('Faz assim', ['açúcar demerara ou mascavo', 'na mesma quantidade', 'bolo fica mais escuro'], rodape='e mais úmido')),
    dict(tema='escuro', olho='A que não tem jeito', titulo='Sem fermento, <em>não&nbsp;faz.</em>',
         texto='Sem fermento o bolo não cresce e fica pesado. Melhor comprar ou fazer outra sobremesa hoje.'),
    dict(tema='verde', olho='Pra qualquer receita', titulo='Cê conta o que faltou. <em>Ele adapta.</em>',
         texto='O NuPrato ajusta a receita pro que cê tem e explica o que mudou.'),
    FIM,
]),

# 18. Sex 13/11 18:40, comunidade, imagem única, conversa (creme)
('18-o-que-tem-pra-janta', [
    dict(tema='creme', titulo='Toda noite, a <em>mesma&nbsp;conversa:</em>', t=84,
         visual=conversa('Amor', [('ela', 'O que tem pra janta?', '19:41'), ('eu', 'Nada', '19:41'),
                                  ('ela', 'Tem ovo, arroz e meia cebola', '19:42'), ('eu', 'Então nada', '19:42')]),
         nota='marca quem responde assim'),
]),

# 19. Sáb 14/11 10:40, receita de fim de semana, capa texto (escuro)
('19-frango-sobrou', [
    dict(tema='escuro', selo='Fim de semana', t=112, titulo='Sobrou frango? <em>Vira 3&nbsp;pratos.</em>'),
    dict(tema='creme', olho='Antes', titulo='Desfia e <em>guarda bem&nbsp;fechado.</em>',
         texto='Frango cozido ou assado que sobrou dura uns 3 dias na geladeira. Desfiado, fica pronto pra virar outra coisa.'),
    dict(tema='papel', olho='Prato 1', titulo='Farofa de frango', cima=True,
         visual=ficha('Faz assim', ['cebola dourada na manteiga', 'frango desfiado', 'farinha de mandioca aos poucos', 'cheiro-verde no fim'], numero='19', rot=1)),
    dict(tema='verde', olho='Prato 2', titulo='Arroz com frango <em>de&nbsp;panela.</em>',
         texto='Refoga o frango com cebola, alho e tomate, junta o arroz pronto e mistura. Cheiro-verde por cima.'),
    dict(tema='papel', olho='Prato 3', titulo='Sanduíche de frango', cima=True,
         visual=ficha('Faz assim', ['frango desfiado', 'requeijão ou maionese', 'tomate e alface', 'pão francês'], rot=-1)),
    dict(tema='creme', olho='Faltou um trem?', titulo='Sem farinha de mandioca, <em>vai de&nbsp;milho.</em>',
         texto='Farofa de farinha de milho fica mais crocante. Cê conta o que tem e o NuPrato ajusta o resto.', nota='sábado resolvido'),
    FIM,
]),
]
