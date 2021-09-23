import pandas as pd

url = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv")

games_filter = (url['Genre'] == 'Platform') | (url['Genre'] == 'Action') | (url['Genre'] == 'Shooter')
year_filter = url['Year_of_Release'] >= 2011

games_filter_report = url[games_filter].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)

print("As tres marcas que mais publicaram esses generos foram: {}".format(games_filter_report))

filter_best_seller_all = url.groupby(['Publisher'])['Global_Sales'].sum().sort_values(ascending=False).head(3)

print("\n\nAs três marcas que mais venderam os três generos combinados foram: {}".format(filter_best_seller_all))


filter_jp_action = url[(url['Genre'] == 'Action') & year_filter].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)
filter_jp_shooter = url[(url['Genre'] == 'Shooter') & year_filter].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)
filter_jp_platform = url[(url['Genre'] == 'Platform') & year_filter].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)

print("\n\nA marca que mais publicações no genero ação foi: {}".format(filter_jp_action.head(1)),
      "\n\nA marca que mais publicações no genero tiro foi: {}".format(filter_jp_shooter.head(1)),
      "\n\nA marca que mais publicações no genero plataforma foi: {}".format(filter_jp_platform.head(1)))

filter_jp_seller_action = url[(url['Genre'] == 'Action') & year_filter].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)
filter_jp_seller_shooter = url[(url['Genre'] == 'Shooter') & year_filter].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)
filter_jp_seller_platform = url[(url['Genre'] == 'Platform') & year_filter].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

print("\n\nA marca que mais vendeu no genero ação foi: {}".format(filter_jp_seller_action.head(1)),
      "\n\nA marca que mais vendeu no genero tiro foi: {}".format(filter_jp_seller_shooter.head(1)),
      "\n\nA marca que mais vendeu no genero plataforma foi: {}".format(filter_jp_seller_platform.head(1)))
