# Esercizio 01 - Trovare il numero massimo e minimo di un elenco di numeri

def massimo_minimo():
    numeri = []
    max_num = 0
    min_num = 0
    quantità = int(input("Quanti numeri vuoi inserire? "))

    for numero in range(quantità):
        numero = float(input("Inserire un numero: "))
        numeri.append(numero)
    
        max_num = numero
        min_num = numero

        if numero > max_num:
            print(f"Il numero massimo è {max_num}")
        else:
            if numero < min_num:
                print(f"Il numero minimo dell'elenco è {min_num}")

massimo_minimo()



    


    
