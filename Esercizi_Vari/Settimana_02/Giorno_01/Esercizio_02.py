'''
Tema: Funzioni ricorsive semplici
Obiettivo: Capire come una funzione ricorsiva può essere usata per sommare i numeri da 1 a n.
'''

# Esercizio 02
# Titolo: "Somma ricorsiva, da 1 a n"

'''
Traccia:
Scrivi una funzione chiamata somma_ricorsiva(n: int) -> int che calcoli la somma dei 
numeri da 1 a n in modo ricorsivo.

La somma si definisce così:

* Caso base:
somma_ricorsiva(1) = 1

* Passo ricorsivo:
somma_ricorsiva(n) = n + somma_ricorsiva(n - 1) per n > 1

Requisiti:
Gestisci correttamente il caso base (n == 1)

* Richiama la funzione solo se n > 1

Aggiungi una funzione test_somma() che:

* Chiede all’utente un intero positivo n
* Verifica che n >= 1
* Calcola e stampa la somma da 1 a n usando la funzione ricorsiva

Suggerimento:
Puoi strutturarlo in modo simile all’esercizio del fattoriale.
'''

def somma_ricorsiva(n: int) -> int:

    if n == 1:
        return 1
    
    else:
        return n + somma_ricorsiva(n - 1)

def test_somma() -> None:

    while True:

        try:
            input_num = int(input("Inserire un numero intero positivo: "))

            if input_num < 1:
                print("Il valore inserito deve essere almeno uno. Riprova")
            else:
                break
        
        except ValueError:
            print("Errore, il valore inserito non è un numero intero.")

    risultato = somma_ricorsiva(input_num)
    print(f"La somma da 1 a {input_num} è: {risultato}")

test_somma()

        



