def poista_ääkkö(lista: list):
    ääkkö = ['ä', 'ö']

    uusi_lista = []
    for sana in lista:
        for merkki in ääkkö:
            if merkki == 'ä':
                sana = sana.replace(merkki, 'a')
            elif merkki == 'ö':
                sana = sana.replace(merkki, 'o')
        if sana:
            uusi_lista.append(sana)

    return uusi_lista


def print_list_as_string(lista: list):
    string = ' '.join(lista)

    return print(string)


teksti = input('Syötä teksti, josta haluat poistaa ääkköset: ')
teksti_lista = teksti.split()
muokattu_teksti = poista_ääkkö(teksti_lista)
print_list_as_string(muokattu_teksti)

