# Brand do Instagram @matheusmiranda.ia

Tudo que é só deste perfil fica aqui. O processo geral de trabalho (vale pra qualquer Instagram) está na skill de Instagram. Atualizado em 12/11/2026.

## Perfil
- Conta: @matheusmiranda.ia, nome de exibição Matheus Miranda. TikTok com o mesmo @.
- Posicionamento: IA na prática pra quem vende e toca negócio.
- Trypost: social_account_id 01a1ccb1-39cc-70ae-b211-a584f1f072d3.
- Navegador: Chrome "Browser 1".
- Mídia: repositório sarrafeiro/orbyt-instagram, pasta matheusmiranda/ (posts, stories, reels, personagem, v2).

## Conteúdo
- Tema vem do que o Matheus construiu de verdade: CRM da MedQueen, pesquisa de ICP com prospecção (30 pessoas novas por dia em todos os perfis), sites em 15 minutos (barbearia, advocacia, consultório na Alemanha, LPs dos produtos), sistema de afiliados, automações, os produtos (MedQueen, NuPrato, PromoSnap).
- Nada de tema pequeno: limpar seguidores, dica genérica ou pesquisa de palavra-chave sozinha foram reprovados.
- Número só o que ele disse ou o que foi medido. Nunca repetir no carrossel o tema de um Reel já gravado.
- PromoSnap: citar o que é, sem gastar tempo nele.

## Carrossel A: padrão centralizado (principal)
- Motor: motor-v2/carrossel_v2.py com MARCA_JSON=matheusmiranda/marca-v2.json.
- Cores: azul-marinho #1E2B4A, creme #FCF4E1, laranja #E2492F (destaque), branco. Uma cor de destaque só.
- Fundos alternando marinho, creme e laranja.
- Reprovado: gradiente, faixa colorida atravessando os cards, kit azul elétrico antigo, texto alinhado à esquerda no topo com espaço vazio embaixo, parágrafo no card.
- Referências que ele aprovou: @onsideag (centralizado, pouco texto) e os carrosséis recentes do @orbytstudio_ (um argumento por card).

## Carrossel B: tirinha com o personagem
- Personagem e estilo: claude/40-personagem-matheusmiranda-ia.md no projeto, PERSONAGEM.md e render.py em matheusmiranda/personagem.
- Mistura card só texto com card ilustrado. Pouco texto. Nada de foto real dele lado a lado.
- Ilustração na Kairogen (nano-banana-2-1, 4:5, 2k, referência do personagem), cerca de 3 créditos por imagem, só com tema e custo aprovados.

## Legenda
Gancho de uma linha com emoji. Dois ou três blocos curtos contando a história. Emoji pontuando. 💬 pergunta pra comentar. 📌 pedido pra salvar quando fizer sentido. Até 5 hashtags. Não lista o que o vídeo já mostra.

Exemplo aprovado (Reel das 5 IAs):
> Se eu tivesse que tocar meus negócios com só 5 IAs, seriam essas. 👇
>
> Não é lista de ferramenta da moda. É o que eu abro todo santo dia pra construir produto, vender e não me afogar em tarefa. 🧠
>
> Cada uma tira um peso diferente das minhas costas: reunião, voz, vídeo, site e aquela que virou meu segundo cérebro.
>
> E a número 1 mudou o jeito que eu trabalho. Assiste até o final. 🎯
>
> 💬 Qual IA não pode faltar no teu dia? Me conta aqui nos comentários.
>
> 📌 Salva pra testar uma por semana.

## Stories
- Gravados: ele grava. A tarefa agendada "Lembrete de stories e Reels do @matheusmiranda.ia" (trig_019o4L1EkARPhztjfrvdv5wN) manda push às 09:51 e 19:51 com o tema, sem roteiro, e o Reels a gravar no dia.
- Só texto: o Claude faz e agenda sozinho, na paleta do cartoon (matheusmiranda/personagem/stories.py). Um "post novo" 10 minutos depois de cada carrossel.

## Reels
- Ele grava. Roteiro em blocos curtos, sem texto pra decorar. A edição fica num chat separado.
- O MP4 final ele arrasta no chat. Vai pro repositório em matheusmiranda/reels/ e de lá pro Trypost.

## Grade
- Carrossel às 12:30 e Reel às 19:40, todo dia.
- Story só texto de "post novo" às 12:40.
