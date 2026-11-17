# Site da Orbyt Studio (orbytstudio.com.br)

Tudo o que vai ao ar fica em `public/`. A Cloudflare (projeto `orbyt-studio`, Workers & Pages) está ligada a este repositório: cada push na `main` publica o site.

- Configuração na Cloudflare: Settings > Builds > raiz `sites/orbyt-studio`, branch `main`, comando de deploy `npx wrangler deploy`, sem comando de build.
- `wrangler.jsonc`: nome do projeto (`orbyt-studio`, igual ao da Cloudflare) e pasta dos arquivos (`public/`).
- `public/`: Home, vitrine e modelos (`modelos/`), LP de advogados (`advogados/`), LP de barbearias (`barbearias/`), atalhos (`_redirects`) e a LP dos 40 prompts de Medicina (`40prompts-estudante-medicina/`, com checkout em `40prompts-estudante-medicina/checkout/`).
- Base: zip do site de 19/10/2026 + parte de barbearias de 22/10 (versão com preços R$ 399 / 199 / 999), conferido arquivo por arquivo contra o site no ar em 17/11/2026.

**Este repositório é público. Nunca colocar aqui o PDF pago, chave do Mercado Pago ou qualquer senha.** Chaves ficam só nas configurações do projeto na Cloudflare (Settings > Variables and Secrets).

Ligado na Cloudflare em 17/11/2026 (Settings > Builds do projeto `orbyt-studio`).
