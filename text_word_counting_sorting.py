from re import split

def poista_välimerkit(teksti):
    välimerkit = [',', '.', '!', '?']
    lista = teksti.split()

    uusi_lista = []
    for sana in lista:
        for merkki in välimerkit:
            sana = sana.replace(merkki, "")
        if sana:  # ettei jää tyhjiä
            uusi_lista.append(sana)

    return uusi_lista


def laske_sanat(lista: list):
    d = {}
    for sana in lista:
        if sana not in d:
            d[sana] = 1
        else:
            d[sana] += 1
    return d


def print_dict(dictionary):
    # järjestetään frekvenssin mukaan (suurin ensin)
    jarjestetty = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    for sana, maara in jarjestetty[:5]:
        print(f"{sana}: {maara}")


# Main
while True:
    input_teksti = input('Input text here: ').lower()
    raaka_teksti = poista_välimerkit(input_teksti)
    d = laske_sanat(raaka_teksti)
    print_dict(d)