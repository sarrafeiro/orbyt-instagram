# Site da Orbyt Studio (orbytstudio.com.br)

Tudo o que vai ao ar fica em `public/`. A Cloudflare (projeto `orbyt-studio`, Workers & Pages) está ligada a este repositório: cada push na `main` publica o site.

- Configuração na Cloudflare: Settings > Builds > raiz `sites/orbyt-studio`, branch `main`, comando de deploy `npx wrangler deploy`, sem comando de build.
- `wrangler.jsonc`: nome do projeto (`orbyt-studio`, igual ao da Cloudflare) e pasta dos arquivos (`public/`).
- `public/40prompts-estudante-medicina/`: LP e checkout do pacote de 40 prompts de Medicina.

**Este repositório é público. Nunca colocar aqui o PDF pago, chave do Mercado Pago ou qualquer senha.** Chaves ficam só nas configurações do projeto na Cloudflare (Settings > Variables and Secrets).
