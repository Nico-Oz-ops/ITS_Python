'''
Tema: Cifratura semplice
Nome: XOR tra due stringhe

Obiettivo: Applicare lo XOR tra due stringhe della stessa lunghezza, simulando una “chiave segreta”.

Traccia:
Scrivi una funzione che riceve in input due stringhe della stessa lunghezza: una messaggio e una chiave.

Per ogni carattere del messaggio, esegui lo XOR tra il suo codice ASCII e quello del carattere 
corrispondente della chiave.
Restituisci la lista di numeri risultante.

Poi scrivi una funzione che, a partire dalla lista di numeri e la stessa chiave, ricostruisce la stringa originale.
'''

def cifrare(messaggio: str, chiave: str) -> list[int]:
    if len(messaggio) != len(chiave):
        raise ValueError("Errore, il messaggio e la chiave devono avere la stessa lunghezza.")

    return [ord(car) ^ ord(key) for car, key in zip(messaggio, chiave)]

def decifrare(numeri: cifrare, chiave: str) -> str:
    return ''.join(chr(num ^ ord(key)) for num, key in zip(numeri, chiave))

if __name__ == '__main__':
    stringa = input("Inserire la stringa da cifrare: ")
    chiave = input("Inserire la chiave da usare per lo XOR: ")

    cifrata = cifrare(stringa, chiave)
    print(f"Stringa cifrata: {cifrata}")

    decifrata = decifrare(cifrata, chiave)
    print(f"Stringa decifrata: {decifrata}")


# Con input() incluso

def cifrare() -> list[int]:

    while True:
        messaggio = input("Inserire un messaggio: ")
        chiave = input("Inserire una chiave lunga quanto il messaggio inserito previamente: ")

        if len(messaggio) != len(chiave):
            print("Errore, il messaggio e la chiave devono avere la stessa lunghezza.")

        else:
            break
    
    return [ord(car) ^ ord(key) for car, key in zip(messaggio, chiave)]
    

print(cifrare())

def decifrare() -> str:

    numeri = []
    while True:
        try:
            num = input("Inserire i numeri generati e digitare 'stop' per finire: ")

            if num == "stop":
                break

            numero = int(num)
            if numero not in numeri:
                numeri.append(numero)

        except ValueError:
            print("Errore, bisogna inserire i numeri interi giusti")

    chiave = input("Inserire la chiave: ")

    return ''.join(chr(num ^ ord(key)) for num, key in zip(numeri, chiave))

print(f"Messaggio originale: {decifrare()}")




