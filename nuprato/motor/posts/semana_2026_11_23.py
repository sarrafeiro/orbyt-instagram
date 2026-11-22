"""Semana 23/11 a 29/11/2026 (tarefa semanal de 22/11). Ordem = ordem de publicação.
Calendário: 2 posts seg/qua/sex (12:40 e 18:40), 1 post ter/qui (18:40), sáb 10:40, dom 17:40.
Carrosséis com foto: só 38 e 44 (Kairogen sem crédito em 22/11; usadas as 2 últimas cenas inéditas).
python3 carrossel.py posts/semana_2026_11_23.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha, busca, numero, lista, par

CENAS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), 'tiktok', 'cenas')
def cena(nome, v=1): return f'{CENAS}/tiktok-carrossel__cena__{nome}__9x16__v{v}.jpg'

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 35. Seg 23/11 12:40, educação salvável, capa carimbo MITO (creme)
('35-oleo-macarrao', [
    dict(tema='creme', carimbo=('MITO', 'mito'), t=92, titulo='"Óleo na água <em>não deixa o macarrão&nbsp;grudar."</em>'),
    dict(tema='escuro', olho='Por que é mito', titulo='O óleo fica <em>boiando&nbsp;em&nbsp;cima.</em>',
         texto='O macarrão cozinha lá embaixo, na água. O óleo não chega nele na hora que importa.'),
    dict(tema='papel', olho='O que funciona', titulo='Macarrão soltinho', cima=True,
         visual=ficha('Faz assim', ['bastante água na panela', 'água fervendo forte antes', 'sal na água', 'mexe nos primeiros minutos'], numero='35', rot=1)),
    dict(tema='creme', olho='E tem mais', titulo='Óleo faz o molho <em>escorrer&nbsp;da&nbsp;massa.</em>',
         texto='Macarrão oleoso não segura o molho. Escorreu? Já mistura com o molho, sem deixar parado no escorredor.'),
    dict(tema='verde', olho='Pra qualquer prato', titulo='Cê fala o prato. <em>Ele dá o&nbsp;ponto.</em>',
         texto='O NuPrato te guia passo a passo, com o ponto de cada etapa.', nota='salva pro próximo macarrão'),
    FIM,
]),

# 36. Seg 23/11 18:40, dor, capa texto gigante (grafite)
('36-mexidao', [
    dict(tema='escuro', selo='Segunda cansada', t=108, titulo='Cansou?<br><em>Mexidão&nbsp;resolve.</em>'),
    dict(tema='creme', olho='O problema', titulo='Chegou tarde <em>e a fome não&nbsp;espera.</em>',
         texto='Cozinhar do zero agora? Nem pensar. Mas a geladeira ainda tem o arroz e o feijão de ontem.'),
    dict(tema='papel', olho='Mexidão', titulo='O que vai', cima=True,
         visual=ficha('Pra 2 pessoas', ['arroz de ontem', 'feijão de ontem, sem muito caldo', '2 ovos', 'meia cebola picada'], numero='36', rot=-1, rodape='tem linguiça ou couve? entra também')),
    dict(tema='verde', olho='Faz assim', titulo='Refoga, junta <em>e mexe&nbsp;tudo.</em>',
         texto='Cebola no óleo até dourar. Junta o arroz e o feijão. Abre um espaço, mexe os ovos ali e mistura tudo.'),
    dict(tema='creme', olho='Faltou um trem?', titulo='A janta <em>se&nbsp;ajeita.</em>',
         texto='Cê conta o que sobrou na geladeira e o NuPrato monta o prato com isso.', nota='janta de segunda resolvida'),
    FIM,
]),

# 37. Ter 24/11 18:40, educação salvável, capa número (creme)
('37-bife-duro', [
    dict(tema='creme', titulo='', centro=True,
         visual=numero('3', 'erros que deixam o bife duro e sem cor', tam=440)),
    dict(tema='escuro', olho='Erro 1', titulo='Frigideira <em>fria.</em>',
         texto='Bife em frigideira morna solta água e cozinha em vez de dourar. Espera esquentar bem antes.'),
    dict(tema='creme', olho='Erro 2', titulo='Bife <em>demais de uma&nbsp;vez.</em>',
         texto='Frigideira lotada esfria e vira sopa de carne. Faz em levas, com espaço entre eles.'),
    dict(tema='papel', olho='Erro 3', titulo='Mexe <em>toda&nbsp;hora.</em>', cima=True,
         visual=ficha('Faz assim', ['põe e deixa quieto', 'vira uma vez só', 'quando soltar sozinho'], rot=1, rodape='garfo furando escorre o caldo')),
    dict(tema='verde', olho='Pra qualquer carne', titulo='Cê fala o prato. <em>Ele dá o ponto de cada&nbsp;etapa.</em>',
         texto='O NuPrato te guia passo a passo até o prato pronto.'),
    FIM,
]),

# 38. Qua 25/11 12:40, mecanismo, capa foto (escuro)
('38-tinha-isso', [
    dict(tema='foto', foto=cena('namorado-comendo'), fy=88, t=92, titulo='Tinha macarrão,<br><em>frango e meio&nbsp;tomate.</em>'),
    dict(tema='papel', olho='Cê fala assim', titulo='Do jeito que&nbsp;tá.', cima=True,
         visual=ficha('O que cê contou', ['macarrão', 'sobra de frango', 'meio tomate e uma cebola', 'janta pra 2'], numero='38', rot=1.2)),
    dict(tema='escuro', olho='O que ele faz', titulo='Monta o prato <em>com o que&nbsp;tem.</em>',
         texto='Frango desfiado no molho de tomate com cebola, macarrão no ponto do pacote. E explica o que mudou.'),
    dict(tema='creme', olho='Até o fim', titulo='Um passo <em>de cada&nbsp;vez.</em>',
         texto='Do refogado ao prato servido, com o ponto de cada etapa.'),
    dict(tema='verde', olho='Como funciona', titulo='Fala o prato.<br><em>Conta o que&nbsp;tem.</em>',
         texto='Quantas pessoas, o que tem na geladeira e na cozinha. A receita vem pra sua casa.'),
    FIM,
]),

# 39. Qua 25/11 18:40, educação salvável, capa antes e depois (papel)
('39-carne-de-panela', [
    dict(tema='papel', titulo='Sem panela de pressão? <em>Carne de panela&nbsp;sai.</em>', t=80, cima=True,
         visual=par(ficha('Carne de panela', ['panela de pressão', 'uns 40 minutos', 'depois de pegar pressão'], rot=-2, fita=False),
                    ficha('Carne de panela', ['panela comum tampada', 'de 2h a 2h30', 'fogo baixo'], rot=1.5, fita=False),
                    rot_a='Como vem', rot_b='Pra panela comum')),
    dict(tema='escuro', olho='O problema', titulo='A receita <em>só fala da&nbsp;pressão.</em>',
         texto='E cê copia o tempo pra panela comum e a carne sai dura. Muda o tempo, muda o cuidado.'),
    dict(tema='creme', olho='Passo 1', titulo='Doura <em>bem&nbsp;antes.</em>',
         texto='Acém ou músculo em pedaços, em levas, até dourar. Depois cebola, alho e tomate no mesmo fundo.'),
    dict(tema='papel', olho='Passo 2', titulo='Fogo baixo <em>e&nbsp;tampa.</em>', cima=True,
         visual=ficha('No meio do caminho', ['água quente até quase cobrir', 'confere a cada 20 minutos', 'secou? mais água quente'], rot=-1, rodape='pronto quando desmancha no garfo')),
    dict(tema='verde', olho='Pra sua cozinha', titulo='Cê conta a panela que tem. <em>Ele ajusta o&nbsp;tempo.</em>',
         texto='Fogão, forno, air fryer ou pressão: o NuPrato adapta a receita e explica o que mudou.'),
    FIM,
]),

# 40. Qui 26/11 18:40, educação salvável, capa busca (grafite)
('40-sobrou-feijao', [
    dict(tema='escuro', titulo='Cê já pesquisou <em>isso&nbsp;aqui?</em>', t=86,
         visual=busca('o que fazer com feijão que sobrou', [('ruim', 'Jogar fora', 'feijão de 2 dias ainda vira janta'), ('ruim', 'Comer igual a semana toda', 'enjoa no terceiro dia'), ('bom', 'Fala pro NuPrato o que sobrou', 'ele monta o prato com isso')])),
    dict(tema='creme', olho='Antes de tudo', titulo='Guarda <em>fechado e&nbsp;gelado.</em>',
         texto='Pote fechado na geladeira assim que esfriar. Feijão guardado assim aguenta uns 3 dias.'),
    dict(tema='papel', olho='Jeito 1', titulo='Tutu de&nbsp;feijão', cima=True,
         visual=ficha('Faz assim', ['refoga alho e cebola', 'junta o feijão amassado', 'farinha de mandioca aos poucos'], numero='40', rot=1, rodape='mexe até soltar da panela')),
    dict(tema='verde', olho='Jeito 2', titulo='Caldinho <em>de&nbsp;feijão.</em>',
         texto='Bate o feijão com o caldo no liquidificador, ferve com alho refogado e termina com cheiro-verde.'),
    dict(tema='creme', olho='Jeito 3', titulo='Sopa com <em>macarrão&nbsp;miúdo.</em>',
         texto='Feijão batido com água, ferve e o macarrão cozinha direto no caldo. Janta de frio.'),
    dict(tema='escuro', olho='Sobrou outro trem?', titulo='Cê conta o que tem. <em>Ele monta o&nbsp;prato.</em>',
         texto='O NuPrato adapta a receita pra sobra da sua geladeira.', nota='qual dos 3 cê faria hoje?'),
    FIM,
]),

# 41. Sex 27/11 12:40, educação salvável, capa texto gigante (creme)
('41-black-friday', [
    dict(tema='creme', selo='Black Friday', t=100, titulo='O que vale estocar <em>na&nbsp;cozinha.</em>'),
    dict(tema='papel', olho='Dura bastante', titulo='Os trens da&nbsp;despensa', cima=True,
         visual=lista(['Arroz e feijão', 'Macarrão', 'Óleo e sal', 'Molho de tomate', 'Farinha de mandioca'])),
    dict(tema='escuro', olho='Regra 1', titulo='Compra o que <em>cê já&nbsp;usa.</em>',
         texto='Promoção de trem que cê nunca cozinha vira coisa vencida no fundo do armário.'),
    dict(tema='creme', olho='Regra 2', titulo='Olha <em>a&nbsp;validade.</em>',
         texto='Estoque bom é o que dá tempo de usar. Os mais antigos vão pra frente do armário.', nota='os novos vão pro fundo'),
    dict(tema='verde', olho='Encheu a despensa?', titulo='Cê conta o que tem. <em>Ele monta a&nbsp;janta.</em>',
         texto='O NuPrato adapta a receita pro que tá no seu armário.'),
    FIM,
]),

# 42. Sex 27/11 18:40, comunidade e receita, capa ficha (verde)
('42-pizza-frigideira', [
    dict(tema='verde', selo='Sexta à noite', titulo='Pizza <em>de&nbsp;frigideira.</em>', t=96, cima=True,
         visual=ficha('Massa pra 1 frigideira', ['1 xícara de farinha de trigo', 'meia xícara de leite', '1 ovo e 2 colheres de óleo', '1 colher de chá de fermento químico'], numero='42', rot=-1.2)),
    dict(tema='creme', olho='Passo 1', titulo='Mistura <em>até&nbsp;ficar&nbsp;lisa.</em>',
         texto='Farinha, leite, ovo, óleo e uma pitada de sal. O fermento entra por último, só misturando.'),
    dict(tema='escuro', olho='Passo 2', titulo='Fogo baixo <em>e&nbsp;tampa.</em>',
         texto='Espalha na frigideira untada e tampa. Fogo alto queima embaixo e deixa cru em cima.'),
    dict(tema='papel', olho='Passo 3', titulo='Vira e <em>monta.</em>', cima=True,
         visual=ficha('Por cima', ['molho de tomate', 'queijo', 'o que tiver: presunto, tomate, milho'], rot=1, rodape='tampa até o queijo derreter')),
    dict(tema='creme', olho='Massa pede cuidado', titulo='Leva fermento: <em>mede&nbsp;certinho.</em>',
         texto='Massa com fermento não aceita chute. Sem forno nenhum, a frigideira dá conta.', nota='comenta o sabor da sua'),
    FIM,
]),

# 43. Sáb 28/11 10:40, oferta, capa texto gigante (creme)
('43-prato-do-sabado', [
    dict(tema='creme', selo='Sábado', t=100, titulo='O prato do sábado <em>é cê que&nbsp;escolhe.</em>'),
    dict(tema='papel', olho='Como funciona', titulo='Em 3 passos', cima=True,
         visual=lista([('Fala o prato', 'do seu jeito'), ('Conta o que tem', 'e pra quantos'), ('Vai pro fogão', 'com o passo a passo')])),
    dict(tema='escuro', olho='Por exemplo', titulo='"Arroz com frango pra 5, <em>panela&nbsp;comum."</em>',
         texto='O NuPrato adapta a quantidade, o tempo e o que faltar, e explica o que mudou.'),
    dict(tema='verde', olho='Por nossa conta', titulo='A 1ª receita guiada <em>é&nbsp;grátis.</em>',
         texto='Escolhe o prato do almoço. O link tá na bio.'),
    FIM,
]),

# 44. Dom 29/11 17:40, dor e educação, capa foto (escuro)
('44-receita-dobrada', [
    dict(tema='foto', foto=cena('sogra-abraco'), fy=22, t=88, titulo='Vem a família toda?<br><em>A receita dobra.</em><br><em>O sal&nbsp;não.</em>'),
    dict(tema='escuro', olho='O problema', titulo='Dobrou as pessoas, <em>dobrou&nbsp;tudo?</em>',
         texto='Ingrediente dobra. Sal e tempero não precisam: dobrar direto costuma passar do ponto.'),
    dict(tema='papel', olho='Pra dobrar a receita', titulo='O que muda', cima=True,
         visual=ficha('Faz assim', ['ingredientes: dobra', 'sal: começa com menos e prova', 'panela maior: demora mais pra ferver', 'forno: confere antes do tempo'], numero='44', rot=1)),
    dict(tema='creme', olho='Panela cheia', titulo='Mais comida <em>pede mais&nbsp;tempo.</em>',
         texto='Panela cheia demora pra ferver e cozinha mais devagar. Vai pelo ponto, não pelo relógio.'),
    dict(tema='verde', olho='Como o NuPrato resolve', titulo='Cê fala pra quantos. <em>Ele refaz a&nbsp;conta.</em>',
         texto='Quantidade, tempero e tempo ajustados pra sua mesa.', nota='marca quem cozinha pra família toda'),
    FIM,
]),
]
