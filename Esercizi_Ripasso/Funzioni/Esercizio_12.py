# Esercizio 12
'''Album: scrivi una funzione chiamata make_album() che costruisca un dizionario che descriva un album musicale. 
La funzione dovrebbe accettare un nome di artista e un titolo di album e dovrebbe restituire un dizionario contenente queste due informazioni. 
Usa la funzione per creare tre dizionari che rappresentano album diversi. Stampa ogni valore restituito per mostrare 
che i dizionari stanno memorizzando correttamente le informazioni dell'album. Usa None per aggiungere un parametro 
facoltativo a make_album() che ti consente di memorizzare il numero di brani in un album. 
Se la riga di chiamata include un valore per il numero di brani, aggiungi quel valore al dizionario dell'album. 
Crea almeno una nuova chiamata di funzione che includa il numero di brani in un album.'''

def make_album(nome_artista, album, canzoni=None) -> dict[str]:
    artista_album = {"artista": nome_artista, "titolo_album": album, "brani":canzoni}
    return artista_album

musicista = make_album("Led Zeppelin", "Led Zeppelin IV", 10)
print(make_album("Pink Floyd", "Dark Side of the Moon", 9))
print(make_album("Pink Floyd", "Animals"))
print(make_album("Pink Floyd", "Atom Heart Mother"))
print(musicista)
