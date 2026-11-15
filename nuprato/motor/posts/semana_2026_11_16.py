"""Semana 16/11 a 22/11/2026 (tarefa semanal de 15/11). Ordem = ordem de publicação.
Calendário novo: 2 posts seg/qua/sex (12:40 e 18:40), 1 post ter/qui (18:40), sáb 10:40, dom 17:40.
Carrosséis com foto (cenas da Kairogen do TikTok): 26, 28 e 32.
python3 carrossel.py posts/semana_2026_11_16.py
"""
import os as _os, sys; sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from carrossel import ficha, busca, numero, lista

CENAS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), 'tiktok', 'cenas')
def cena(nome, v=1): return f'{CENAS}/tiktok-carrossel__cena__{nome}__9x16__v{v}.jpg'

FIM = dict(tipo='final', titulo='Bora fazer o seu?', texto='Fala o prato. O NuPrato adapta pra sua cozinha e te guia até o fim.')

POSTS = [
# 25. Seg 16/11 12:40, educação salvável, capa busca (creme)
('25-feijao-sem-pressao', [
    dict(tema='creme', titulo='Cê já pesquisou <em>isso&nbsp;aqui?</em>', t=86,
         visual=busca('feijão sem panela de pressão', [('ruim', 'Cozinha até ficar macio', 'quanto tempo? ninguém diz'), ('ruim', 'Receita que pede panela de barro', 'e cê só tem panela comum'), ('bom', 'Fala pro NuPrato o que cê tem', 'ele adapta pra panela comum')])),
    dict(tema='escuro', olho='Dá pra fazer?', titulo='Dá. Só pede <em>mais&nbsp;tempo.</em>',
         texto='Sem pressão, o feijão cozinha devagar. O segredo começa na véspera.'),
    dict(tema='papel', olho='Passo 1', titulo='De molho <em>na&nbsp;véspera.</em>', cima=True,
         visual=ficha('Faz assim', ['feijão catado e lavado', 'água fria cobrindo bem', 'de 8 a 12 horas', 'joga essa água fora'], numero='25', rot=1)),
    dict(tema='creme', olho='Passo 2', titulo='Panela comum, <em>fogo&nbsp;baixo.</em>',
         texto='Água nova cobrindo uns 3 dedos acima do feijão, tampa entreaberta. Feijão carioca costuma levar de 1h30 a 2h.'),
    dict(tema='papel', olho='Passo 3', titulo='Secou? <em>Água&nbsp;quente.</em>', cima=True,
         visual=ficha('No meio do caminho', ['confere a água a cada 20 minutos', 'completa com água quente', 'pronto quando amassa fácil'], rot=-1, rodape='água fria para o cozimento')),
    dict(tema='verde', olho='Passo 4', titulo='Tempero <em>no&nbsp;fim.</em>',
         texto='Refoga alho e cebola, junta uma concha do feijão amassado e volta tudo pra panela. Sal aí, provando.'),
    FIM,
]),

# 26. Seg 16/11 18:40, dor, capa foto (escuro)
('26-janta-pra-1', [
    dict(tema='foto', foto=cena('quinta-sofa-ele'), fy=50, t=92, titulo='Janta pra 1<br><em>sem sobrar a semana&nbsp;inteira.</em>'),
    dict(tema='escuro', olho='O problema', titulo='A receita é pra 4.<br><em>Cê é&nbsp;1.</em>',
         texto='Divide por 4 e esbarra no meio ovo, na pitada de sal e no tempo de panela.'),
    dict(tema='papel', olho='Macarrão pra 1', titulo='A conta que dá certo', cima=True,
         visual=ficha('Pra 1 pessoa', ['uns 100 g de macarrão', '1 dente de alho', '2 tomates maduros picados', 'queijo ralado por cima'], numero='26', rot=1)),
    dict(tema='creme', olho='Cuidado com o tempo', titulo='Molho menor <em>apura mais&nbsp;rápido.</em>',
         texto='Com metade da quantidade, o molho seca antes. O macarrão não: o tempo do pacote vale igual.'),
    dict(tema='verde', olho='Como o NuPrato resolve', titulo='Cê fala pra quantos. <em>Ele faz a&nbsp;conta.</em>',
         texto='Quantidade, tempo de panela e o que muda, explicado do seu jeito.', nota='sem marmita pra semana toda'),
    FIM,
]),

# 27. Ter 17/11 18:40, educação salvável, imagem única, carimbo (creme)
('27-lavar-arroz', [
    dict(tema='creme', carimbo=('VERDADE', 'verdade'), t=92, titulo='"Lavar o arroz <em>deixa&nbsp;soltinho."</em>',
         texto='Lavar tira o amido solto e o arroz gruda menos. <b>Mas o soltinho também vem de refogar o arroz no óleo antes da água e acertar a medida.</b>',
         nota='lava, escorre bem e refoga'),
]),

# 28. Qua 18/11 12:40, mecanismo, capa foto (escuro)
('28-fala-do-seu-jeito', [
    dict(tema='foto', foto=cena('ia-app'), fy=35, t=96, titulo='Cê fala o prato<br><em>do seu&nbsp;jeito.</em>'),
    dict(tema='papel', olho='Assim mesmo', titulo='Sem termo de&nbsp;chef.', cima=True,
         visual=ficha('O que cê falou', ['macarrão alho e óleo', 'pra 2 pessoas', 'não tenho azeite, só óleo', 'fogão de 4 bocas'], numero='28', rot=1.2)),
    dict(tema='escuro', olho='O que ele faz', titulo='Adapta e <em>explica o que&nbsp;mudou.</em>',
         texto='Óleo no lugar do azeite, alho no fogo baixo pra não amargar, quantidade pra 2.'),
    dict(tema='foto', foto=cena('ia-fogao'), fy=55, baixo=True, t=92, titulo='Cê vai pro fogão.<br><em>Ele guia o&nbsp;resto.</em>',
         texto='Um passo de cada vez, até o prato pronto.'),
    dict(tema='verde', olho='Como funciona', titulo='Fala o prato.<br><em>Conta o que&nbsp;tem.</em>',
         texto='Fogão, forno, air fryer ou panela de pressão: a receita vem pra sua cozinha.'),
    FIM,
]),

# 29. Qua 18/11 18:40, educação salvável, capa ficha (papel)
('29-pao-de-queijo', [
    dict(tema='papel', titulo='Pão de queijo de liquidificador:<br><em>o que&nbsp;troca?</em>', t=80, cima=True,
         visual=ficha('Pão de queijo', ['queijo: troca', 'polvilho doce ou azedo: troca', ('x', 'polvilho por farinha de trigo')], rot=1.2)),
    dict(tema='creme', olho='Antes de tudo', titulo='Pão de queijo <em>pede mais&nbsp;cuidado.</em>',
         texto='É massa de forno: troca um trem de cada vez e não mexe na quantidade de polvilho.'),
    dict(tema='papel', olho='Troca 1', titulo='Sem queijo minas?', cima=True,
         visual=ficha('Faz assim', ['queijo meia cura', 'ou parmesão ralado', 'na mesma quantidade'], rodape='parmesão deixa mais salgado', rot=-1)),
    dict(tema='creme', olho='Troca 2', titulo='Só tem polvilho&nbsp;doce?', cima=True,
         visual=ficha('Pode ir', ['só doce: cresce menos', 'só azedo: cresce mais', 'metade de cada: meio termo'], rot=1)),
    dict(tema='escuro', olho='A que não tem jeito', titulo='Farinha de trigo<br><em>não vira pão de&nbsp;queijo.</em>',
         texto='Sem polvilho, sai outra coisa. Melhor comprar o polvilho ou fazer outro lanche hoje.'),
    dict(tema='verde', olho='Pra qualquer receita', titulo='Cê conta o que faltou. <em>Ele&nbsp;adapta.</em>',
         texto='O NuPrato ajusta a receita pro que cê tem e explica o que mudou.'),
    FIM,
]),

# 30. Qui 19/11 18:40, educação salvável, capa número (verde)
('30-sete-trens', [
    dict(tema='verde', titulo='', centro=True,
         visual=numero('7', 'trens pra ter em casa e nunca ficar sem janta', tam=440)),
    dict(tema='creme', olho='A base', titulo='Arroz, feijão <em>e&nbsp;ovo.</em>',
         texto='Duram bastante na despensa e na geladeira, e com eles já sai prato de verdade.'),
    dict(tema='papel', olho='Os 7 trens', cima=True,
         visual=lista(['Arroz', 'Feijão', 'Ovo', 'Macarrão', 'Molho de tomate', 'Cebola e alho', 'Batata'])),
    dict(tema='escuro', olho='Com isso sai', titulo='Macarrão ao molho, <em>arroz com ovo,&nbsp;feijão.</em>',
         texto='E batata com ovo na frigideira quando a semana aperta.'),
    dict(tema='creme', olho='Faltou um trem?', titulo='A janta <em>muda&nbsp;junto.</em>',
         texto='Cê conta o que sobrou na despensa e o NuPrato monta o prato com isso.', nota='salva e confere no mercado'),
    FIM,
]),

# 31. Sex 20/11 12:40 (feriado), oferta e comunidade, capa texto (creme)
('31-prato-do-feriado', [
    dict(tema='creme', selo='Feriado', t=104, titulo='Qual vai ser<br>o prato <em>do&nbsp;feriado?</em>'),
    dict(tema='papel', olho='Escolhe um', titulo='Comenta o&nbsp;número', cima=True,
         visual=lista([('Frango com quiabo', 'sem baba'), ('Feijão tropeiro', 'do jeito mineiro'), ('Strogonoff', 'sem creme de leite')])),
    dict(tema='escuro', olho='Depois de escolher', titulo='Cê conta o que tem <em>e pra&nbsp;quantos.</em>',
         texto='O NuPrato adapta a receita pra sua cozinha e te guia passo a passo até o prato pronto.'),
    dict(tema='verde', olho='Por nossa conta', titulo='A 1ª receita guiada <em>é&nbsp;grátis.</em>',
         texto='Escolhe o prato do feriado. O link tá na bio.'),
    FIM,
]),

# 32. Sex 20/11 18:40 (feriado), dor, capa foto (escuro)
('32-sogra-almoco', [
    dict(tema='foto', foto=cena('sogra-mensagem'), fy=40, t=96, titulo='Sogra vem almoçar. <em>E&nbsp;agora?</em>'),
    dict(tema='escuro', olho='O pedido dela', titulo='Frango com quiabo. <em>E o quiabo sempre&nbsp;baba.</em>',
         texto='Pelo menos o seu. Dá pra evitar com 3 cuidados.'),
    dict(tema='papel', olho='Quiabo sem baba', titulo='Os 3 cuidados', cima=True,
         visual=ficha('Faz assim', ['lava e seca bem antes de cortar', 'refoga separado, fogo alto', 'umas gotas de limão'], numero='32', rot=1)),
    dict(tema='foto', foto=cena('sogra-fogao'), fy=55, baixo=True, t=88, titulo='Frango dourando, <em>quiabo&nbsp;separado.</em>',
         texto='Junta tudo só no fim.'),
    dict(tema='foto', foto=cena('sogra-repetindo'), fy=50, baixo=True, t=110, titulo='Ela <em>repetiu.</em>'),
    dict(tema='creme', olho='Como o NuPrato resolve', titulo='Cê fala o prato. <em>Ele te guia até o&nbsp;fim.</em>',
         texto='Com o ponto de cada etapa e o que fazer se der errado no meio.', nota='marca quem tem almoço com a sogra'),
    FIM,
]),

# 33. Sáb 21/11 10:40, receita de fim de semana, capa ficha (papel)
('33-panqueca', [
    dict(tema='papel', selo='Fim de semana', titulo='Panqueca de carne moída <em>no&nbsp;sábado.</em>', t=80, cima=True,
         visual=ficha('Pra 4 pessoas', ['1 xícara de farinha de trigo', '1 xícara de leite', '2 ovos e 1 colher de óleo', '500 g de carne moída'], numero='33', rot=-1.2)),
    dict(tema='creme', olho='Passo 1', titulo='Massa no <em>liquidificador.</em>',
         texto='Farinha, leite, ovos, óleo e uma pitada de sal. Bate até ficar lisa e sem grumo.'),
    dict(tema='papel', olho='Passo 2', titulo='Frigideira <em>untada,&nbsp;fina.</em>', cima=True,
         visual=ficha('Faz assim', ['meia concha por panqueca', 'gira pra espalhar', 'soltou a borda, vira'], rot=1, rodape='a primeira sempre sai feia')),
    dict(tema='escuro', olho='Passo 3', titulo='Recheio <em>bem&nbsp;sequinho.</em>',
         texto='Carne moída refogada com cebola, alho e tomate, até secar o caldo. Recheio molhado rasga a massa.'),
    dict(tema='creme', olho='Passo 4', titulo='Enrola, molho <em>e&nbsp;queijo.</em>',
         texto='Molho de tomate por cima, queijo e forno até derreter.'),
    dict(tema='verde', olho='Faltou um trem?', titulo='Sem forno, <em>tampa a&nbsp;frigideira.</em>',
         texto='Fogo baixo uns minutos e o queijo derrete igual. Cê conta o que tem e o NuPrato ajusta o resto.'),
    FIM,
]),

# 34. Dom 22/11 17:40, dor e receita, capa texto (escuro)
('34-sobrou-churrasco', [
    dict(tema='escuro', selo='Domingo', t=112, titulo='Sobrou churrasco? <em>Segunda tem&nbsp;carreteiro.</em>'),
    dict(tema='creme', olho='Antes de guardar', titulo='Pica a carne<br><em>e guarda&nbsp;fechado.</em>',
         texto='Carne e linguiça que sobraram, em pote fechado na geladeira. No outro dia viram janta.'),
    dict(tema='papel', olho='Arroz carreteiro', titulo='O que vai', cima=True,
         visual=ficha('Pra 4 pessoas', ['a carne que sobrou, picadinha', 'linguiça em rodela', '2 xícaras de arroz', 'cebola, alho e tomate'], numero='34', rot=1)),
    dict(tema='verde', olho='Faz assim', titulo='Doura a carne, <em>refoga o&nbsp;arroz.</em>',
         texto='Carne e linguiça na panela, depois cebola, alho e tomate. Junta o arroz, mexe e põe água quente.'),
    dict(tema='creme', olho='Ponto', titulo='Tampa e <em>fogo&nbsp;baixo.</em>',
         texto='Até secar a água e o arroz ficar macio. Cheiro-verde no fim.', nota='janta de segunda resolvida'),
    FIM,
]),
]
