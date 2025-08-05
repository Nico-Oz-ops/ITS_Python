'''
Obiettivo: Allenarti a usare il ciclo for per stampare una 
sequenza numerica da 1 a un numero scelto dall’utente.
'''

# Esercizio 02
# Titolo: "Conta fino a N"

'''
Scrivi una funzione conta_fino_a() che:

- Chiede all’utente di inserire un numero intero positivo N
- Stampa tutti i numeri da 1 fino a N inclusi, uno per riga
- Se il numero non è positivo o non è un intero, stampa un messaggio d’errore

Suggerimenti:
* Usa range(1, N + 1) per generare i numeri da 1 a N
* Ricorda che range(1, 6) produce: 1, 2, 3, 4, 5
* Controlla che N > 0 prima di iniziare a stampare
'''

def conta_fino_a() -> int:
    try:
        input_num = int(input("Inserire un numero intero positivo: "))
    
    except ValueError:
        print("Errore, il numero inserito deve essere intero")
        return

    if input_num <= 0:
        print(f"Errore, il numero inserito deve essere positivo")
        return

    for num in range(1, input_num + 1):
        print(num)

conta_fino_a()
















