import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import cel, lista
SLUG = 'b06-adv-google'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
LUPA = '<svg viewBox="0 0 24 24" fill="none" stroke="#59606A" stroke-width="2.4" style="width:30px;height:30px;flex:none"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'
def sugestoes(q, itens):
    r = ''.join(f'<div class="res"><i style="background:#E6EAEE">{LUPA}</i><div><b style="color:#16181B;font-weight:500">{a}</b></div></div>' for a in itens)
    return f'<div class="busca"><div class="campo">{LUPA}{q}</div>{r}</div>'
def campo(q):
    return f'<div class="busca" style="padding-bottom:30px"><div class="campo">{LUPA}{q}</div></div>'
def pilha(q, img, ch):
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:34px;width:100%;height:100%">{campo(q)}'
            f'<div style="flex:1;min-height:0;display:flex;justify-content:center;width:100%">{cel(img, ch=ch)}</div></div>')
CARDS = [
    dict(tipo='capa', olho='Advocacia', t=96,
         titulo='Advogado, olha o que o seu cliente <em>digita no Google.</em>',
         texto='Cada tipo de pesquisa pede uma coisa do seu site.',
         visual=sugestoes('advogado', ['advogado trabalhista em bh', 'advogado perto de mim', 'quanto tempo demora um processo trabalhista', 'aposentadoria negada pelo inss o que fazer']), ponto=False),
    dict(olho='Pesquisa 1', titulo='Área e cidade <em>escritas no site.</em>',
         texto='É assim que o Google entende que você atende aquele assunto naquela cidade.',
         visual=pilha('advogado trabalhista em bh', 'adv1-cel-areas.png', 520), ponto=False),
    dict(olho='Pesquisa 2', titulo='Endereço e WhatsApp <em>a um toque.</em>',
         texto='Quem pesquisa "perto de mim" quer ir até você ou falar agora.',
         visual=pilha('advogado perto de mim', 'adv2-cel-capa.png', 520), ponto=False),
    dict(olho='Pesquisa 3', titulo='A dúvida dele <em>respondida no site.</em>',
         texto='Perguntas frequentes informativas, seguindo o Provimento 205/2021. Ele lê e já sabe quem procurar.',
         visual=pilha('quanto tempo demora um processo', 'adv1-cel-duvidas.png', 500), ponto=False),
    dict(olho='Pesquisa 4', titulo='Um conteúdo <em>para cada assunto.</em>',
         texto='Artigo sobre o tema que o cliente pesquisa, com o seu escritório como autor.',
         visual=pilha('aposentadoria negada pelo inss', 'adv1-cel-conteudo.png', 500), ponto=False),
    dict(olho='Resumo', titulo='Salva pra conferir no seu.',
         visual=lista([('Área e cidade escritas', 'O Google entende o que você atende e onde'),
                       ('Endereço e WhatsApp a um toque', 'Pra quem quer falar agora'),
                       ('Perguntas frequentes', 'Informativas, dentro das regras'),
                       ('Um conteúdo por assunto', 'Artigos com o seu escritório como autor')], 'pode'), centro=True, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80,
         titulo='Site do seu escritório, pronto em 2 dias úteis.',
         preco='R$ 797', preco_nota='preço fechado<br>pagamento único',
         checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'],
         cta=CTA_ADV),
]
