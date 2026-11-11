"""Exemplo com um card de cada formato. Copie, troque o texto e rode:
python3 carrossel.py posts/exemplo_formatos.py
"""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, conversa, numero, busca, lista, tweet, checklist, par, ficha
import marca
SLUG = 'exemplo-formatos'
NOME = marca.M['nome_completo']
CARDS = [
    # 1. capa só texto gigante em fundo de destaque
    dict(tipo='texto', tema='destaque', selo='Como funciona', t=124,
         titulo='Gancho curto aqui. <em>A promessa em destaque.</em>', rodape='assunto · 5 passos'),
    # 2. número gigante
    dict(tema='escuro', olho='Passo 1', titulo='Um argumento <em>por card.</em>',
         visual=numero('2 dias', 'rótulo curto do número, uma linha ou duas.', tam=190), centro=True, ponto=False),
    # 3. print no celular
    dict(olho='Passo 2', titulo='Prova real: <em>print do produto.</em>', texto='Até 40 palavras de apoio.',
         visual=cel('adv2-cel-capa.png', ch=600), ponto=False),
    # 4. conversa de WhatsApp ('eu' = cliente, 'ela' = marca)
    dict(tema='papel', olho='Passo 3', titulo='Objeção numa <em>conversa.</em>',
         visual=conversa(NOME, [('eu', 'Pergunta real do cliente?', '09:12'), ('ela', 'Resposta curta e direta.', '09:14')])),
    # 5. tweet
    dict(olho='Passo 4', titulo='"A frase que o cliente <em>fala."</em>',
         visual=tweet('A resposta, com <em>o ponto principal</em> em destaque.'), centro=True, ponto=False),
    # 6. busca do Google
    dict(olho='Passo 5', titulo='O que ele <em>pesquisa.</em>',
         visual=busca('termo pesquisado', [('bom', 'Resultado bom', 'por que é bom'), ('ruim', 'Resultado ruim', 'por que espanta')]), ponto=False),
    # 7. checklist em papel
    dict(tema='papel', olho='Checklist', titulo='Salva e marca <em>quantos tem.</em>',
         visual=checklist(['Item um', 'Item dois', 'Item três'], marcados=1), centro=True, ponto=False),
    # 8. carimbo mito ou verdade
    dict(tema='escuro', carimbo=('MITO', 'mito'), titulo='"Frase que todo mundo <em>repete."</em>',
         texto='A explicação de por que não é bem assim.', ponto=False),
    # 9. lista salvável
    dict(olho='Resumo', titulo='Os pontos do post, <em>numa lista.</em>',
         visual=lista([('Ponto um', 'detalhe'), ('Ponto dois', 'detalhe'), ('Ponto três', 'detalhe')], 'num'), centro=True, ponto=False),
    # 10. final: preço, 4 checks e chamada
    dict(tipo='final', olho='Quanto custa', t=80, titulo='A oferta em uma frase.', preco='R$ 000', preco_nota='nota do preço<br>segunda linha',
         checks=['Benefício 1', 'Benefício 2', 'Benefício 3', 'Benefício 4'], cta='Chamada pro WhatsApp. <b>Link no perfil.</b>'),
]
