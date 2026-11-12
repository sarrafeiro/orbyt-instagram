import sys; sys.path.insert(0,'/home/claude/insta-pessoal/v2')
from v2 import fluxo
SLUG='p05-crm-medqueen'
CARDS=[
 dict(fundo='escuro', titulo='Construí um CRM inteiro<br><b>em uma semana.</b>', pilula='Com a IA pilotando tudo', t=110),
 dict(pre='O problema da MedQueen', titulo='Quem se cadastrava<br><b>ficava sem conversa.</b>', t=96),
 dict(pre='Do escopo ao primeiro disparo', num='7', n=340, pilula='dias, de ponta a ponta'),
 dict(fundo='laranja', titulo='WhatsApp e e-mail<br><b>no automático.</b>', t=110),
 dict(titulo='Dispara <b>por evento.</b>', t=100, visual=fluxo(['Usuário age','Gatilho','Mensagem certa'])),
 dict(titulo='Filtra por<br><b>campanha e origem.</b>', pilula='Sabe de onde cada um veio', t=100),
 dict(fundo='escuro', pre='O meu papel', titulo='Eu falo a intenção.<br><b>A IA executa.</b>', pilula='Sem ler uma linha do sistema', t=104),
 dict(fundo='laranja', titulo='O que no teu negócio<br><b>ainda depende de você lembrar?</b>', pilula='Comenta aqui', t=92),
]
