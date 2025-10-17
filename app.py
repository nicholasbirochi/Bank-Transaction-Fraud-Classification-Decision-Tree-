import pandas as pd
import numpy as np
import os

xlsx_file = r".\DataBase\transacoes_fraude.xlsx"
df = pd.read_excel(xlsx_file, encoding='utf-8')