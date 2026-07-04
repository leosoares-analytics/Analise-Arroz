# Analise-Arroz

## To-do List

### Configuração básica

- [x] Criar ambiente para este projeto
- [ ] Pesquisar na IA quais KPIs e analises estatisticas posso incluir para ajudar na tomada de decisão e quais dados/informações são relevantes para analise do preço do arroz

### Ingestão

- [x] Definir Stacks para o pipeline
- [x] Conexão API CEPEA --> Arquivo via Excel
- [x] DDados coperativa
- [ ] NewsAPI para filtrar as noticias mais relevantes dos ultimos 30 dias em relação ao preço do arroz
- [ ] Corrigir Awesome API para puxar valores historicos

### Vizualisação de dados

- [x] Graficos de historico e sazonalidade do preço do arroz
- [x] Gap entre valor de mercado e coperativa
- [ ] Noticias de contexto
- [x] KPIs relevantes
- [x] Preço do dia
- [x] Média do valor do arroz

### Forecasting

#### Ingestão de dados Forecasting

- [x] Indicador CEPEA/ESALQ (Arroz em Casca)
- [ ] Estoque de Passagem e Intenção de Plantio (CONAB)
- [ ] Custos de Produção (Insumos)
- [ ] Taxa de Câmbio (USD/BRL) --> Awesome API
- [ ] Preço do Arroz na Bolsa de Chicago (CBOT)
- [ ] Inflação (IPCA / IGP-M)
- [ ] Anomalias de Temperatura e Precipitação (Chuvas)
- [ ] Eventos Climáticos Globais (El Niño / La Niña) (como o ONI - Ocean Niño Index)

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


## Forecasting

Para alimentar modelos mais avançados que o Prophet tradicional (como o SARIMAX, XGBoost ou o Skforecast), você precisará criar "lags" (atrasos temporais) dessas variáveis, já que o impacto do clima ou do dólar de hoje não altera o preço do arroz instantaneamente, mas sim semanas depois.

Veja como você prepararia esse DataFrame no Pandas:

'''
import pandas as pd

# Supondo que você coletou dados diários ou semanais de fontes como CEPEA, BCB e INMET
df = pd.read_csv("dados_arroz.csv", parse_dates=['data'], index_index='data')

1. Definindo a variável alvo
df['preco_arroz'] = df['indicador_cepea']

2. Criando Lags das variáveis preditoras (O dólar de 7 e 30 dias atrás influencia hoje)
df['dolar_lag_7'] = df['dolar'].shift(7)
df['dolar_lag_30'] = df['dolar'].shift(30)

3. Criando médias móveis para suavizar o ruído do clima
df['chuva_media_30d'] = df['precipitacao_RS'].rolling(window=30).mean()

4. Variáveis de calendário (Sazonalidade de Safra vs Entresafra)
O preço do arroz costuma cair na época de colheita (março a maio) por excesso de oferta
df['mes'] = df.index.month
df['epoca_colheita'] = df['mes'].isin([3, 4, 5]).astype(int)

Remover os valores nulos gerados pelos 'shifts'
df_treino = df.dropna()
'''

### Qual modelo escolher para esse cenário?
- Se você quer focar em variáveis externas (Clima + Dólar): Use XGBoost, LightGBM ou a biblioteca Skforecast. Eles lidam muito bem com relacionamentos não-lineares (ex: se a chuva passar de um limite X, o preço sobe Y devido à inundação).

- Se você quer focar na tendência de mercado puro com impactos pontuais: Use o SARIMAX do statsmodels, onde as variáveis econômicas entram como variáveis exógenas (exog).

- Dica para o Dashboard no Streamlit
Como o objetivo é a venda do arroz, crie um simulador no Streamlit onde o usuário possa alterar cenários fictícios. Exemplo: "E se o dólar subir para R$ 5,80 no próximo mês, o que acontece com a curva de preço?".

Você pode usar os sliders do Streamlit para colher essas hipóteses do usuário, aplicá-las ao modelo mutivariado e plotar o impacto simulado na tela.

