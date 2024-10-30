# Conversor de Imagens para WebP

Este projeto é um script Python que converte imagens de vários formatos para o formato WebP. O script também remove imagens PNG após a conversão, mantendo apenas as imagens convertidas e as que já estão no formato WebP.

## Funcionalidades

- Converte imagens nos seguintes formatos: .jpg, .jpeg, .png, .bmp, .tiff, .gif.
- Ignora arquivos que já estão no formato .webp.
- Remove arquivos .png após a conversão.
- Exibe um resumo da execução com:
  - Número de imagens convertidas
  - Número de imagens puladas (já em WebP)
  - Número de imagens PNG apagadas
  - Comparativo do peso da pasta antes e depois da conversão

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - Pillow (para manipulação de imagens)
  - Colorama (para colorir as saídas no terminal)

### Instalação das Bibliotecas

Para instalar as bibliotecas necessárias, execute o seguinte comando:

pip install Pillow colorama

## Como Usar

1. Clone ou baixe o repositório.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute o script, passando o caminho da pasta que contém as imagens como argumento:

python converter.py <caminho_da_pasta>

Substitua <caminho_da_pasta> pelo caminho da pasta que contém suas imagens.

## Exemplo de Uso

python converter.py C:\caminho\para\sua\pasta

## Exemplo de Saída

Após a execução do script, você verá mensagens coloridas no terminal indicando o status das conversões e um resumo no final:

Convertido para WebP: C:\caminho\para\sua\pasta\imagem1.webp
Pulado (já em WebP): C:\caminho\para\sua\pasta\imagem2.webp
PNG removido: C:\caminho\para\sua\pasta\imagem3.png

=== Resumo da Execução ===
Imagens Convertidas para WebP: 5
Imagens Puladas (já em WebP): 2
Imagens PNG Apagadas: 3

Tamanho da pasta antes da conversão: 15.30 MB
Tamanho da pasta após a conversão: 10.50 MB
Diferença no tamanho: 4.80 MB