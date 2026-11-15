# Wave Pro — site público

Este repositório publica o site público do Wave Pro em `https://wavepromusic.github.io` por meio do GitHub Pages.

## Rotas públicas

- `/` — apresentação do aplicativo.
- `/track.html` — página de transição para links de músicas compartilhadas.
- `/hoje.html` — Sintonia do Dia, igual para todos os visitantes na data de São Paulo.
- `/privacy.html` e `/terms.html` — documentos públicos do aplicativo.
- `/app-ads.txt` — vendedores autorizados do inventário de anúncios.
- `/resignificar/catalog.json` — catálogo editorial somente-leitura usado pelo Wave para os conteúdos do canal Ressignificar Cada Dia.

## Catálogo Ressignificar

O workflow **Atualizar catálogo Ressignificar** consulta a publicação Atom pública do canal uma vez por hora e preserva os itens já catalogados em `/resignificar/catalog.json`. Não usa chave, YouTube Data API, scraping de páginas, nem segredos no aplicativo. Como o canal ainda não possui vídeos, o catálogo começa vazio; cada publicação nova passa a entrar na próxima sincronização. O workflow também pode ser iniciado manualmente na aba **Actions** após uma publicação.

## Android App Links

`/.well-known/assetlinks.json` foi publicado com a impressão digital SHA-256 do certificado de assinatura distribuído pela Google Play para `com.wavepro.app`. Em alterações futuras, nunca use o certificado de depuração nesse arquivo.

O aplicativo deve reconhecer somente `wavepromusic.github.io` como endereço público de compartilhamento.
