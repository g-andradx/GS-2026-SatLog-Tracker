# SatLog Tracker – Sistema Inteligente de Rastreamento Logístico por Satélite

## Nome do Grupo

GRUPO SATLOG

### 👨‍🎓 Integrantes

# GUSTAVO ANDRADE RM564102


---

# 📜 Descrição

O SatLog Tracker é uma Prova de Conceito (POC) desenvolvida para a Global Solution 2026.1, com o objetivo de demonstrar como tecnologias espaciais podem ser aplicadas para otimizar processos logísticos na Terra.

A solução simula um sistema inteligente de monitoramento de cargas utilizando informações provenientes de satélites, GPS e sensores embarcados. O sistema coleta dados relacionados à temperatura da carga, velocidade média, distância até o destino, atraso da rota, qualidade do sinal de comunicação e status operacional.

A partir desses dados, técnicas de Ciência de Dados e Machine Learning são utilizadas para identificar padrões e prever o nível de risco de cada transporte, classificando-o como Baixo, Médio ou Alto risco.

O principal objetivo do projeto é auxiliar empresas de logística a identificar possíveis problemas durante o transporte antes que eles aconteçam, permitindo ações preventivas para reduzir atrasos, perdas financeiras e danos às mercadorias.

O projeto foi desenvolvido utilizando Python, Pandas, Scikit-Learn, Matplotlib, Seaborn e Streamlit. Os dados foram analisados por meio de gráficos, indicadores e dashboards interativos, permitindo uma visualização clara do comportamento das cargas monitoradas.

Entre os algoritmos avaliados, o Random Forest apresentou o melhor desempenho, sendo escolhido como modelo principal para a classificação do risco logístico.

A proposta demonstra como tecnologias baseadas em satélites e monitoramento remoto podem contribuir para aumentar a eficiência operacional, melhorar a tomada de decisão e reduzir riscos em operações logísticas.

---

# 📁 Estrutura de Pastas

## data

Contém a base de dados utilizada no projeto.

* satlog_data.csv

## src

Contém os códigos-fonte desenvolvidos.

* analise_satlog.ipynb
* modelo_ml.py
* dashboard.py
* gerar_dataset.py

## docs

Contém a documentação do projeto.

* gráficos gerados durante a análise
* matriz de confusão
* prints do dashboard
* diagramas e documentação complementar

## README.md

Documento principal contendo informações gerais do projeto.

---

# 📊 Resultados Obtidos

Durante os testes realizados com diferentes algoritmos de Machine Learning, foram obtidos os seguintes resultados:

* Random Forest: 100% de acurácia
* Regressão Logística: 94% de acurácia
* KNN: 84% de acurácia

O modelo Random Forest foi selecionado como modelo final devido ao seu excelente desempenho na classificação do risco das cargas.

A matriz de confusão demonstrou alta capacidade de classificação, identificando corretamente os diferentes níveis de risco presentes na base de dados.

---

# 📎 Links e Observações

## Link do Repositório

https://github.com/g-andradx/GS-2026-SatLog-Tracker

## Link do Vídeo

https://youtu.be/zp6RvReJ_jU


## Decisões Técnicas

* Utilização de dados simulados para representar cargas monitoradas por satélite.
* Aplicação de técnicas de análise de dados com Pandas.
* Utilização de Machine Learning para classificação de risco.
* Desenvolvimento de dashboard interativo utilizando Streamlit.
* Comparação entre diferentes algoritmos de classificação.
* Escolha do Random Forest como modelo final.

## Observações Gerais

Projeto desenvolvido para fins acadêmicos como Prova de Conceito (POC) da Global Solution 2026.1.

Participação no pódio: SIM

---

# 🔧 Como Executar o Código

## Pré-requisitos

* Python 3.11 ou superior
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit

## Instalação

1. Clonar o repositório.
2. Instalar as dependências do projeto.
3. Abrir o notebook de análise de dados.
4. Executar o treinamento do modelo de Machine Learning.
5. Executar o dashboard Streamlit.
6. Utilizar o simulador para prever o risco de novas cargas.

## Execução

1. Carregar a base de dados localizada na pasta `data`.
2. Executar os scripts da pasta `src`.
3. Iniciar o dashboard.
4. Acessar o sistema pelo navegador.

---

# 🚀 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Random Forest
* Regressão Logística
* KNN
* Streamlit
* GitHub

---

# 🛰️ Aplicação da Tecnologia Espacial

O projeto utiliza o conceito de monitoramento remoto por satélite para acompanhar cargas durante o transporte. A utilização de sistemas de posicionamento global (GPS) e comunicação via satélite permite coletar informações em tempo real, auxiliando na identificação de riscos operacionais e na tomada de decisões estratégicas.

---

# 🗃 Histórico de Lançamentos

## 1.0.0 - Junho/2026

* Desenvolvimento da base de dados.
* Implementação da análise exploratória.
* Criação dos gráficos e indicadores.
* Treinamento dos modelos de Machine Learning.
* Avaliação dos modelos.
* Construção do dashboard interativo.
* Implementação do simulador de previsão.
* Finalização da documentação do projeto.
