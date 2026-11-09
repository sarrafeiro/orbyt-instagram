# Motor do Instagram do NuPrato (@nuprato.app)

Manual da tarefa semanal do NuPrato. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem. O Matheus não aprova nada antes: o post sai sozinho. Por isso a conferência visual (passo 6) é obrigatória.

Esta conta é separada das contas da Orbyt (@orbyt_studio e @orbytstudio_), que usam `motor/` na raiz do repositório. O NuPrato tem motor, marca, pastas e histórico próprios, tudo dentro de `nuprato/`. Nunca misture: não use nada de `motor/`, `posts/`, `barbearia/` nem `stories/` da raiz.

Estratégia e identidade: docs `claude/instagram-nuprato.md` e `claude/conceito-posts-nuprato.md` no projeto "Cozinha Infinita" do claude.ai. Se a sessão tiver acesso ao projeto, leia antes. Este manual tem tudo que é preciso para rodar mesmo sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Fala com quem cozinha em casa, no dia a dia.
- **Nunca usar travessão (U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem um verificador.
- Sem "não é X, é Y", sem emoji como marcador ou ícone na arte, sem frase de efeito vazia, sem "Concorda?".
- **Posicionamento:** perfil que resolve problema de quem cozinha em casa, não perfil de receita qualquer. Todo post parte de uma dor real (faltou ingrediente, receita de mãe "a olho", geladeira vazia, receita escrita pra outra cozinha, panela diferente) e termina no mecanismo: cê fala o prato, o NuPrato adapta pra sua cozinha e te guia até o fim.
- **Público de massa, ticket baixo.** Só ingrediente do dia a dia do brasileiro (arroz, feijão, ovo, frango, batata, carne moída, tomate, queijo). Nada gourmet (nada de cogumelo, trufa, ingrediente caro).
- **Fase atual (desde 03/11/2026): venda de conceito.** O app ainda não está pronto nem renomeado. Nada de print do app, nada de "baixa agora", nada de prometer função que o Matheus não confirmou. Funções que podem ser ditas: o usuário fala o prato; conta o que tem, quantas pessoas e o que tem na cozinha (fogão, forno, air fryer, panela de pressão); a IA adapta a receita (troca o que falta, ajusta quantidade e tempo) e explica o que mudou; guia passo a passo até o prato pronto.
- **Chamada:** "1ª receita guiada grátis" e "link na bio". Sem WhatsApp, sem preço, sem "sem cartão" (não confirmado). Nunca "comente PALAVRA que eu mando no direct", a não ser como pedido de comentário pra engajar (ex.: "comenta strogonoff").
- **Tom mineiro:** no máximo 2 marcas mineiras por legenda. "Nu" só na frase inteira "Nu, que prato!". "trem" no lugar de coisa ou ingrediente. "cê" liberado. "sô" no máximo 1 por peça. "uai" e "trem bão" só na voz (reel), nunca escrito.
- **Proibido:** roxo, qualquer referência ao Nubank, tweet como formato (lembra fintech), selo com borda, fundo ou contorno, selo na capa de post, número, estatística ou depoimento inventado, nome de pessoa real, repostar conteúdo de outra página.
- Substituição de ingrediente tem que ser verdadeira e segura. Na dúvida, não escreva. Bolo e pão: sempre avisar que pedem mais cuidado.
- Hashtag: 0 a 3, específicas (#receitafacil #comidacaseira #dicasdecozinha #cozinhafacil #substituicao #receitademae). Nunca mais de 3.

## 2. Preparar a sessão

1. Anexar o repositório com permissão de envio: ferramenta `add_repo` com owner `sarrafeiro`, repo `orbyt-instagram`, access `push`. Clonar com o comando que ela devolver (timeout grande).
2. Conferir: `python3 -c "import playwright, PIL"`. O Chromium já vem instalado (não rodar `playwright install`).
3. Trabalhar dentro de `nuprato/motor/`. Marca em `marca.json`, letras em `fontes/`, selo e avatar em `img/`.
4. Ler `nuprato/historico.md` inteiro: o que já saiu (não repetir título nem gancho), o tipo de capa dos últimos posts e os números das semanas anteriores.

## 3. A semana (horário de Brasília, UTC−3; o Trypost recebe em UTC)

**Regra do Matheus (04/11): nada sai depois das 19:00 de Brasília (22:00Z), nem post, nem story, nem reel.** Reel extra que o Matheus mandar sai às 14:31 (17:31Z).

**Calendário novo do feed (Matheus, 09/11; vale a partir da semana de 16/11):** 2 posts de feed por dia de segunda a sábado e 1 no domingo. Terça, quinta e sábado têm vídeo de receita que o Matheus faz: a tarefa deixa o horário das 14:31 (17:31Z) livre pra ele e produz só 1 carrossel nesses dias. Segunda, quarta e sexta: 2 carrosséis (12:40 = 15:40Z e 18:40 = 21:40Z). Domingo: 1 carrossel às 17:40 (20:40Z). Sábado o carrossel sai às 10:40 (13:40Z). Total: 10 carrosséis + 3 vagas de vídeo. A tabela abaixo continua valendo pros stories e pro horário das 18:40.

**Carrossel com foto (Matheus, 09/11):** parte dos carrosséis (uns metade) usa as cenas com gente de verdade geradas na Kairogen pro TikTok (`nuprato/tiktok/cenas/`). No motor: card `tema='foto', foto=<caminho>, fy=<foco vertical %>, baixo=True` (texto embaixo). Modelo: `posts/fotos_2026_11_09.py`. Mistura cards de foto com cards da marca (ficha, texto) e fecha no `FIM`. Esses posts vão com `meta: {is_ai_generated: true}` no Trypost. A regra antiga "sem comida gerada por IA no carrossel" não vale mais pra esse tipo. Não repetir cena já usada no Instagram (ver histórico); se faltar cena nova, avisar o Matheus em vez de gerar sozinho (gerar gasta crédito).

| Dia | Feed | Story 1 | Story 2 |
|---|---|---|---|
| Seg | 18:40 (21:40Z) carrossel, dor | 11:10 (14:10Z) | 17:10 (20:10Z) |
| Ter | 18:40 (21:40Z) imagem única ou carrossel, educação salvável | 11:10 (14:10Z) | 17:10 (20:10Z) |
| Qua | 18:40 (21:40Z) carrossel, mecanismo (como o NuPrato resolve) | 11:10 (14:10Z) | 17:10 (20:10Z) |
| Qui | 18:40 (21:40Z) carrossel, educação salvável (trocas, checklist) | 11:10 (14:10Z) | 17:10 (20:10Z) |
| Sex | 18:40 (21:40Z) imagem única ou carrossel, mito ou comunidade | 11:10 (14:10Z) | 17:10 (20:10Z) |
| Sáb | 10:40 (13:40Z) carrossel, oferta (1ª receita grátis) ou receita de fim de semana | 09:10 (12:10Z) | 18:10 (21:10Z) |
| Dom | sem feed | 10:10 (13:10Z) | 18:10 (21:10Z) |

Total: 6 feed + 14 stories = 20. Na semana: 4 carrosséis e 2 imagens únicas (igual à estreia). Reels: a tarefa semanal não produz reel. O Matheus faz os reels (capa na Runway, vídeo, card final) e manda; aí entram como post a mais, sem tirar nenhum do calendário. Agendar reel: `content_type: instagram_reel`, `media: [{url, meta: {cover_offset_ms: 300}}]` (a capa é o primeiro quadro), `meta: {share_to_feed: true, is_ai_generated: true, audio: {...}}`. Vídeo acima de 30 MB: comprimir antes (`ffmpeg -c:v libx264 -preset veryfast -crf 21 -c:a copy -movflags +faststart`).

**Música (desde 04/11 a conta está ligada ao Trypost pelo Facebook, plataforma instagram-facebook):** `search-instagram-audio-tool` com `account_id` da conta (sem `q` traz o que está em alta; buscas que funcionam: "samba", "funk"). A API só devolve a biblioteca licenciada do Instagram, não os hits do momento. Copie `id`, `title`, `artist` e `cover_url` em `meta.audio`, com `audio_volume: 45` e `video_volume: 100` (o vídeo tem som de cozinha). Música também pode ir em carrossel? Não: só em reel.

**Música dos reels (decisão do Matheus, 04/11):** a partir dos próximos vídeos, o Matheus já monta o reel com a música por cima na edição. Nesse caso NÃO pôr `meta.audio` no Trypost (senão entram duas músicas). Só usar `meta.audio` quando ele pedir. Reprovados: "Samba Quentinho" (Mike Block) e o funk "Audio em alta ⬆️" (djpatrickr). "Funky Friday" (Danny Peter Wolf, instrumental) foi liberado pelo Matheus nos dois reels da semana de 04/11. Limite da API: sem `q` ela devolve a lista "em alta" da biblioteca licenciada (genérica, sem os hits do Brasil); com `q` busca por nome. O Claude não escuta o áudio.

**Regra de repetição (Matheus, 04/11): a mesma música só volta depois de 5 reels.** Antes de escolher, olhe no histórico a música dos 5 últimos reels e não use nenhuma delas. Por isso a lista de aprovados serve de referência da linha, não de rodízio fixo: busque músicas novas no mesmo estilo. O Claude não escuta o áudio pela API: escolhe pelo título e pela linha aprovada e avisa o Matheus qual pôs, pra ele trocar se não curtir. Toda música usada vai pro histórico (título, artista, id). Busca útil: `type: original_sound` com `q: funk` traz sons originais (muita coisa estrangeira; prefira os com título em português ou instrumental).

Stories: o das 17:10 anuncia o post do dia (story com `capa=`); o das 11:10 é peça solta (frase de argumento, ficha com uma troca de ingrediente, pergunta pra responder, a oferta com o selo). Sábado: o das 18:10 anuncia o post do dia. Domingo: 2 peças soltas. Story que anuncia post: o título do story não repete o título da capa; use uma frase de dentro do post. Story com selo: no máximo 2 por semana.

## 4. Pauta

**Antes de tudo, veja se a semana já está pronta:** `list-posts-tool` com `channels: ["01a1a286-d9e6-72fb-9c27-2149379ec79d"]` e `status: scheduled`, olhando a semana alvo (segunda 00:00 a domingo 23:59, Brasília). Se já tiver 20, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Pilares: dor do dia a dia 30%, educação salvável 25%, mecanismo 20%, oferta 15%, comunidade 10%. Banco de ideias (marque no histórico o que usar e acrescente ideias novas no fim):

- Arroz empapou: o que fazer agora (salva o prato, sem drama).
- Feijão sem panela de pressão: passo a passo de verdade.
- O que fazer com o frango que sobrou (3 pratos).
- 4 trocas pro bolo que não dá errado (com o aviso de cuidado).
- Janta pra 1 pessoa sem sobrar a semana inteira (ajustar quantidade).
- Air fryer x forno: o que muda na receita.
- Checklist: o que ter em casa pra nunca ficar sem janta.
- Mito ou verdade: "lavar o arroz deixa soltinho".
- Mito ou verdade: "carne tem que descansar antes de cortar".
- Conversa: o parceiro pergunta "o que tem pra janta?" e a resposta é "nada" (geladeira).
- Conversa: a amiga manda "me passa a receita?" e a receita tem 4 páginas de história.
- Busca do Google: "o que fazer com ovo e batata".
- Número: "3 ingredientes" (uma janta com 3 trens só).
- Antes e depois: receita pra 6 pessoas x a mesma receita ajustada pra 2.
- Antes e depois: receita que pede forno x a mesma na air fryer.
- Pergunta pra comunidade: "qual prato cê sempre quis fazer e nunca teve coragem?".
- Salvei no Insta e nunca fiz (o NuPrato faz junto).
- Strogonoff sem creme de leite (já usado na estreia como busca; pode voltar como ficha em story).
- Tropeiro pra quem nunca fez (prato mineiro, passo a passo).
- Pão de queijo de liquidificador: o que dá pra trocar e o que não dá.

### Variar o formato (regra do Matheus)

- **Nunca dois posts seguidos com o mesmo tipo de capa.** Conferir no histórico a capa dos 3 últimos.
- Tipos de capa liberados: 1. texto gigante (fundo verde ou grafite, com `selo=` pílula); 2. ficha de receita de papel (`ficha`); 3. mito ou verdade (`carimbo`); 4. número gigante (`numero`); 5. conversa de WhatsApp (`conversa`); 6. busca do Google (`busca`); 7. antes e depois (`par` com duas `ficha`). Lista numerada (`lista`) só no meio do carrossel.
- Na semana: pelo menos 1 capa só texto; no máximo 2 capas de ficha.
- Grade em xadrez: alterne capa escura (verde ou grafite) e capa clara (creme ou papel) na ordem de publicação.
- Dentro do carrossel, pelo menos 2 fundos (creme, papel, verde, escuro).

### Carrossel é argumento

Cada card defende uma ideia em tipografia grande, com um visual herói (ficha, conversa, busca, número, lista, carimbo). Fale da vida de quem cozinha: a geladeira com 4 trens, a receita que pede o que cê não tem, o "um tiquinho" da mãe, o mercado às 20h. Referências do que funciona: `posts/estreia.py` (os 9 posts da estreia).

## 5. Produzir

Escreva um script novo em `nuprato/motor/posts/semana_AAAA_MM_DD.py` (data da segunda) no formato de `posts/estreia.py`: uma lista `POSTS = [(slug, cards), ...]`. Slug: `NN-tema` (ex.: `10-arroz-empapou`), numerando a partir do último número do histórico. A data entra só na pasta publicada.

- `python3 carrossel.py posts/semana_AAAA_MM_DD.py` (sai em `saida/<slug>/01.png...`). Pra um só: `SO=10-arroz-empapou python3 carrossel.py posts/...`.
- Carrossel: 5 a 8 cards (1080x1350). Capa com gancho de até 8 palavras, nunca começando pelo nome da marca. Um argumento por card, até 40 palavras. `<em>` vira marca-texto amarelo; use `&nbsp;` pra não deixar 1 palavra sozinha na linha marcada.
- Todo carrossel termina no card `FIM` (verde com o selo dourado e "1ª receita guiada grátis · link na bio"). Copie `FIM` de `posts/estreia.py`.
- Imagem única: uma lista com 1 card (veja `03-mito-risca`, `05-um-tiquinho`, `09-primeira-gratis`). Ela precisa se sustentar sozinha: gancho + apoio curto + anotação à mão.
- `ficha` e `lista` em fundo escuro ou verde ficam bons; `conversa` e `busca` também. Não use `numero` com `tam` maior que 440.

**Stories** (1080x1920): base `posts/exemplo_stories.py` (4 tipos: frase, capa do post, ficha, oferta com selo). Script em `posts/stories_AAAA_MM_DD.py`, saída em `saida/stories-AAAA-MM-DD/` (data da segunda). Para o story que anuncia post, `capa=` aponta para o `01.png` em `saida/<slug>/`. Pílula de baixo: "post novo no perfil", "link na bio" ou "mais trocas no perfil".

**Legendas:** arquivo `posts/legendas_AAAA_MM_DD.md` no formato de `posts/legendas_estreia.md` (legenda + `ALT:` por slug). 1ª linha = gancho com a palavra que a pessoa pesquisa; 3 a 6 linhas curtas; uma pergunta quando fizer sentido; fecha com "link na bio"; 0 a 3 hashtags. Texto alternativo em todo post de feed. Story não leva legenda.

## 6. Conferir antes de publicar (obrigatório)

1. `python3 folha.py saida/<slug> ...` e abrir cada folha em `saida/_folhas/` com a ferramenta Read. Procurar: texto cortado, palavra sozinha na linha marcada, card vazio, ficha pequena demais, texto em cima de outro. O `carrossel.py` avisa "AVISO ... passa Npx" se algo vazar (até 8 px no card final é normal, é a etiqueta girada).
2. Stories: montar uma tira (veja como foi feita a `stories-exemplo.jpg`) e abrir com Read.
3. `python3 checar.py posts/<arquivos novos>`: tem que sair vazio.
4. Reler cada substituição de ingrediente: verdadeira, segura, com ingrediente comum.

## 7. Publicar e agendar

1. Para cada post: `python3 publicar.py <slug> posts/AAAA-MM-DD-<slug>` (data = dia em que sai). Stories: `python3 publicar.py stories-AAAA-MM-DD stories/AAAA-MM-DD`.
2. Na raiz do repositório: `git add -A nuprato && git commit -m "NuPrato, semana AAAA-MM-DD: 6 posts e 14 stories" && git push`. Antes do push, `git fetch origin main` e `git rebase origin/main` (outras contas usam o mesmo repositório).
3. Pegue as URLs com o hash do commit: `python3 publicar.py <slug> posts/AAAA-MM-DD-<slug> --hash` (não regrava nada, só imprime). Use sempre essas, não as da branch.
4. Trypost, `create-post-tool`, conta **`01a1a286-d9e6-72fb-9c27-2149379ec79d`** (@nuprato.app), `status: scheduled`, `scheduled_at` em UTC (tabela da seção 3), horário exato (não usar fila).
   - Post de feed: `content_type: instagram_feed`, `media: [{url, alt}, {url}, ...]` (alt só no primeiro já basta; máximo 10), `content` = legenda.
   - Story: `content_type: instagram_story`, `content: ""`, uma imagem por post.
   - Se o Trypost devolver erro de mídia, esperar 2 minutos e tentar de novo uma vez.
5. No fim, `list-posts-tool` com o canal e `status: scheduled`: conferir 20 agendados na semana, sem horário repetido.

## 8. Medir a semana que passou

1. `list-posts-tool` (canal do NuPrato, `status: published`, olhe só os de `origin: trypost` dos últimos 7 dias) e `get-post-metrics-tool` de cada um; `get-channel-insights-tool` da conta.
2. Anotar no `historico.md`: alcance, curtidas, comentários, salvamentos, compartilhamentos e visitas ao perfil por post (o que a ferramenta devolver; se não devolver, "sem dado", nunca estimar).
3. Regra do Matheus: metade dos temas novos nas linhas que mais engajaram (pilar, formato, tipo de capa, tipo de gancho), com ângulo novo; o resto variado. Sinal fraco (2 curtidas e o resto zerado) não vira a semana toda. A partir de 4 semanas de dado, dobrar os 2 formatos com mais (salvamentos + compartilhamentos) por alcance e cortar o pior. Anotar a decisão.

## 9. Avisar o Matheus

Mensagem curta (ferramenta SendUserMessage), em português, sem travessão, com:
- os 6 temas da semana e o dia de cada um;
- os números da semana anterior em 3 linhas (melhor post, pior post, total de alcance);
- qualquer coisa que travou e o que ele precisa fazer (só se precisar).
Se algo travar antes de agendar (sem acesso ao Trypost ou ao GitHub), não inventar: avisar o que travou e parar.
