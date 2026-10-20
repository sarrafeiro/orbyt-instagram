# Motor do Instagram da Orbyt Studio (@orbyt_studio)

Manual da tarefa semanal. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem. O Matheus não aprova nada antes: o post sai sozinho. Por isso a conferência visual (passo 6) é obrigatória.

Estratégia completa: arquivo `brain/16-instagram-orbyt.md` no projeto "Orbyt Studio" do claude.ai (se a sessão tiver acesso ao projeto, leia antes). Este manual tem tudo que é preciso para rodar mesmo sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Chama o público pelo que ele é ("Advogado,", "Doutor," só se fizer sentido).
- **Nunca usar travessão (caractere U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem um verificador.
- Sem "não é X, é Y", sem emoji como marcador, sem frase de efeito vazia ("transforme sua presença digital"), sem "Concorda?".
- **Só advocacia.** Desde 20/10/2026 o Instagram é só de site para advogado (os dois nichos no mesmo feed confundiam). Nunca citar barbearia nem dentista, nem em legenda, card, story ou hashtag. Os posts de barbearia foram apagados do perfil.
- Chamada sempre para o **WhatsApp pelo link do perfil**. Nunca "comente PALAVRA que eu mando no direct".
- Sem rosto, sem pessoa gerada por IA, sem nome de cliente real. Nome de exemplo: **Andrade & Ferraz Advocacia** (fictício).
- Advocacia: dizer "seguindo o Provimento 205/2021". Nunca "aprovado pela OAB", nunca prometer resultado de processo, nunca falar de honorário do advogado nem de consulta grátis do escritório. O preço que aparece é o da Orbyt, isso pode.
- Hashtag: 0 a 3, específicas (#siteparaadvogados #advocacia #advocaciabh #marketingjuridico #provimento205). Nunca mais de 3.
- Reel sem música (o Trypost não põe música nessa conta). Reel tem que ser entendido sem som.
- Só print dos nossos próprios modelos. Nunca repostar conteúdo de outra página.

**Oferta vigente (não inventar nada além disto):**
- Landing page R$ 399, preço fechado, em até 2 dias úteis.
- Site com modelo do segmento R$ 797, preço fechado, em até 2 dias úteis.
- Site 100% personalizado a partir de R$ 1.497, em até 5 dias úteis.
- Loja virtual a partir de R$ 2.997.
- R$ 0 pra começar. O cliente vê o site pronto num link da Orbyt, pede até 2 ajustes e **só paga depois de aprovar**, uma vez, Pix ou cartão parcelado. Sem entrada, sem mensalidade.
- A publicação é feita em chamada, numa conta do próprio cliente: o site fica no nome dele.
- Advocacia: guia por assunto (mini diagnóstico em 3 cliques) que leva o cliente ao WhatsApp do escritório sabendo o que levar.
- WhatsApp da Orbyt: (31) 99073-0997. Base em BH, atende o Brasil todo.

## 2. Preparar a sessão

1. Anexar o repositório com permissão de envio: ferramenta `add_repo` com owner `sarrafeiro`, repo `orbyt-instagram`, access `push`. Clonar com o comando que ela devolver.
2. Conferir: `which ffmpeg`, `python3 -c "import playwright, PIL"`. O Chromium já vem instalado (não rodar `playwright install`).
3. Trabalhar dentro de `motor/`. As letras estão em `motor/www/fonts`, os prints dos modelos em `motor/prints`, os modelos de site em `motor/www/modelos` (advocacia/1 e advocacia/2; o barb-anon não é mais usado).
4. Ler `motor/historico.md` inteiro: o que já saiu (não repetir título nem gancho) e os números das semanas anteriores.

## 3. A semana (horário de Brasília, UTC−3; o Trypost recebe em UTC)

| Dia | Feed | Story 1 | Story 2 |
|---|---|---|---|
| Seg | 19:40 (22:40Z) carrossel advocacia, dor | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Ter | 19:40 (22:40Z) **reel** advocacia, vitrine (modelo rodando) | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Qua | 19:40 (22:40Z) carrossel advocacia, oferta e mecanismo | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Qui | 19:40 (22:40Z) carrossel advocacia, educação salvável | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Sex | 19:40 (22:40Z) carrossel advocacia, objeção, mito ou antes e depois | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Sáb | 10:40 (13:40Z) **reel** advocacia, vitrine ou bastidor | 09:10 (12:10Z) | 20:10 (23:10Z) |
| Dom | sem feed | 10:10 (13:10Z) | 19:10 (22:10Z) |

Total: 6 feed + 14 stories = 20.

Stories de segunda a sábado: o que sai **depois** do feed do dia é o "post novo" (capa do post do dia); o outro é peça solta (frase de pagamento, preço, modelo no celular, dúvida frequente, bastidor). Como o feed de seg a sex sai 19:40 e os stories saem antes, nesses dias o story das 13:10 anuncia o post **da véspera** e o das 08:10 é peça solta. Sábado: o story das 20:10 anuncia o reel do dia. Domingo: 2 peças soltas.

**Teste de horário:** semana de 02/11/2026 o feed de seg a sex vai às 13:10 (16:10Z) e o story das 13:10 passa para 19:40 (22:40Z). Na semana seguinte, comparar o alcance das primeiras 24 h das duas semanas (passo 8) e ficar com o melhor horário. Anotar a decisão no histórico.

## 4. Pauta

**Antes de tudo, veja se a semana já está pronta:** `list-posts-tool` com os agendados da semana alvo (segunda 00:00 a domingo 23:59, horário de Brasília). Se já tiver 20 agendados, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Escolha 6 temas que não estão no histórico. Pilares: vitrine/prova 30%, dor do nicho 25%, oferta e mecanismo 20%, educação salvável 15%, bastidor 10%. Banco de ideias (risque no histórico o que usar, e acrescente ideias novas no fim desta lista quando tiver):

Advocacia
- Seu site abre direito no celular? É ali que o cliente pesquisa você.
- O que o cliente quer ver no site do escritório antes de ligar (lista de 5).
- 4 coisas que o site faz pelo escritório e o Instagram não faz (comparação).
- Perfil no Google sem site: o que o cliente pensa quando não acha mais nada.
- Pode publicar artigo no site do escritório? Pode, e ajuda a aparecer no Google (conteúdo informativo, Provimento 205/2021).
- Como apresentar áreas de atuação sem ferir o Código de Ética.
- Equipe com número da OAB no site: por que passa confiança.
- 5 erros no site de escritório que espantam cliente.
- Reel: o guia por assunto em outro caminho (escolher outra área no `#chips1`).
- Reel: celular e computador lado a lado (modelo advocacia 2).
- Reel bastidor: do nome do escritório no WhatsApp ao site no link de aprovação.

Oferta e mecanismo (sempre falando com advogado)
- O que acontece depois que você aprova o site.
- O site fica no seu nome: o que isso quer dizer na prática.
- Landing page ou site pro escritório (R$ 399 x R$ 797).
- Por que a gente monta antes de você pagar.
- Do pedido ao site no ar em 5 passos (variação do post fixado, com outro visual).

Ideias novas (acrescentadas em 20/10)
- Reel advocacia: guia por assunto no caminho Família (divórcio, guarda, pensão).
- Carrossel advocacia: dúvidas frequentes do escritório no site (print `adv1-cel-duvidas`).

### Variar o formato (regra do Matheus, 20/10)

O feed não pode parecer o mesmo post repetido com outra copy. Regras:
- **Nunca dois posts seguidos com o mesmo tipo de capa.** Conferir no histórico qual foi a capa dos 3 últimos.
- Tipos de capa (rodar entre eles): 1. só texto gigante em fundo laranja ou escuro (`tipo='texto'`); 2. print do modelo no celular; 3. site no computador (`navegador`); 4. conversa de WhatsApp (`conversa`); 5. estilo tweet (`tweet`); 6. antes e depois com site antigo (`par` + `site_antigo`); 7. checklist em papel (`tema='papel'` + `checklist`); 8. carimbo MITO/VERDADE (`carimbo`); 9. número gigante (`numero`); 10. busca do Google (`busca`).
- Dentro do carrossel, alternar o fundo dos cards (`tema='claro'|'escuro'|'laranja'|'papel'`). Pelo menos 2 fundos diferentes por carrossel.
- Na semana: no máximo 2 carrosséis com print de celular na capa; pelo menos 1 capa só texto.
- Formatos de pauta pra variar também: lista salvável, checklist, mito ou verdade, objeção e resposta, antes e depois, passo a passo, comparação, pergunta e resposta.
- Ideia nova de formato que funcionar: anotar no histórico.

## 5. Produzir

Copie um arquivo de `motor/posts/` como base, troque o texto, rode.

**Carrossel** (1080×1350, 5 a 9 cards): bases com formatos diferentes em `posts/n1_como_funciona.py` (capa só texto laranja, número gigante), `n2_duvidas_adv.py` (conversa), `n3_precos_adv.py` (texto escuro, ficha, checklist), `n4_antes_depois.py` (site antigo x novo), `n5_desculpas.py` (tweet), `n6_checklist.py` (papel), `n7_mitos.py` (carimbo), `b06_adv_google.py` (busca), `p05_adv_oab.py` (lista pode/não pode). Rodar `python3 carrossel.py posts/<arquivo>.py` (sai em `saida/<SLUG>/01.png...`).
- Card `capa`: gancho de até 8 palavras falando com o advogado. Nunca começar com "Orbyt". Card `texto`: só tipografia, título gigante centralizado (use `tema`, `selo`, `rodape`).
- Cards `passo`: um argumento por card, até 40 palavras.
- Card `final` (escuro): preço, 4 checks e a chamada pro WhatsApp com "Link no perfil".
- `<em>` deixa a palavra laranja. `t` é o tamanho do título (padrão bom: 84 a 104), `s` o do texto.
- Visuais prontos: `cel('arquivo.png', chip=None, ch=altura)`, `navegador('arquivo.png', 'url', w=None)`, `conversa(nome, [(quem, texto, hora)])`, `pagamento()`, `busca(q, resultados)`, `lista(itens, tipo='pode'|'nao'|'num')`, `ficha(linhas, destaque, grande)`, `applink()`.
- `centro=True` centraliza; `ponto=False` tira o ponto da órbita quando ele bater no texto; `gigante=True` deixa o card com título grande centralizado.
- Opções novas por card: `tema='claro'|'escuro'|'laranja'|'papel'`, `selo='texto'` (etiqueta acima do título), `rodape='texto'`, `carimbo=('MITO','mito')` ou `('VERDADE','verdade')`.
- Visuais novos: `tweet(texto, tam=None)`, `numero(valor, rotulo, tam=None)`, `site_antigo()`, `checklist(itens, marcados=0)`, `par(antes, depois, rot_a, rot_b)`.
- Prints bons (pasta `prints/`): `adv2-cel-capa`, `adv1-cel-guia1/2/3`, `adv2-cel-guia1/3`, `adv2-cel-guia-inss`, `adv1-cel-areas`, `adv1-cel-equipe`, `adv1-cel-conteudo`, `adv1-cel-duvidas`, `adv2-desk-capa`, `adv1-desk-areas` e as outras versões `-desk-`. **Não usar** `adv1-cel-capa` (primeira tela curta), `adv2-cel-areas` e `adv2-cel-equipe` (etiqueta em cima do título), `*-contato` (saem quebrados) e nenhum `barb-*`.
- Novo print: `python3 capturar.py adv1 adv2`.

**Reel** (1080×1920, 15 a 25 s, 30 fps, sem som): base `posts/r02_adv.py` (guia por assunto), `posts/r05_adv_inss.py` (guia no modelo 2) e `posts/b07_reel_adv_tour.py` (tour: áreas, equipe, método). Copie, mude `OUT`, os títulos dos fundos (`html_fundo`), a sequência de rolagem/toques e o cartão final (`html_fim`). Primeiro fundo: gancho grande nos 2 primeiros segundos. Fim: preço + "só paga depois de aprovar" + "Link no perfil". Leva cerca de 1,5 min para gravar. Sai `saida/<pasta>/<nome>.mp4` e uma `-capa.jpg`.

**Stories** (1080×1920): base `posts/stories_estreia.py`. Três tipos: capa de post (`capa=` caminho do `01.png` do post), modelo no celular (`cel=` print), frase escura (`escuro=True`, com `sub` e opcional `preco`). Texto fica longe do topo e da base. Rodar e salvar em `saida/stories-AAAA-MM-DD/` (data da segunda-feira).

**Legenda** (vai no Trypost, não na imagem): 1ª linha = gancho com a palavra de busca ("site para advogados", "site para escritório de advocacia"); 3 a 6 linhas curtas; uma pergunta quando fizer sentido; chamada pro WhatsApp pelo link do perfil; 0 a 3 hashtags. Texto alternativo em toda imagem com a palavra de busca. Story não leva legenda (o Trypost manda sem texto); o texto vai dentro da imagem.

## 6. Conferir antes de publicar (obrigatório)

1. Abrir **cada** PNG com a ferramenta Read e olhar: texto cortado, texto em cima do celular ou do ponto laranja, card vazio, print errado, palavra quebrada no meio. Corrigir e renderizar de novo.
2. Ver 3 quadros de cada reel (`ffmpeg -ss 1 -i reel.mp4 -frames:v 1 q1.jpg`, idem no meio e no fim) e abrir com Read.
3. Verificador de travessão (tem que sair vazio):
   `python3 checar.py posts/<arquivos novos>.py` (inclua o arquivo onde ficaram as legendas).
4. Conferir preço e prazo contra a seção 1.

## 7. Publicar e agendar

1. `python3 publicar.py <pasta em saida> posts/AAAA-MM-DD-<slug>` para cada post (data = dia em que sai), e `python3 publicar.py stories-AAAA-MM-DD stories/AAAA-MM-DD` para os stories. Ele converte PNG em JPG e imprime as URLs públicas.
2. `git add -A && git commit` (mensagem: "Semana AAAA-MM-DD: 6 posts e 14 stories") e `git push`. Esperar 1 minuto antes de agendar (o link raw demora um pouco a ficar disponível). O ambiente não consegue abrir raw.githubusercontent.com; quem baixa é o Trypost.
3. Trypost, ferramenta `create-post-tool`, conta `01a159a1-1a44-7093-aa3b-56218442a19a`, `status: scheduled`, `scheduled_at` em UTC (tabela da seção 3):
   - Carrossel: `content_type: instagram_feed`, `media: [{url, alt}, ...]` (máximo 10), `content` = legenda.
   - Reel: `content_type: instagram_reel`, `meta: {"share_to_feed": true}`, `media: [{url, alt, meta: {"cover_offset_ms": 1200}}]`.
   - Story: `content_type: instagram_story`, `content: ""`, uma imagem por post.
   - Rótulos (`label_ids`): Advocacia `01a159da-242b-7236-8e6d-33b1b1a63037` (todo post de feed) · Story `01a159da-4349-712f-9f1c-dd48f783b1e2`. Os rótulos Barbearia e Geral não são mais usados.
   - Agendar cada um no horário exato. Não usar a fila automática (ela não separa feed de story).
   - Se o Trypost devolver erro de mídia, esperar 2 minutos e tentar de novo uma vez.
4. No fim, `list-posts-tool` da semana: tem que ter 20 agendados, sem horário repetido.

## 8. Medir a semana que passou

1. `list-posts-tool` (publicados nos últimos 7 dias) e `get-post-metrics-tool` de cada um; `get-channel-insights-tool` da conta.
2. Anotar no `historico.md`, na semana certa: alcance, salvamentos, compartilhamentos, comentários e visitas ao perfil por post (o que a ferramenta devolver; se não devolver, escrever "sem dado", nunca estimar).
3. Regra de decisão: a partir de 4 semanas de dado, dobrar os 2 formatos ou pilares com mais (salvamentos + compartilhamentos) por alcance e cortar o pior. Anotar a decisão.
4. Sinal ruim: depois de 3 semanas, alcance quase só de seguidores → trocar 1 carrossel por reel.

## 9. Avisar o Matheus

Mensagem curta (ferramenta SendUserMessage), em português, sem travessão, com:
- os 6 temas da semana e o dia de cada um;
- os números da semana anterior em 3 linhas (melhor post, pior post, total de alcance);
- qualquer coisa que travou e o que ele precisa fazer (só se precisar).
Se algo travar antes de agendar (sem acesso ao Trypost ou ao GitHub), não inventar: avisar o que travou e parar.
