numeri_reali = [] #lista che conterrà tutti i numeri reali inseriti
somma_int = 0
count_int = 0

while True:
    num = float(input("Inserire una sequenza di numeri reali non negativi: "))
    if num < 0: #se il numero inserito è negativo il ciclo si interrompe.
        break

    numeri_reali.append(num) #se il numero è valido viene aggiunto alla lista numeri_reali.

    if num.is_integer(): #si verifica se il numero è intero.
        somma_int += num #si aggiorna la somma con i numeri interi inseriti.
        count_int += 1

if numeri_reali:
    media_num_interi = somma_int / count_int
    Num_Max = max(numeri_reali) #trova il numero più grande della lista numeri_reali.
    Num_Min = min(numeri_reali) #trova il numero più piccolo della lista numeri_reali.
    print(f"La media dei numeri interi è: \"{media_num_interi:.2f}\".")
    print(f"Il numero più grande è: \"{Num_Max:.2f}\"")
    print(f"Il numero più piccolo è: \"{Num_Min:.2f}\"")
else:
     print("Numero non valido")







    





    