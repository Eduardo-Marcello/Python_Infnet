import requests
from bs4 import BeautifulSoup
from collections import Counter


def count_words(single_word_def, text_def):
    for single_word_def in [p.text for p in single_word_def]:
        single_word_def = single_word_def.strip()
        text_def += single_word_def.lower().replace(",", "").replace(".", "") + " "
    count_def = Counter(text_def.split(" "))
    print(f"There are {len(count_def.items())} words in the text")
    return count_def


def find_single_words(count_def2, single_word_def2):
    for i, value in enumerate(count_def2.values()):
        if i == "ladies":
            print(f"The word {i} appears {value} times")
        if value == 1:
            single_word_def2.append(count_def2.get(value))
    print(f"The unique words that appear within the text:\n{single_word_def2}")


url = "http://brasil.pyladies.com/about"
dt = requests.get(url)
dt.encoding = dt.apparent_encoding
s = BeautifulSoup(dt.text, "lxml", from_encoding="utf-8")
Lines = s.find_all('p')
single_word = []
text = ""
count = count_words(single_word, text)
find_single_words(count, single_word)
