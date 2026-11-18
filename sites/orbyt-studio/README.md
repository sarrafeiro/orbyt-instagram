# Site da Orbyt Studio (orbytstudio.com.br)

Tudo o que vai ao ar fica em `public/`. A Cloudflare (projeto `orbyt-studio`, Workers & Pages) está ligada a este repositório: cada push na `main` publica o site.

- Configuração na Cloudflare: Settings > Builds > raiz `sites/orbyt-studio`, branch `main`, comando de deploy `npx wrangler deploy`, sem comando de build.
- `wrangler.jsonc`: nome do projeto (`orbyt-studio`, igual ao da Cloudflare) e pasta dos arquivos (`public/`).
- `public/`: Home, vitrine e modelos (`modelos/`), LP de advogados (`advogados/`), LP de barbearias (`barbearias/`), atalhos (`_redirects`) e a LP dos 40 prompts de Medicina (`40prompts-estudante-medicina/`, com checkout em `40prompts-estudante-medicina/checkout/`).
- Base: zip do site de 19/10/2026 + parte de barbearias de 22/10 (versão com preços R$ 399 / 199 / 999), conferido arquivo por arquivo contra o site no ar em 17/11/2026.

**Este repositório é público. Nunca colocar aqui o PDF pago, chave do Mercado Pago ou qualquer senha.** Chaves ficam só nas configurações do projeto na Cloudflare (Settings > Variables and Secrets).

Ligado na Cloudflare em 17/11/2026 (Settings > Builds do projeto `orbyt-studio`).

## Pagamento (Mercado Pago) e entrega do PDF

- `src/index.js` é o servidor. Responde só em `/api/...`; o resto do site continua saindo de `public/`.
- Aplicação no Mercado Pago: "Orbyt Medicina" (Checkout Transparente, API de Orders). Webhook: `https://orbytstudio.com.br/api/mp/webhook`, evento Order.
- `src/40prompts.bin` é o PDF criptografado. Sem a chave não abre, então pode ficar no GitHub.
- Segredos na Cloudflare (orbyt-studio > Settings > Variables and Secrets, tipo Secret): `MP_ACCESS_TOKEN`, `PDF_KEY` e, quando tiver e-mail, `RESEND_API_KEY`.
- Trocar o PDF: criptografar de novo com a mesma chave e substituir `src/40prompts.bin`.

## Extras do checkout (order bump por fase)

- No checkout a pessoa escolhe a fase (ciclo básico, ciclo clínico, internato) e pode marcar 3 extras: OSCE (R$ 7,90), Simulados ENAMED (R$ 5,90) e Kit de prompts da fase (R$ 4,90). Os 3 juntos saem por R$ 9,90 e levam o Kit Acadêmico de bônus.
- Preços e nomes ficam em dois lugares: `src/index.js` (`EXTRAS`, `COMBO_CENTAVOS`, quem cobra de verdade) e `public/40prompts-estudante-medicina/checkout/index.html` (`EXTRAS_C`, `COMBO_C`, só o que aparece na tela). Mudou um, mude o outro.
- A escolha viaja na referência do pedido no Mercado Pago (`40p-pix-f3oek-...`: fase 3, o = OSCE, e = ENAMED, k = kit). A entrega lê dali.
- Os PDFs dos extras ficam criptografados com a mesma `PDF_KEY` em `public/40prompts-estudante-medicina/dl/` (`f1-osce.bin` ... `f3-kit.bin`, `academico.bin`). Formato: 12 bytes de IV + AES-GCM.
- Conferir se um extra abre: `/api/saude/extras?n=f1-osce` (um por vez).
- Trocar ou incluir um PDF de extra: como a chave só existe na Cloudflare, sobe-se temporariamente uma rota que cifra com a `PDF_KEY` (protegida por senha cujo hash vai no código), cifra-se o arquivo por ela, grava-se o `.bin` na pasta `dl/` e remove-se a rota. Foi assim em 17/11/2026 (ver histórico do git).
