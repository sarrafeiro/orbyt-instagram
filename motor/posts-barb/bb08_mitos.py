import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
# Carrossel só de argumento (sem print de celular). Base: posts/n7_mitos.py da advocacia.
SLUG = 'bb08-mitos'
CTA_BARB = 'Manda o nome da sua barbearia no WhatsApp. A gente monta o seu site sem custo e você só paga se aprovar. <b>Link no perfil.</b>'
CHECKS = ['Você só paga depois de aprovar', 'Agendar pelo app ou pelo WhatsApp', 'Sem entrada e sem mensalidade', 'O site fica no seu nome']
CARDS = [
    dict(tipo='texto', tema='escuro', selo='Mito ou verdade', t=136, titulo='3 mitos sobre <em>site de barbearia.</em>'),
    dict(carimbo=('MITO', 'mito'), titulo='"O boca a boca já resolve."',
         texto='A indicação traz o seu nome. Antes de ir, o cliente procura. Se não acha preço nem foto do corte, vai na barbearia que mostrou.', gigante=True, t=104, s=40, ponto=False),
    dict(tema='papel', carimbo=('MITO', 'mito'), titulo='"Site é coisa de barbearia grande."',
         texto='Quem tem uma cadeira só é quem mais precisa: o site atende enquanto você corta. R$&nbsp;399, uma vez só.', gigante=True, t=104, s=40, ponto=False),
    dict(carimbo=('MITO', 'mito'), titulo='"Cliente de barbearia não pesquisa."',
         texto='Pesquisa sim. Ele digita "barbearia perto de mim" e compara preço, foto e avaliação antes de escolher.', gigante=True, t=104, s=40, ponto=False),
    dict(tema='laranja', carimbo=('VERDADE', 'verdade'), titulo='O seu corte vende sozinho. <em>Quando o cliente consegue ver.</em>',
         texto='No site, o antes e depois fica logo na primeira rolagem.', gigante=True, t=96, s=40, ponto=False),
    dict(tipo='final', olho='Quanto custa', t=80, titulo='Site da sua barbearia, pronto em 2 dias úteis.', preco='R$ 399', preco_nota='preço fechado<br>pagamento único', checks=CHECKS, cta=CTA_BARB),
]
