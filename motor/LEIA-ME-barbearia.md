# Motor do Instagram de barbearias da Orbyt Studio (@orbytstudio_)

Manual da tarefa semanal da conta de BARBEARIAS. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem. O Matheus não aprova nada antes: o post sai sozinho. Por isso a conferência visual (passo 6) é obrigatória.

Esta conta é separada do @orbyt_studio (advocacia), que tem o manual `LEIA-ME.md`. Os dois usam o mesmo motor (`carrossel.py`, `reel.py`, `story.py`, `publicar.py`, `checar.py`), mas o conteúdo, a conta no Trypost, as pastas e o histórico são outros. Nunca misture.

Estratégia geral do Instagram: arquivo `brain/16-instagram-orbyt.md` no projeto "Orbyt Studio" do claude.ai; a conta de barbearia está no `brain/18-instagram-barbearia.md`. Se a sessão tiver acesso ao projeto, leia antes. Este manual tem tudo que é preciso para rodar mesmo sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Chama o público de "Barbeiro," quando fizer sentido.
- **Nunca usar travessão (U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem um verificador.
- Sem "não é X, é Y", sem emoji como marcador, sem frase de efeito vazia, sem "Concorda?".
- **Só barbearia.** Nunca citar advogado, escritório, OAB nem dentista, em nada (card, legenda, story, hashtag).
- Chamada sempre para o **WhatsApp pelo link do perfil**. Nunca "comente PALAVRA que eu mando no direct".
- Sem rosto de pessoa gerada por IA, sem nome de cliente real. Barbearia de exemplo: **Sua Barbearia** (fictícia, modelo `www/modelos/barb-anon`). Nunca mostrar Rituno, Rodrigo, Breno nem outro cliente real.
- Hashtag: 0 a 3, específicas (#sitebarbearia #barbearia #barbeariabh #barbeariasp #clubedeassinatura). Nunca mais de 3.
- Reel sem música (o Trypost não põe música nessa conta). Reel tem que ser entendido sem som.
- Só print dos nossos próprios modelos. Nunca repostar conteúdo de outra página.

**Oferta vigente para barbearia (decisão do Matheus em 22/10/2026; não inventar nada além disto):**
- **Site com modelo de barbearia: R$ 399**, preço fechado, em até 2 dias úteis.
- **Landing page: R$ 199**, preço fechado, em até 2 dias úteis.
- Site 100% personalizado a partir de R$ 1.497, em até 5 dias úteis.
- **Argumento de preço (regra do Matheus): "custa menos que 5 cortes".** R$ 40 é corte de entrada; em barbearia boa o corte passa de R$ 80 (o Matheus paga R$ 120). Conta pronta: 5 cortes de R$ 80 dão R$ 400. Use isso em carrossel, story, reel e legenda. Nunca "9 cortes" nem "18 cortes".
- R$ 0 pra começar. O cliente vê o site pronto num link da Orbyt, pede até 2 ajustes e **só paga depois de aprovar**, uma vez, Pix ou cartão parcelado. Sem entrada, sem mensalidade.
- A publicação é feita em chamada, numa conta do próprio cliente: o site fica no nome dele.
- O site de barbearia tem: botão Agendar na primeira tela (leva pro app que ele já usa ou direto pro WhatsApp), tabela de serviços com preço, clube de assinatura com a economia, antes e depois dos cortes (o cliente arrasta), equipe com agendar direto com o barbeiro, espaço, avaliações, produtos, dúvidas e como chegar.
- Sem foto boa? Começa com foto de exemplo e troca quando o dono mandar.
- Objeção principal: "já tenho o link do app". Resposta: o app agenda, o site vende.
- LP de barbearia: orbytstudio.com.br/barbearias. O site geral da Orbyt mostra outro preço (R$ 797): o Matheus sabe e aceitou. Nos posts desta conta vale sempre R$ 399 e R$ 199.
- WhatsApp da Orbyt: (31) 99073-0997. Base em BH, atende o Brasil todo.

**Carro-chefe do conteúdo: o antes e depois que o cliente arrasta com o dedo.** É o que o mini diagnóstico é para a conta de advocacia: o diferencial que mais vende. Regra: **pelo menos 2 dos 6 posts da semana mostram o arrastar**, de preferência nos 2 reels (reel arrastando os 3 cortes `#ba1`, `#ba2`, `#ba3`); num carrossel, ele entra como o card de prova (print `barb-cel-antes-depois`) no meio de cards de argumento, nunca como carrossel inteiro de celular. Pelo menos 1 story por semana também. O reel de base é `posts-barb/bb07_reel_antes_depois.py`. Ganchos que funcionam: "o seu corte vende sozinho", "o cliente arrasta e vê a diferença", "o seu trabalho convence melhor que qualquer texto".

## 2. Preparar a sessão

1. Anexar o repositório com permissão de envio: ferramenta `add_repo` com owner `sarrafeiro`, repo `orbyt-instagram`, access `push`. Clonar com o comando que ela devolver.
2. Conferir: `which ffmpeg`, `python3 -c "import playwright, PIL"`. O Chromium já vem instalado (não rodar `playwright install`).
3. Trabalhar dentro de `motor/`. Scripts desta conta em `motor/posts-barb/`. Letras em `motor/www/fonts`, prints em `motor/prints` (só os `barb-*`), modelo em `motor/www/modelos/barb-anon`.
4. Ler `motor/historico-barbearia.md` inteiro: o que já saiu (não repetir título nem gancho) e os números das semanas anteriores.

## 3. A semana (horário de Brasília, UTC−3; o Trypost recebe em UTC)

| Dia | Feed | Story 1 | Story 2 |
|---|---|---|---|
| Seg | 19:40 (22:40Z) carrossel, dor | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Ter | 19:40 (22:40Z) **reel**, vitrine (modelo rodando) | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Qua | 19:40 (22:40Z) carrossel, oferta e mecanismo | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Qui | 19:40 (22:40Z) carrossel, educação salvável | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Sex | 19:40 (22:40Z) carrossel, objeção, mito ou antes e depois | 08:10 (11:10Z) | 13:10 (16:10Z) |
| Sáb | 10:40 (13:40Z) **reel**, vitrine ou bastidor | 09:10 (12:10Z) | 20:10 (23:10Z) |
| Dom | sem feed | 10:10 (13:10Z) | 19:10 (22:10Z) |

Total: 6 feed + 14 stories = 20. Stories: o das 13:10 anuncia o post da véspera; o das 08:10 é peça solta (frase de argumento, frase de pagamento, a conta do "menos que 5 cortes", dúvida, bastidor). Sábado: o story das 20:10 anuncia o reel do dia. Domingo: 2 peças soltas. Story com celular: no máximo 2 por semana (um deles o antes e depois). Story que anuncia post: o título do story não repete o título da capa; use uma frase de dentro do post.

## 4. Pauta

**Antes de tudo, veja se a semana já está pronta:** `list-posts-tool` com `channels: ["01a164ce-6789-728e-a634-c998fa7d61fa"]` e os agendados da semana alvo (segunda 00:00 a domingo 23:59, Brasília). Se já tiver 20, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Escolha 6 temas que não estão no histórico. Pilares: vitrine/prova 30%, dor 25%, oferta e mecanismo 20%, educação salvável 15%, bastidor 10%. Banco de ideias (risque no histórico o que usar e acrescente ideias novas no fim):

- (CARRO-CHEFE) Carrossel antes e depois: "o seu corte vende sozinho", um corte por card (degradê, barba, cacheado) e o botão Agendar no fim.
- (CARRO-CHEFE) Reel: o cliente arrasta, vê o corte e toca em Agendar (mostrar a mensagem chegando no WhatsApp).
- (CARRO-CHEFE) Story: print do antes e depois com "arrasta pra comparar".
- (USADA em 27/10) Reel bb06 antes de ir (equipe, espaço, avaliações, como chegar), agora em `barbearia/posts/2026-10-27-bb06-reel-antes-de-ir`. (USADA em 31/10) Reel carro-chefe arrasta e toca em Agendar (`bb11_reel_agendar.py`). (USADA em 29/10) Primeiros segundos do cliente novo (`bb12_primeiros_segundos.py`).
- Menos que 5 cortes: carrossel ou story só com a conta (5 cortes de R$ 80 = R$ 400; o site custa R$ 399, uma vez só).
- "Barbearia perto de mim": o que aparece no Google quando a sua barbearia não tem site (`busca`).
- Avaliações no site: nota de quem já sentou na cadeira (print `#avaliacoes`).
- Agendar direto com o barbeiro: cada um com o seu botão (seção `#equipe`).
- Produtos à venda no site (seção `#produtos`): pomada, óleo, shampoo.
- O site da sua barbearia tem estes 7 itens? (checklist em papel).
- (USADA em 30/10, `bb08_mitos.py`) 3 mitos sobre site de barbearia. Mitos ainda livres pra outro post: "o link do app já resolve", "precisa de mensalidade", "site não traz cliente".
- (USADA em 26/10) Enquanto você corta, quem responde o cliente? (`bb10_enquanto_corta.py`). (USADA em 28/10) Faz a conta: quanto vale um cliente que volta (`bb09_faz_a_conta.py`).
- Ideias de argumento (sem celular): "Cliente perguntou o preço e sumiu" (conversa); "O que o cliente novo vê nos primeiros 5 segundos" (lista); "Barbearia de 1 cadeira precisa de site?" (pergunta e resposta); "Indicação sem site: o amigo manda o seu @ e o cliente não acha o preço" (tweet); "Quanto custa uma cadeira vazia numa terça à tarde" (número, conta com o preço do barbeiro); "Instagram, app de agenda e site: o que cada um faz" (ficha de comparação, sem print); "Mito ou verdade: site não traz cliente" (carimbo); "O que muda quando o cliente acha o seu preço sozinho" (antes e depois em texto, `par` com duas `lista`).
- Número gigante: "38 serviços. Num toque só." (tabela).
- Landing page de R$ 199 pra uma campanha: dia dos pais, combo corte + barba, promoção do mês.
- Cliente pergunta preço no direct toda hora? Manda o link do site (conversa de WhatsApp).
- Clube de assinatura: o cliente vê quanto economiza e assina pelo site.
- Reel bastidor: do nome da barbearia no WhatsApp ao site no link de aprovação.
- Reel: produtos e dúvidas (estacionamento, criança, pagamento).
- O site fica no seu nome: o que isso quer dizer na prática.

### Variar o formato (regra do Matheus)

- **Nunca dois posts seguidos com o mesmo tipo de capa.** Conferir no histórico a capa dos 3 últimos.
- Tipos de capa: 1. só texto gigante em fundo laranja ou escuro (`tipo='texto'`); 2. print no celular; 3. site no computador (`navegador`); 4. conversa de WhatsApp (`conversa`); 5. tweet (`tweet`); 6. antes e depois (`par`); 7. checklist em papel (`tema='papel'` + `checklist`); 8. carimbo MITO/VERDADE (`carimbo`); 9. número gigante (`numero`); 10. busca do Google (`busca`); 11. lista numerada (`lista`); 12. link do app x site (`applink`).
- Dentro do carrossel, alternar o fundo dos cards (pelo menos 2 fundos). **Atenção:** `ficha` e `lista` ficam ilegíveis com `tema='escuro'` (caixa branca com texto branco). Use `claro` ou `papel` nesses cards.
- Na semana: pelo menos 1 capa só texto.

### Argumento antes de print (regra do Matheus, 22/10)

Na estreia, 6 dos 9 carrosséis tinham o mesmo esquema: título em cima e celular com print embaixo, card após card. O Matheus achou fraco e pediu o jeito da conta de advocacia, que deu certo: carrossel que **argumenta**, quase sem celular. Regras:
- **Carrossel é argumento.** Cada card defende uma ideia (um mito, uma objeção, uma conta, uma cena do dia a dia do barbeiro, uma pergunta do cliente), em tipografia grande, com carimbo, tweet, conversa, número, checklist, lista ou ficha. O print do site é prova, não é o conteúdo.
- **No máximo 1 carrossel por semana com print de celular nos cards**, e mesmo nele no máximo 2 cards com celular. Os outros carrosséis da semana não têm nenhum print.
- Celular e tela ficam pros **reels** (vitrine e carro-chefe do antes e depois) e no máximo 2 stories por semana.
- Fale da vida do barbeiro: a máquina na mão e o celular vibrando, a cadeira vazia na terça, o cliente que pergunta o preço e some, a indicação que não acha o preço, o clube que faz voltar todo mês. Isso convence mais que mostrar a tela.
- Referências do que funciona: aqui, `bb10_enquanto_corta.py`, `bb09_faz_a_conta.py`, `bb08_mitos.py`, `bb05_desculpas.py`, `bb02_precos.py`; na advocacia, `posts/n7_mitos.py`, `posts/n5_desculpas.py`, `posts/n3_precos_adv.py`, `posts/n6_checklist.py`.
- Conta com número (ex.: cliente que volta) sempre com as premissas no card ("corte de R$ 80, a cada 3 semanas") e o convite "troca pelo seu preço". Nunca estatística inventada ("70% dos clientes...").

## 5. Produzir

Copie um arquivo de `motor/posts-barb/` como base, troque o texto e o `SLUG`, rode `python3 carrossel.py posts-barb/<arquivo>.py` (sai em `saida/<SLUG>/01.png...`).

Bases por formato (comece por estas): `bb10_enquanto_corta.py` (conversa com cliente, `conversa(..., pessoa=True)`, texto gigante, checklist), `bb09_faz_a_conta.py` (número gigante com conta), `bb08_mitos.py` (carimbo MITO/VERDADE), `bb05_desculpas.py` (tweet), `bb02_precos.py` (texto escuro, ficha, checklist, número), `bb03_tres_jeitos.py` (lista, ficha), `bb04_duvidas.py` (conversa), `bb07_reel_antes_depois.py` (reel carro-chefe).
Bases com muito celular, use só no carrossel da semana que pode ter print (e corte pra no máximo 2 cards com celular): `bb01_como_funciona.py`, `b02_fixado_barb.py`, `b05_barb_cliente_novo.py` (busca), `p06_barb_link.py` (applink x site), `p09_barb_5coisas.py`, `p13_barb_preco.py`.

- Todo carrossel termina com o card `final` (escuro) com `preco='R$ 399'`, os 4 checks e a chamada. Copie `CHECKS` e `CTA_BARB` de `bb01_como_funciona.py`.
- **Tweet:** ponha `_os.environ['ORBYT_HANDLE'] = 'orbytstudio_'` no topo do script (antes de importar o carrossel), senão sai @orbyt_studio.
- Card `capa`: gancho de até 8 palavras. Nunca começar com "Orbyt". Um argumento por card, até 40 palavras. `<em>` deixa a palavra laranja.
- No `numero()`, use `tam=195` no máximo (maior que isso o "$" encosta no texto de baixo).
- Prints bons: `barb-cel-capa`, `barb-cel-clube`, `barb-cel-servicos`, `barb-cel-tabela`, `barb-cel-antes-depois`, `barb-cel-duvidas`, `barb-cel-espaco2`, `barb-desk-capa` e as outras `barb-desk-*`. **Não usar** `barb-cel-espaco` nem `barb-cel-local` (topo em branco). Print novo: grave um quadro do modelo com Playwright (veja como o `bb06_reel_antes_de_ir.py` faz) e salve em `prints/`.

**Reel** (1080×1920, 15 a 25 s, sem som): bases `posts-barb/r03_barb.py` (tour + arrastar antes e depois), `r04_barb_tabela.py` (tabela), `b08_reel_barb_clube.py` (clube), `bb06_reel_antes_de_ir.py` (equipe, espaço, avaliações, como chegar). Copie, mude `OUT` (`RAIZ + '/saida/<slug>'`), os títulos (`html_fundo`), a sequência e o cartão final `html_fim('R$ 399', ...)`. **Grave um reel por vez** (o servidor local usa porta fixa; dois ao mesmo tempo dão "Address already in use"). Cerca de 1 min cada.

**Stories** (1080×1920): base `posts-barb/stories_barb_2026_10_23.py`. Rodapé sempre com `@orbytstudio_`. Tipos: capa de post (`capa=` caminho do `01.png`), frase escura (`escuro=True`, `sub`, opcional `preco`) e modelo no celular (`cel=` print, no máximo 2 por semana). Salvar em `saida/stories-barb-AAAA-MM-DD/` (data da segunda).

**Legendas:** num arquivo `posts-barb/legendas_barb_AAAA_MM_DD.py` com `LEG` e `ALT` por slug (veja `legendas_barb_estreia.py`). 1ª linha = gancho com a palavra de busca ("site para barbearia"); 3 a 6 linhas curtas; uma pergunta quando fizer sentido; chamada pro WhatsApp pelo link do perfil; 0 a 3 hashtags. Texto alternativo em toda imagem com a palavra de busca. Story não leva legenda.

## 6. Conferir antes de publicar (obrigatório)

1. Abrir **cada** PNG (ou uma folha com todos lado a lado) com a ferramenta Read: texto cortado, texto em cima do celular, card vazio, texto branco em caixa branca, print errado, celular com topo em branco.
2. Ver 3 quadros de cada reel (`ffmpeg -ss 1 ...`, meio e `-sseof -1.5`) e abrir com Read.
3. `python3 checar.py posts-barb/<arquivos novos>.py` (inclua o de legendas). Tem que sair vazio.
4. Conferir preço: só R$ 399 (site), R$ 199 (landing) e R$ 1.497 (personalizado). Rode `grep -n "797" posts-barb/<arquivos novos>.py`: tem que sair vazio.

## 7. Publicar e agendar

1. `python3 publicar.py <pasta em saida> barbearia/posts/AAAA-MM-DD-<slug>` para cada post (data = dia em que sai), e `python3 publicar.py stories-barb-AAAA-MM-DD barbearia/stories/AAAA-MM-DD` para os stories.
2. `git add -A && git commit` (mensagem: "Barbearia, semana AAAA-MM-DD: 6 posts e 14 stories") e `git push`. Esperar 1 minuto antes de agendar.
3. Trypost, `create-post-tool`, conta **`01a164ce-6789-728e-a634-c998fa7d61fa`** (@orbytstudio_), `status: scheduled`, `scheduled_at` em UTC (tabela da seção 3). Link da mídia: `https://raw.githubusercontent.com/sarrafeiro/orbyt-instagram/main/<caminho>`.
   - Carrossel: `content_type: instagram_feed`, `media: [{url, alt}, ...]` (máximo 10), `content` = legenda.
   - Reel: `content_type: instagram_reel`, `meta: {"share_to_feed": true}`, `media: [{url, alt, meta: {"cover_offset_ms": 1200}}]`.
   - Story: `content_type: instagram_story`, `content: ""`, uma imagem por post.
   - Rótulos (`label_ids`): Barbearia `01a159da-2f00-737a-b28a-3ee515481e8d` (todo post de feed) · Story `01a159da-4349-712f-9f1c-dd48f783b1e2`.
   - Agendar cada um no horário exato. Não usar a fila automática.
   - Se o Trypost devolver erro de mídia, esperar 2 minutos e tentar de novo uma vez.
4. No fim, `list-posts-tool` com o canal da conta: tem que ter 20 agendados na semana, sem horário repetido.

## 8. Medir a semana que passou

1. `list-posts-tool` (publicados nos últimos 7 dias, canal da conta) e `get-post-metrics-tool` de cada um; `get-channel-insights-tool` da conta.
2. Anotar no `historico-barbearia.md`: alcance, salvamentos, compartilhamentos, comentários e visitas ao perfil por post (o que a ferramenta devolver; se não devolver, "sem dado", nunca estimar).
3. Regra do Matheus: seguir o que engajou, mas manter as outras linhas de conteúdo; não apostar tudo num sinal fraco. A partir de 4 semanas de dado, dobrar os 2 formatos ou pilares com mais (salvamentos + compartilhamentos) por alcance e cortar o pior. Anotar a decisão.
4. Sinal ruim: depois de 3 semanas, alcance quase só de seguidores → trocar 1 carrossel por reel.

## 9. Avisar o Matheus

Mensagem curta (ferramenta SendUserMessage), em português, sem travessão, com:
- os 6 temas da semana e o dia de cada um;
- os números da semana anterior em 3 linhas (melhor post, pior post, total de alcance);
- qualquer coisa que travou e o que ele precisa fazer (só se precisar).
Se algo travar antes de agendar (sem acesso ao Trypost ou ao GitHub), não inventar: avisar o que travou e parar.
