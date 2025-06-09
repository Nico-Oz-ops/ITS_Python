# Esercizio 01
'''
Cifrario di Cesare

Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell’alfabeto minuscole scrivendo from string import ascii_lowercase

Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…

Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.

● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c

Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:

● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.

La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.

Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata.
'''

from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s, key):

    cifrare = []

    for carattere in s: 

        if carattere in ascii_lowercase:

            indice = (ascii_lowercase.index(carattere) + key) % 26 # per trovare la posizione (l'indice) della lettera minuscola, 
            cifrare.append(ascii_lowercase[indice])                 # per poi sommare la key e tornare da capo se si supera "z" (non uscire fuori dall'alfabeto)
                                                                    # e infine il carattere si aggiungge alla lista cifrare
        elif carattere in ascii_uppercase:
            indice = (ascii_uppercase.index(carattere) + key) % 26
            cifrare.append(ascii_uppercase[indice])
        
        else:
            cifrare.append(carattere)
    
    return cifrare

def caesar_cypher_decrypt(s, key):

    decifrare = []

    for carattere in s:
        
        if carattere in ascii_lowercase:                            # si applica la stessa procedura per il cifrato 
                                                                    # ma muovendosi all’indietro nell’alfabeto
            indice = (ascii_lowercase.index(carattere) - key) % 26 
            decifrare.append(ascii_lowercase[indice])
        
        elif carattere in ascii_uppercase:
            indice = (ascii_uppercase.index(carattere) - key) % 26
            decifrare.append(ascii_uppercase[indice])
        
        else:
            decifrare.append(carattere)
    
    return decifrare


messaggio = "Ciao, come va? Hai capito qualcosa? O continui ad essere una capra di monte?"
chiave = 5
cifrato = caesar_cypher_encrypt(messaggio, chiave)
decifrato = caesar_cypher_decrypt(messaggio, chiave)

print(f"Messaggio cifrato: {cifrato}")
print(f"Messaggio decifrato: {decifrato}")
            


