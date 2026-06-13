# Analise-Arroz

## To-do List

Ingestão

- [ ] Definir Stacks para o pipeline
- [ ] Conexão API Yahoo Finance
- [ ] Conexão API Nasdaq
- [ ] Conexão API USDA
- [ ] Conexão API CEPEA
- [ ] Conexão API Banco Central
- [ ] Conexão API IRGA
- [ ] Conexão API EMATER
- [ ] Conexão API INMET
- [ ] Conexão API Copernicus
      
  Tratamento

- [ ] dbt quality

Machine Learning

- [ ] Previsão de Safra
- [ ] Previsão de Preços

Vizualisação de dados

- [ ] Vizualisação de dados

## Fontes de dados

### Internacional: Bolsa de Chicago (CBOT) e Panorama Geral

#### API do Yahoo Finance (via biblioteca yfinance em Python):

- O que buscar: Histórico de preços diários do arroz futuro.

- Ticker: ZR=F (Rough Rice Futures).

#### API da Nasdaq Data Link (antigo Quandl)

- Dados oficiais e organizados de commodities agrícolas e dados macroeconômicos globais

#### USDA Quick Stats AP

- volumes de produção e comércio mundial

### Nacional (Brasil)

#### API do CEPEA (Esalq/USP)

- O Indicador do Arroz em Casca Esalq/Senar-RS é a grande referência nacional de preço físico.

#### API do Banco Central do Brasil (SGS - Sistema Gerenciador de Séries Temporais)

-   Taxa de câmbio (Dólar), inflação (IPCA/IGP-M) e dados de exportação/importação de commodities

#### IRGA (Instituto Rio Grandense do Arroz)

- Séries históricas exclusivas de preços de arroz em casca (como o Tipo 1, 58% de grãos inteiros), custos de produção por hectare e o acompanhamento semanal da colheita/plantio por região orizícola.

#### EMATER/RS-ASCAR

- Relatórios conjunturais semanais. Eles trazem os preços médios pagos ao produtor e a situação das lavouras em nível municipal e regional

#### Plataformas de Mercado Físico (ex: Notícias Agrícolas / Clicmercado)

- O que buscar: Cotações específicas de praças. Frequentemente há registros de preços FOB diretamente em cooperativas/indústrias da região de Capivari do Sul / Palmares do Sul (como os dados da Coripil, por exemplo). O acesso aqui geralmente exige técnicas de web scraping
- Planeta Arroz

### Clima e Satélite

#### API do INMET (Instituto Nacional de Meteorologia)

- Dados de estações meteorológicas automáticas próximas a Palmares do Sul (temperatura, precipitação acumulada)

#### Copernicus (Open Access Hub) ou Google Earth Engine

- Imagens de satélite (Sentinel/Landsat) para calcular índices de vegetação (como o NDVI) sobre as áreas de lavoura de Palmares do Sul. Isso permite monitorar a saúde do arroz em tempo real e prever produtividade antes da colheita terminar

## Pipeline de dados

<img width="1408" height="768" alt="Image" src="https://github.com/user-attachments/assets/3e545abf-5a25-48c3-a071-7143b7d114a5" />




