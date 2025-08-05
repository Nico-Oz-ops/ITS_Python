'''
Tema: Ricorsione semplice
Obiettivo: Imparare a scomporre un numero intero in singole cifre usando la ricorsione.
'''

# Esercizio 03
# Titolo: "Conta cifre ricorsiva"

'''
Traccia:
Scrivi una funzione chiamata conta_cifre(n: int) -> int che restituisce il 
numero di cifre di un intero positivo n, usando la ricorsione.

Esempi:

conta_cifre(7) → 1
conta_cifre(123) → 3
conta_cifre(98765) → 5

Regole:
* Caso base: se n < 10, allora ha una sola cifra → ritorna 1
* Passo ricorsivo: conta_cifre(n) = 1 + conta_cifre(n // 10)

Requisiti:
Scrivi anche una funzione test_conta_cifre() che:

* Chiede all’utente un numero intero positivo
* Valida l’input
* Stampa quante cifre ha il numero inserito

Suggerimento:
Il simbolo // è la divisione intera:
123 // 10 = 12, 12 // 10 = 1, 1 // 10 = 0
'''

def conta_cifre(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + conta_cifre(n // 10)

def test_conta_cifre():

    while True:

        try:
            input_num = int(input("Inserire un numero intero positivo: "))

            if input_num < 0:
                print("Errore, il valore inserito deve essere un numero positivo.")
            
            elif input_num < 10:
                print("Errore, il valore inserito deve essere composto da almeno 2 cifre.")

            else:
                break
        
        except ValueError:
            print("Errore, il valore inserito deve essere un numero intero")
        
    risultato = conta_cifre(input_num)
    print(f"{input_num} è composto da {risultato} cifre")

test_conta_cifre()
