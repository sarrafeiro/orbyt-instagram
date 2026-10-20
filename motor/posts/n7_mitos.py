import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
SLUG = 'n7-mitos'
CTA_ADV = 'Manda o nome do seu escritório no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CARDS = [
    dict(tipo='texto', tema='escuro', selo='Mito ou verdade', t=136, titulo='3 mitos sobre <em>site de advogado.</em>'),
    dict(carimbo=('MITO', 'mito'), titulo='"Advogado não pode ter site."',
         texto='Pode. O Provimento 205/2021 permite site com áreas de atuação, equipe, contato e conteúdo informativo. O que não pode é prometer resultado.', gigante=True, t=104, s=40, ponto=False),
    dict(tema='papel', carimbo=('MITO', 'mito'), titulo='"Site é caro e tem mensalidade."',
         texto='O site com modelo de advocacia custa R$ 797, uma vez só. Sem entrada e sem mensalidade.', gigante=True, t=104, s=40, ponto=False),
    dict(carimbo=('MITO', 'mito'), titulo='"Demora meses pra ficar pronto."',
         texto='Com o modelo de advocacia, fica pronto em até 2 dias úteis. E você só paga depois de aprovar.', gigante=True, t=104, s=40, ponto=False),
    dict(tema='laranja', carimbo=('VERDADE', 'verdade'), titulo='O cliente pesquisa você <em>antes de ligar.</em>',
         texto='Por isso o site precisa estar lá quando ele procurar.', gigante=True, t=104, s=40, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site do seu escritório, pronto em 2 dias úteis.', preco='R$ 797', preco_nota='preço fechado<br>pagamento único', checks=['Você só paga depois de aprovar', 'Seguindo o Provimento 205/2021', 'Sem entrada e sem mensalidade', 'O site fica no seu nome'], cta=CTA_ADV),
]
