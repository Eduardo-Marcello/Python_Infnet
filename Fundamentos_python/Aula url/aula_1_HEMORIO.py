import requests
import pandas as pd
from datetime import date

df = pd.read_csv('https://hemo-project.s3.amazonaws.com/data/blood-donors-all.csv')
print(df)


def get_date_in_str(valor):
  valor = str(valor)
  ano = valor[:4]
  mes = valor[4:6]
  dia = valor[6:]
  return datetime(int(ano), int(mes), int(dia))


df["date"] = df.datestr.apply(get_date_in_str)


