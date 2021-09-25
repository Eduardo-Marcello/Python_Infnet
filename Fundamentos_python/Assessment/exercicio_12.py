import requests
from bs4 import BeautifulSoup


def check_acronyms(s_def, initials_def, country_def):
    if (initials_def == "GO") or (initials_def == "MT") or (initials_def == "MS") or (initials_def == "DF"):
        for i in s_def.html.body.find_all("div", "linha"):
            country_def[i.text] = i.get("linha")
        print(country_def)
    else:
        print("This state does not belong to Midwest")


url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
dt = requests.get(url).text
s = BeautifulSoup(dt, "lxml")
initials = input("Enter a state abbreviation: ")
country = {}
check_acronyms(s, initials, country)
