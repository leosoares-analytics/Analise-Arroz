# Analise-Arroz

## To-do List

### Configuração básica

- [x] Criar ambiente para este projeto
- [ ] Pesquisar na IA quais KPIs e analises estatisticas posso incluir para ajudar na tomada de decisão e quais dados/informações são relevantes para analise do preço do arroz

### Ingestão

- [x] Definir Stacks para o pipeline
- [ ] Conexão API Yahoo Finance (USA/BRL , ETFs Agriculas , Indices de commodities) 
- [x] Conexão API CEPEA --> Arquivo via Excel
- [ ] Conexão API Banco Central ddo Brasil [BCB]
- [ ] Webscaping coperativa
- [ ] NewsAPI para filtrar as noticias mais relevantes dos ultimos 30 dias em relação ao preço do arroz
- [ ] Criar base dded dados "macro contexto" em relação anoticias de 2005 a maio de 2026 para anlise do preço do arroz

### Vizualisação de dados

- [x] Graficos de historico e sazonalidade do preço do arroz
- [ ] Gap entre valor de mercado e coperativa
- [ ] Noticias de contexto
- [ ] KPIs relevantes
- [x] Preço do dia
- [ ] Média do valor do arroz
- [ ] Forecasting
- [ ] Desvio Padrão e Variância do Preço: Mede a instabilidade do mercado. Alta volatilidade exige mais cautela e monitoramento frequente; baixa volatilidade indica um mercado mais previsível
- [ ] Análise de Quartis e Percentis (Preço Histórico): Descobrir em qual faixa o preço atual se encontra em relação ao histórico. Por exemplo: "O preço atual de R$ X está no percentil 90 dos últimos 3 anos". Se estiver no topo (percentil alto), costuma ser um excelente sinal de venda

## Escopo da analise

Dashboard simples que auxilie na visão macro (Valor do arroz, valor do dolar e diversos outras variaveis que impactam) para tomada de decisão do melhor momento para venda do arroz.

## Criação do Ambiente

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
> Esse caso não é uma API, mas sim um arquivo Excel que deve ser baixado e atualizado pelo site https://www.cepea.org.br/br/indicador/arroz.aspx clicando em serie ded preços.
> O arquivo deve ser salvo mudando o tipo de arquivo de .XLS para .XLSX

### API Yahoo Finance

Dados Coletados
'''
- USD/BRL : razão dolar / real
- ZR=F : representa os contratos futuros de Rough Rice negociados na CBOT/CME.
- DBA : exposição a futuros agrícolas como milho, soja, trigo, açúcar, café, algodão e pecuária.
- MOO : investe em empresas ligadas ao agronegócio, como fertilizantes, sementes, máquinas agrícolas e processamento agrícola.
'''
## Pipeline de dados

<img width="1408" height="768" alt="Image" src="https://github.com/user-attachments/assets/3e545abf-5a25-48c3-a071-7143b7d114a5" />




