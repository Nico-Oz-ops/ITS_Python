# Esercizio 13
'''Album utente: inizia con il tuo programma dall'esercizio 8-7. 
Scrivi un ciclo while che consenta agli utenti di immettere l'artista e il titolo di un album. 
Una volta ottenute queste informazioni, chiama make_album() con l'input dell'utente e stampa il dizionario creato. 
Assicurati di includere un valore quit nel ciclo while.'''

def make_album(nome_artista, album, canzoni=None) -> dict[str]:
    artista_album = {"artista": nome_artista, "titolo_album": album, "brani":canzoni}
    return artista_album

while True:
    scelta = input("Vuoi inserire il nome di un artista e un suo album? ").lower()
    if scelta == "no":
        print("Operazione finita!")
        break
    else:
        nome_artista = input("Inserisci il nome dell'artista: ").title()
        album = input("Inserisci il nome dell'album: ").title()

# Non lo chiede la traccia dell'esercizio, ma se volessi aggiungere canzoni all'album, farei così...
        scelta_canzoni = input("Vuoi inserire il numero di canzoni dell'album scelto: ").lower()
        if scelta_canzoni == "no":
            canzoni = None                                                          
        else:
            canzoni = int(input("Inserire il numero di canzoni: "))
 
    info_artista = make_album(nome_artista, album, canzoni)
    print(info_artista)




