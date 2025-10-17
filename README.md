# 💳 Bank Transaction Fraud Classification – Decision Tree

**Challenge:** [Rocketseat](https://app.rocketseat.com.br/projects/desenvolvimento-de-ia-arvore-de-decisao?module_slug=desafio-arvore-de-decisao&origin=%2Fprojects)  
**Brief:** Train a Decision Tree to flag fraudulent transactions. Includes quick EDA, light feature preparation, imbalance handling, and evaluation via ROC-AUC / PR-AUC metrics.

## 🧠 Objective
Develop a Machine Learning model capable of detecting potential fraudulent transactions based on transaction metadata.

## ⚙️ Tech Stack
- Python 3.x  
- Scikit-learn  
- Pandas / NumPy  
- Matplotlib / Seaborn (for EDA)

## 🧩 Steps
1. Exploratory Data Analysis (EDA)
2. Feature engineering and preprocessing
3. Model training using Decision Tree
4. Evaluation via ROC-AUC and PR-AUC
5. Fraud detection performance review

## 📊 Results
- Balanced accuracy improvement via class weighting  
- ROC-AUC and PR-AUC results showing model robustness  

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
```

# 🧠 Classificação de Fraudes em Transações

Este projeto tem como objetivo realizar uma **análise exploratória** e futura **classificação de fraudes em transações financeiras**, utilizando **Python** com as bibliotecas **Pandas** e **NumPy** para manipulação e análise dos dados.

## 📂 Estrutura do Projeto

```
📁 7_-_Classificação_de_Fraudes_em_Transações_Bancárias
├── 📁 DataBase
│ ├── 📁 __MACOSX # Base auxiliar gerada no macOS
│ │ └── 📄 transacoes_fraude.csv # Base de dados (cópia automática)
│ └── 📄 transacoes_fraude.csv # Base de dados principal
├── 🧮 app.py # Script principal de leitura e análise inicial
└── 📝 README.md # Documentação do projeto
```

## ⚙️ Dependências

Antes de executar o projeto, garanta que o ambiente virtual esteja configurado e as dependências instaladas:

```bash
pip install pandas numpy
```

## 🚀 Execução

1. Verifique se o arquivo `transacoes_fraude.csv` está dentro da pasta `DataBase`.
2. Execute o script `app.py`:

```bash
python app.py
```

## 🧩 Código Principal

```bash
import pandas as pd
import numpy as np
import os

# Caminho do arquivo CSV
csv_file = r".\DataBase\transacoes_fraude.csv"

# Leitura dos dados
pd.read_csv(csv_file)
```

## 🧩 Explicação

- **pandas (`pd`)**: utilizado para manipulação de dados em formato tabular.  
- **numpy (`np`)**: útil para cálculos numéricos e operações com matrizes.  
- **os**: permite interagir com o sistema operacional (ex: manipular caminhos de arquivos).  
- O arquivo CSV é lido e carregado como um **DataFrame** através do comando `pd.read_csv()`.

## 🧠 Próximos Passos

- Realizar **análise exploratória dos dados (EDA)**.  
- Tratar **valores nulos** e **outliers**.  
- Criar **modelos de classificação** para detecção de fraudes.  
- Avaliar o desempenho dos modelos com métricas como **precisão**, **recall** e **F1-score**.

## 🧾 Licença

Este projeto é de **uso educacional** e está **livre para estudo e aprimoramento**.