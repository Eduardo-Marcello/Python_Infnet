import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "http://brasil.pyladies.com/about"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

paragrafos = soup.find_all('p')

palavras_unicas = []

texto = ""

for paragrafo in [p.text for p in paragrafos]:
    paragrafo = paragrafo.strip()
    texto += paragrafo.lower().replace(",", "").replace(".", "") + " "

count = Counter(texto.split(" "))
print("São", len(count.items()), "palavras no texto")

for key, value in count.items():
    if key == "ladies":
        print("A palavra ", key, "aparece nesta quantidade:", value)
    if value == 1:
        palavras_unicas.append(key)
print("Palavras únicas que aparecem dentro do texto:\n", palavras_unicas)
