# LP 40 Prompts de Medicina (Orbyt Studio para Medicina)

Site estático publicado na Cloudflare (Workers & Pages, ligado a este repositório).

- `index.html`: landing page.
- `checkout/index.html`: checkout (endereço `/checkout/`).
- `img/`: imagens da LP.

Configuração na Cloudflare: diretório raiz `sites/prompts-medicina`, sem comando de build, pasta de saída `.` (a própria raiz).

Preço e preço "de": variáveis `PRECO` e `PRECO_DE` no fim de cada página. Média de vendas por dia: `VENDAS_BASE`.

O pagamento (Mercado Pago) ainda não está ligado: o checkout mostra a faixa "Prévia" e o botão de simular aprovado.
**Nunca colocar o PDF pago neste repositório: ele é público.**
