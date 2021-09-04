from collections import defaultdict


def conta_palavras(paragrafo_def):
    palavras = defaultdict(int)
    for palavra in paragrafo.split(" "):
        palavras[palavra] += 1
    print(palavras)
    return palavra


paragrafo = """Essas vacinas usam duas plataformas diferentes para combater o vírus. A AstraZeneca usa vetor viral (
adenovírus de chimpanzé atenuado) e a Pfizer usa o RNA mensageiro (ou mRNA), que tem uma pequena sequência genética 
criada em laboratório que "ensina" as próprias células do corpo humano a se protegerem contra o Sars-CoV-2. """
paragrafo.replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace('"', "")
conta_palavras(paragrafo)
