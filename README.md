# Wave Pro — site público

Este repositório publica o site público do Wave Pro em `https://wavepromusic.github.io` por meio do GitHub Pages.

## Rotas públicas

- `/` — apresentação do aplicativo.
- `/track.html` — página de transição para links de músicas compartilhadas.
- `/hoje.html` — Sintonia do Dia, igual para todos os visitantes na data de São Paulo.
- `/privacy.html` e `/terms.html` — documentos públicos do aplicativo.
- `/app-ads.txt` — vendedores autorizados do inventário de anúncios.

## Android App Links

`/.well-known/assetlinks.json` foi publicado com a impressão digital SHA-256 do certificado de assinatura distribuído pela Google Play para `com.wavepro.app`. Em alterações futuras, nunca use o certificado de depuração nesse arquivo.

O aplicativo deve reconhecer somente `wavepromusic.github.io` como endereço público de compartilhamento.
