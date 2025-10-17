# 💳 Bank Transaction Fraud Classification — Initial Data Loading Study

**Challenge:** [Rocketseat](https://app.rocketseat.com.br/projects/desenvolvimento-de-ia-arvore-de-decisao?module_slug=desafio-arvore-de-decisao&origin=%2Fprojects)

This repository contains an initial study of loading a bank transaction dataset with Python. The current script reads an Excel file into a pandas DataFrame; it does not yet train or evaluate a fraud classifier.

## Requirements

- Python 3
- pandas
- An Excel reader supported by pandas, such as `openpyxl`

Install the packages with:

```bash
pip install pandas openpyxl
```

## Data and execution

Place `transacoes_fraude.xlsx` in the `DataBase` directory, then run the script from the repository root:

```bash
python app.py
```

The script reads `DataBase/transacoes_fraude.xlsx` into `df`. The repository includes the data files in `DataBase/`.

## Next steps

Possible next steps include exploring the data, handling missing values and outliers, and developing and evaluating a classification model.

## Current limitation

The existing `read_excel` call passes an `encoding` argument, which is not part of the [current pandas API](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html). That call needs adjustment before running with current pandas. No model training or fraud-detection scores are implemented in this script.

## License

The existing educational-use permission allows study and improvement. See [license](license) for the original terms.
