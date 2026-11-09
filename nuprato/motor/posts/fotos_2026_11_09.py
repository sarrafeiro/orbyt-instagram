"""Carrosséis com cenas reais (as mesmas geradas na Kairogen pro TikTok, Nano Banana 2.1), semana 09/11.
Pedido do Matheus em 09/11: 2 posts de feed por dia; parte deles com essas fotos.
python3 carrossel.py posts/fotos_2026_11_09.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha

CENAS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), 'tiktok', 'cenas')
def cena(nome, v=1): return f'{CENAS}/tiktok-carrossel__cena__{nome}__9x16__v{v}.jpg'

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 20. Qua 11/11 12:40, mecanismo
('20-ia-nao-cozinha', [
    dict(tema='foto', foto=cena('ia-cetica'), fy=30, t=96, titulo='IA não cozinha. <em>Quem cozinha é&nbsp;cê.</em>'),
    dict(tema='escuro', olho='Então pra que serve?', titulo='Pra resolver <em>o que trava a&nbsp;janta.</em>',
         texto='Faltou um trem, a receita é pra 6, cê só tem air fryer. É aí que a receita costuma desandar.'),
    dict(tema='papel', olho='Cê conta assim', titulo='Do jeito que&nbsp;fala.', cima=True,
         visual=ficha('O que cê quer comer hoje?', ['macarrão ao molho de tomate', 'pra 2 pessoas', 'sem extrato, tenho tomate'], numero='20', rot=1.2)),
    dict(tema='foto', foto=cena('ia-fogao', 2), fy=55, baixo=True, t=92, titulo='Ela adapta. <em>Cê vai pro&nbsp;fogão.</em>',
         texto='Passo a passo, do jeito da sua cozinha.'),
    dict(tema='verde', olho='Como funciona', titulo='Fala o prato. <em>Ela te guia até o&nbsp;fim.</em>',
         texto='Troca o que falta, ajusta quantidade e tempo e explica o que mudou.'),
    FIM,
]),

# 21. Qua 11/11 18:40, dor
('21-geladeira-quinta', [
    dict(tema='foto', foto=cena('quinta-geladeira'), fy=40, t=96, titulo='Geladeira assim<br><em>e fome&nbsp;agora.</em>'),
    dict(tema='creme', titulo='Parece nada. <em>É&nbsp;janta.</em>', t=96, cima=True,
         visual=ficha('O que tem aqui', [('o', 'ovo'), ('o', 'tomate'), ('o', 'queijo'), ('o', 'meia cebola')], rot=-1.2)),
    dict(tema='papel', olho='Ovo no molho de tomate', titulo='Uma panela só', cima=True,
         visual=ficha('Faz assim', ['refoga cebola e tomate picado', 'sal e um pouco de água', 'abre espaço e quebra os ovos', 'tampa até a clara firmar', 'queijo por cima'], numero='21', rot=1)),
    dict(tema='foto', foto=cena('quinta-sofa'), fy=55, baixo=True, t=88, titulo='Janta no sofá. <em>Sem&nbsp;delivery.</em>'),
    dict(tema='verde', olho='Como o NuPrato resolve', titulo='Cê conta o que tem. <em>Ele monta o&nbsp;prato.</em>',
         texto='E troca o que faltar no meio do caminho.'),
    FIM,
]),

# 22. Sex 13/11 12:40, dor e comunidade
('22-sexta-13', [
    dict(tema='foto', foto=cena('sexta13-fumaca'), fy=35, t=100, titulo='Sexta 13: <em>os sustos da&nbsp;cozinha.</em>'),
    dict(tema='foto', foto=cena('sexta13-arroz'), fy=45, baixo=True, olho='Susto 1', t=88, titulo='Arroz que <em>virou&nbsp;papa.</em>',
         texto='Água demais. Destampa, fogo baixo e deixa secar sem mexer.'),
    dict(tema='foto', foto=cena('sexta13-feijao'), fy=45, baixo=True, olho='Susto 2', t=88, titulo='Feijão <em>pegou no&nbsp;fundo.</em>',
         texto='Não raspa. Passa o de cima pra outra panela e o gosto de queimado fica pra trás.'),
    dict(tema='foto', foto=cena('sexta13-tropeiro'), fy=45, baixo=True, olho='Susto 3', t=88, titulo='Tropeiro <em>só de&nbsp;farinha.</em>',
         texto='Farinha demais, feijão de menos. A farinha entra aos poucos, mexendo.'),
    dict(tema='escuro', olho='Pra nenhum susto', titulo='Receita guiada <em>passo a&nbsp;passo.</em>',
         texto='Com o ponto de cada etapa e o que fazer se der errado no meio.', nota='qual foi o seu susto? comenta'),
    FIM,
]),

# 23. Sex 13/11 18:40, comunidade
('23-duvidaram', [
    dict(tema='foto', foto=cena('namorado-zoando'), fy=45, t=92, titulo='Quando duvidam <em>que cê sabe&nbsp;cozinhar.</em>'),
    dict(tema='creme', olho='O desafio', titulo='Frango, arroz e<br><em>o que sobrou na&nbsp;geladeira.</em>',
         texto='Sem receita de caderno e sem ninguém pra ligar.'),
    dict(tema='escuro', olho='A virada', titulo='Cê fala o que tem.<br><em>O NuPrato guia o&nbsp;resto.</em>',
         texto='Passo a passo, com a receita adaptada pra sua cozinha.'),
    dict(tema='foto', foto=cena('namorado-comendo', 2), fy=55, baixo=True, t=84, titulo='Pouco tempo depois: <em>repetiu o&nbsp;prato.</em>'),
    dict(tema='creme', titulo='Marca quem <em>duvidou de&nbsp;você.</em>', t=100, nota='ou quem sempre repete'),
    FIM,
]),

# 24. Dom 15/11 17:40, dor e mecanismo
('24-domingo', [
    dict(tema='foto', foto=cena('domingo-mesa'), fy=40, t=96, titulo='Almoço de domingo <em>na sua&nbsp;vez.</em>'),
    dict(tema='foto', foto=cena('domingo-mae'), fy=40, baixo=True, t=88, titulo='A receita tava <em>na cabeça da&nbsp;mãe.</em>',
         texto='Um pouco disso, o suficiente daquilo.'),
    dict(tema='escuro', olho='O problema', titulo='Ninguém <em>anotou&nbsp;nada.</em>',
         texto='E agora a lasanha é pra 8 pessoas, no forno da sua casa.'),
    dict(tema='papel', titulo='Cê conta pra quantos. <em>Ele faz a&nbsp;conta.</em>', t=80, cima=True,
         visual=ficha('Lasanha de domingo', ['pra 8 pessoas', 'carne moída, presunto e queijo', 'forno pequeno: 2 formas'], numero='24', rot=1)),
    dict(tema='foto', foto=cena('domingo-lasanha'), fy=50, baixo=True, t=96, titulo='Domingo <em>resolvido.</em>'),
    FIM,
]),
]
