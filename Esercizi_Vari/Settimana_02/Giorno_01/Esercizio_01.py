'''
Tema: Funzioni ricorsive semplici
Obiettivo: Comprendere la struttura di una funzione ricorsiva, partendo da un classico semplice.
'''

# Esercizio 01
# Titolo: "Fattoriale ricorsivo"

'''
Traccia:
Scrivi una funzione chiamata fattoriale(n: int) -> int che calcola il 
fattoriale di un numero intero n in modo ricorsivo.

Il fattoriale di un numero intero positivo n si definisce così:

* fattoriale(0) = 1 (caso base)
* fattoriale(n) = n * fattoriale(n - 1) per n > 0

La funzione deve:

* Gestire il caso base correttamente.
* Applicare la ricorsione solo per n > 0.
* Infine, crea una funzione test_fattoriale() che:
* Chiede all’utente un numero intero ≥ 0,
* Calcola e stampa il suo fattoriale usando la funzione ricorsiva.

Suggerimento:
Ricorda di validare l’input in test_fattoriale() per evitare numeri negativi.
'''

def fattoriale(n: int) -> int:

    if n == 0:
        return 1
    
    else:
        return n * (fattoriale(n - 1))

def test_fattoriale() -> None:

    while True:
            
        try:
            input_num = int(input("Inserire un numero intero uguale o maggiore di zero: "))

            if input_num < 0:
                print("Errore, il valore inserito deve essere un intero maggiore o uguale di zero")
            
            else:
                break

        except ValueError:
            print("Errore, il valore inserito deve essere un numero intero")
        
    risultato = fattoriale(input_num)

    print(f"Il fattoriale di {input_num}: {risultato}")

test_fattoriale()



        
