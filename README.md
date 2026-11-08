# Wave Pro — site público

Este repositório publica o site público do Wave Pro em `https://wavepromusic.github.io` por meio do GitHub Pages.

## Rotas públicas

- `/` — apresentação do aplicativo.
- `/track.html` — página de transição para links de músicas compartilhadas.
- `/hoje.html` — Sintonia do Dia, igual para todos os visitantes na data de São Paulo.
- `/privacy.html` e `/terms.html` — documentos públicos do aplicativo.
- `/app-ads.txt` — vendedores autorizados do inventário de anúncios.

## Android App Links

`/.well-known/assetlinks.json` ainda não é publicado. Ele exige a impressão digital SHA-256 exata do certificado de assinatura distribuído pela Google Play para `com.wavepro.app`; nunca use o certificado de depuração nesse arquivo.

Até uma versão futura do aplicativo reconhecer `wavepromusic.github.io`, os links antigos permanecem sendo a rota de compatibilidade do app.
