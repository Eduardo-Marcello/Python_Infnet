import requests
import pandas as pd

df = pd.read_csv('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv')
print(df)

for mes in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
    print(mes, round(df[mes].mean(), 2))

# Calcule a média anual
soma = 0
count = 0

for mes in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
    soma += df[mes].mean()
    count += 1
print(soma / count)

# Calcule a média anual por método
df_valores = df.T[4:]
for i in range(0, 15):
    print(df["GCM"][i], round(df_valores[i].mean(), 2))
