import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
sigla = input("Insira a sigla do estado: ")
estados = {}

if (sigla == "GO") or (sigla == "MT") or (sigla == "MS") or (sigla == "DF"):
    for div in soup.html.body.find_all("div", "linha"):
        estados[div.text] = div.get("linha")
    print(estados)
else:
    print("Estado não pertecente ao Centro-Oeste")
