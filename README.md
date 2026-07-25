# Analise-Arroz

## Escopo da analise

Dashboard simples que auxilie na visão macro (Valor do arroz, valor do dolar e diversos outras variaveis que impactam) para tomada de decisão do melhor momento para venda do arroz.

## Metodologia 

O projeto foi estruturadod com base no Scrum e Kanban por meio do software Jira.

Resumo do projeto

<img width="1562" height="890" alt="Image" src="https://github.com/user-attachments/assets/980f79f2-b6f4-4967-a34a-1d15cc7e431d" />

Kanban

<img width="1567" height="890" alt="Image" src="https://github.com/user-attachments/assets/573e3401-04c5-409c-ab81-47d370501b00" />

Backlog

<img width="1570" height="890" alt="Image" src="https://github.com/user-attachments/assets/6f29d5a8-3752-46f8-80c4-90607707a31b" />

## Como rodar o dadshboard

1 - Abra o cmd

```
mkdir dados_arroz
cd dados_arroz
python -m venv venv
```

2 - Instalar Bibliotecas

```
pip install dbt-duckdb
```

3 - Incializar o projeto

```
cd dados_arroz
dbt init dbt_case_arroz --skip-profile-setup
```

4 - Como abrir a pasta .dbt para ver o profile.yml ??

```
cd dbt_case_arroz
New-Item profiles.yml
```

```
cd models
New-Item stg_preco_arroz.sql
New-Item schema.yml
```

```
cd ..
dbt run --profiles-dir .
```

```
dbt test --profiles-dir .
```

## Como rodar dbt após tudo feito

```
dbt clean
dbt run --profiles-dir .
dbt test --profiles-dir .
```

## Rodando o dashboard

Via terminal abra a pasta ondde está o arquivo dashboard.py

```
streamlit run dashboard.py
```

## Fontes de dados

### CEPEA

Dados do valor historico do arroz em casca

> [!IMPORTANT]
> Esse caso não é uma API, mas sim um arquivo Excel que deve ser baixado e atualizado pelo site https://www.cepea.org.br/br/indicador/arroz.aspx clicando em serie de preços.
> O arquivo deve ser salvo mudando o tipo de arquivo de .XLS para .XLSX

### BCB

Valor do Dolar

### Conab

> [!IMPORTANT]
> Esse caso não é uma API, mas sim um arquivo Excel que deve ser baixado e atualizado pelo site https://portaldeinformacoes.conab.gov.br/download-arquivos.html
> O arquivo deve ser salvo mudando o tipo de arquivo de .XLS para .XLSX

#### Arquivos Conab
  - Series historicas grãos
  - Estimativa grãos
  - Oferta e demanda
  - Custo de produção
  - Preço agropecuaria mensal municipio
  - Preço agropecuaria mensal uf
  - Estoquue publicos
  - Frete

## Dashboard

