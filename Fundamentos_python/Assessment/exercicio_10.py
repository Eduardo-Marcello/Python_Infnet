import pandas as pd

url = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv")

year_filter = url['Year'] >= 2001
sports_filter = (url['Sport'] == 'Skating') | (url['Sport'] == 'Ice Hockey') | (url['Sport'] == 'Skiing') | \
                (url['Sport'] == 'Curling')
medal_filter = url['Medal'] == 'Gold'
total_gold_medal_NOR = url[(url['NOC'] == 'NOR') & sports_filter & medal_filter & year_filter]
total_gold_medal_SWE = url[(url['NOC'] == 'SWE') & sports_filter & medal_filter & year_filter]
total_gold_medal_DEN = url[(url['NOC'] == 'DEN') & sports_filter & medal_filter & year_filter]
lista = list(total_gold_medal_NOR.shape)
conquer_gold_NOR = lista[0]
lista = list(total_gold_medal_SWE.shape)
conquer_gold_SWE = lista[0]
lista = list(total_gold_medal_DEN.shape)
conquer_gold_DEN = lista[0]

if conquer_gold_NOR > conquer_gold_SWE and conquer_gold_NOR > conquer_gold_DEN:
    print(f"Noruega é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_NOR} medalhas")
elif conquer_gold_SWE > conquer_gold_NOR and conquer_gold_SWE > conquer_gold_DEN:
    print(f"Suéçia é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_SWE} medalhas")
else:
    print(f"Dinamarca é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_DEN} medalhas")

