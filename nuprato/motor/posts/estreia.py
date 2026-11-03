"""Estreia do @nuprato.app: 9 carrosséis de venda de conceito (sem print do app, sem reel).
Ordem = ordem de publicação. Na grade, o 9 fica no canto de cima à esquerda.
python3 carrossel.py posts/estreia.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha, par, conversa, busca, numero, lista

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 1. Manifesto (capa texto gigante, verde)
('01-manifesto', [
    dict(tema='verde', selo='Manifesto', t=118, titulo='Livro de receita é <em>trem do passado.</em>'),
    dict(tema='creme', olho='O problema', titulo='A receita foi escrita pra <em>outra cozinha.</em>',
         texto='Outra panela, outro fogão, outra despensa. Aí falta um trem e a janta trava.'),
    dict(tema='papel', olho='Toda casa já viveu isso', titulo='Cê abre a receita e…', cima=True,
         visual=ficha('Strogonoff de frango', [('x', 'creme de leite'), ('x', 'champignon'), 'frango', 'cebola'], numero='01',
                      rodape='faltaram 2 de 4. E agora?', ruim=True)),
    dict(tema='escuro', olho='A virada', titulo='E se a receita <em>se adaptasse a você?</em>',
         texto='Cê fala o que quer comer. O NuPrato entende o que tem aí e ajusta a receita na hora.'),
    dict(tema='creme', olho='O que muda', titulo='Um livro de receita <em>infinito.</em>',
         texto='Qualquer prato, do seu jeito, com o que cê tem. <b>Sem papo de chef nem frescura.</b>'),
    FIM,
]),

# 2. Geladeira (capa checklist em papel)
('02-geladeira', [
    dict(tema='papel', titulo='Abriu a geladeira e <em>só tem isso?</em>', t=88, cima=True,
         visual=ficha('O que tem aqui', [('o', 'arroz de ontem'), ('o', '3 ovos'), ('o', '1 tomate'), ('o', 'um pedaço de queijo')], rot=1.2)),
    dict(tema='creme', olho='Spoiler', titulo='Isso aí <em>já é janta.</em>',
         texto='A maioria das casas tem o básico. O que falta é alguém dizer o que fazer com ele.'),
    dict(tema='verde', olho='Com esses 4 trens', titulo='Dá pra fazer:', cima=True,
         visual=lista([('Arroz de forno', 'na frigideira tampada, se não tiver forno'), ('Bolinho de arroz', 'com o ovo e o queijo'), ('Omelete recheada', 'com o tomate e o queijo')])),
    dict(tema='creme', olho='Como o NuPrato resolve', titulo='Cê conta o que tem. <em>Ele monta o prato.</em>',
         texto='E ainda avisa o que dá pra trocar se faltar alguma coisa no meio do caminho.'),
    dict(tema='papel', titulo='Salva esse post pra <em>próxima geladeira vazia.</em>', nota='antes de pedir delivery, olha aqui'),
    FIM,
]),

# 3. Mito ou verdade (capa carimbo, escuro)
('03-mito-risca', [
    dict(tema='escuro', carimbo=('MITO', 'mito'), t=96, titulo='"Tem que seguir a receita <em>à risca."</em>',
         texto='Receita é ponto de partida. Quantidade, ingrediente e panela dá pra adaptar. <b>Bolo e pão pedem mais cuidado.</b>',
         nota='o NuPrato adapta e te fala o porquê'),
]),

# 4. 5 trocas (capa número gigante, creme)
('04-cinco-trocas', [
    dict(tema='creme', visual=numero('5', 'trocas que salvam a janta quando falta um trem', tam=440), titulo='', centro=True),
    dict(tema='papel', olho='Troca 1', titulo='Sem creme de leite?', cima=True,
         visual=ficha('Faz assim', ['leite', 'um pouco de amido de milho', 'engrossa no fogo baixo'], rodape='fica cremoso igual')),
    dict(tema='creme', olho='Troca 2', titulo='Sem farinha de rosca?', cima=True,
         visual=ficha('Faz assim', ['bolacha cream cracker', 'esfarelada no pilão ou no saco', 'empana do mesmo jeito'], rot=1)),
    dict(tema='papel', olho='Troca 3', titulo='Sem extrato de tomate?', cima=True,
         visual=ficha('Faz assim', ['tomate bem maduro', 'picado sem semente', 'apura no fogo até virar molho'])),
    dict(tema='creme', olho='Troca 4', titulo='Sem panela de pressão?', cima=True,
         visual=ficha('Faz assim', ['panela comum tampada', 'mais água e mais tempo', 'feijão de molho na véspera'], rot=1)),
    dict(tema='papel', olho='Troca 5', titulo='Sem forno?', cima=True,
         visual=ficha('Faz assim', ['air fryer, temperatura menor', 'ou frigideira tampada', 'fogo baixo e paciência'])),
    dict(tema='verde', olho='Pra cada receita', titulo='O NuPrato acha a <em>troca certa</em> pra&nbsp;você.',
         texto='Cê fala o que faltou. Ele ajusta quantidade, tempo e modo de fazer.'),
    FIM,
]),

# 5. Conversa com a mãe (capa WhatsApp, verde)
('05-um-tiquinho', [
    dict(tema='verde', titulo='Toda receita de mãe <em>é&nbsp;assim:</em>', t=84,
         visual=conversa('Mãe', [('eu', 'Mãe, quanto de sal no feijão?', '19:02'), ('ela', 'Um tiquinho, filho. Vai pondo e provando', '19:05'), ('eu', 'Quanto é um tiquinho??', '19:05')])),
]),

# 6. Antes e depois (capa par de fichas, papel)
('06-caderno-x-nuprato', [
    dict(tema='papel', titulo='A mesma receita. <em>Dois finais.</em>', t=86, cima=True,
         visual=par(ficha('Escondidinho', [('x', 'aipim'), ('x', 'carne seca'), ('x', 'forno'), 'queijo'], rot=-2, fita=False),
                    ficha('Escondidinho', ['batata', 'carne moída', 'air fryer', 'queijo'], rot=1.5, fita=False))),
    dict(tema='creme', olho='Receita de caderno', titulo='Ela pede o que <em>cê não tem.</em>',
         texto='E não diz o que fazer quando falta. Cê desiste ou vai no mercado às 20h.'),
    dict(tema='verde', olho='Receita NuPrato', titulo='Ela parte do que <em>tem na sua casa.</em>',
         texto='Mesma ideia de prato, com os ingredientes e o equipamento que cê tem hoje.'),
    dict(tema='creme', olho='E não para na lista', titulo='Te acompanha <em>até o prato pronto.</em>',
         texto='Cada passo explicado, sem palavra de chef, com o que fazer se der errado no meio.'),
    FIM,
]),

# 7. Busca do Google (capa busca, escuro)
('07-busca-strogonoff', [
    dict(tema='escuro', titulo='Cê já pesquisou <em>isso aqui?</em>', t=86,
         visual=busca('strogonoff sem creme de leite', [('ruim', 'Strogonoff da vovó (receita original)', '3 páginas de história antes da receita'), ('ruim', '"Substituí por iogurte e talhou"', 'comentário de quem tentou'), ('bom', 'Fala pro NuPrato o que cê tem', 'ele adapta a receita pra sua cozinha')])),
    dict(tema='creme', olho='O que acontece', titulo='Cada site fala <em>uma coisa.</em>',
         texto='Cê junta 3 receitas, 2 comentários e um vídeo. No fim, inventa e torce.'),
    dict(tema='papel', olho='A resposta que cê queria', titulo='Uma só, <em>pra sua cozinha.</em>', cima=True,
         visual=ficha('Strogonoff sem creme de leite', ['leite + amido de milho', 'entra no fim, fogo baixo', 'não deixa ferver'], numero='04', rodape='fica cremoso, sem talhar')),
    dict(tema='creme', olho='Por que funciona', titulo='O NuPrato pergunta <em>antes de responder.</em>',
         texto='Quantas pessoas, que panela cê tem, o que tem na geladeira. Aí sim monta a receita.'),
    FIM,
]),

# 8. Como funciona (capa ficha de papel, creme)
('08-como-funciona', [
    dict(tema='creme', selo='Como funciona', titulo='Cê fala o prato. <em>A&nbsp;gente resolve o resto.</em>', t=84, cima=True,
         visual=ficha('O que cê quer comer hoje?', ['frango com batata', 'pra 3 pessoas', 'só tenho air fryer'], numero='01', rot=1.5)),
    dict(tema='papel', olho='Passo 1', titulo='Fala o que <em>quer comer.</em>',
         texto='O nome do prato, uma vontade ou só "o que dá pra fazer com frango?". Do jeito que cê falaria com alguém.'),
    dict(tema='creme', olho='Passo 2', titulo='Conta o que <em>tem aí.</em>',
         texto='Ingredientes, quantas pessoas vão comer e o que tem na cozinha: fogão, forno, air fryer, panela de pressão.'),
    dict(tema='papel', olho='Passo 3', titulo='A IA <em>adapta a receita.</em>',
         texto='Troca o que falta, ajusta a quantidade e o tempo. E te fala o que mudou e por quê.'),
    dict(tema='creme', olho='Passo 4', titulo='Te guia <em>até o prato pronto.</em>',
         texto='Um passo de cada vez, sem termo de chef, com o que fazer se der errado no meio.'),
    FIM,
]),

# 9. Oferta (capa texto gigante, verde)
('09-primeira-gratis', [
    dict(tipo='final', titulo='Sua 1ª receita é <em>por nossa conta.</em>', t=96,
         texto='Escolhe o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.'),
]),
]
