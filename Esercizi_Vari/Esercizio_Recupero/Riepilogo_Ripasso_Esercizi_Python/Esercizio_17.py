'''
Definire una funzione che prende una lista di stringhe
e restituisce un dizionario con le parole e la loro frequenza
'''

def conta_frequenza(lista_stringhe: list[str]) -> dict[str, int]:
    frequenze = {}
    # Creo un dizionario vuoto che conterrà le parole come chiavi e il numero di occorrenze come valori

    for frase in lista_stringhe:
    # Itero su ogni stringa (frase) presente nella lista
        parole = frase.split()
        # Divide la frase in parole separate (usando gli spazi come separatori).
        for parola in parole:
            # Itera su ciascuna parola ottenuta dalla frase.

            parola_pulita = "".join(carattere for carattere in parola.lower() if carattere.isalnum())
            # Converte la parola in minuscolo e rimuove tutti i caratteri non alfanumerici
            # (come punteggiatura, spazi o simboli).

            if parola_pulita:
                # Controlla che la parola non sia vuota dopo la pulizia.

                if parola_pulita in frequenze:
                    frequenze[parola_pulita] += 1
                else:
                    frequenze[parola_pulita] = 1
    
    return frequenze

lista = ["Ciao ! ", "mondo", "Ciao", "Python.", "Ciao, Mondo", "CIAO!", "co,me"]
print(conta_frequenza(lista))