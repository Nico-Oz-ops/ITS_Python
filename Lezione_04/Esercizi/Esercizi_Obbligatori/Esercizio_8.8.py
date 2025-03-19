# 8.8 - Album utente

def make_album(artista, titolo, song=None) -> dict[str]:
    album = {"Nome_Artista": artista, "Album": titolo, "Canzoni": song}

    return album

while True:
    scelta = input("Vuoi inserire un artista e il suo album? ")
    if scelta == "no".lower():
        print("ADios")
        break
    else:
        artista = input("Inserire il nome di un artista: ")

        titolo = input("Inserire un album dell'artista scelto: ")

    album = make_album(artista, titolo)

    print(album)



    



