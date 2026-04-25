class TekstiKasittelija:
    def __init__(self, teksti: str):
        self._teksti = teksti

    def poista_aakkoset(self):
        ääkkö_map = {
            'ä': 'a',
            'ö': 'o',
            'å': 'a',
            'Ä': 'A',
            'Ö': 'O',
            'Å': 'A'
        }

        uusi_teksti = self._teksti
        for merkki, korvaus in ääkkö_map.items():
            uusi_teksti = uusi_teksti.replace(merkki, korvaus)

        return TekstiKasittelija(uusi_teksti)

    def poista_valimerkit(self):
        välimerkit = [',', '.', '!', '?', ':', ';']

        uusi_teksti = self._teksti
        for merkki in välimerkit:
            uusi_teksti = uusi_teksti.replace(merkki, '')

        return TekstiKasittelija(uusi_teksti)

    def hae(self):
        return self._teksti

    def __str__(self):
        return self._teksti

    def pieniksi_kirjaimiksi(self):
        return TekstiKasittelija(self._teksti.lower())

    def laske_sanat(self):
        sanat = self._teksti.split()
        laskuri = {}

        for sana in sanat:
            if sana not in laskuri:
                laskuri[sana] = 1
            else:
                laskuri[sana] += 1

        return laskuri

    def print_dict(self, dictionary: dict):
        # järjestetään frekvenssin mukaan (suurin ensin)
        dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        for sana, maara in dictionary[:5]:
            print(f"{sana}: {maara}")


teksti = TekstiKasittelija(input("Syötä teksti: "))
tulos = teksti.poista_aakkoset().poista_valimerkit().pieniksi_kirjaimiksi()

print(tulos)
print_dict(tulos.laske_sanat())