# Esercizio 14 - Simulazione di un gioco di dadi

punteggio = 0

while True:
    while True:
        
        dado_1 = input("Inserire il valore, da 1 a 6, del lancio del primo dado: ")
        dado_2 = input("Inserire il valore, da 1 a 6, del lancio del secondo dado: ")
        
        if dado_1.lstrip("-").isdigit() and dado_2.lstrip("-").isdigit():
            dado_1 = int(dado_1)
            dado_2 = int(dado_2)
            
            if 0 < dado_1 <= 6 and 0 < dado_2 <= 6:
                break
            else:
                print("\nErrore. Inserire un valore compreso tra 1 e 6 per entrambi i dadi")
        
        else:
            print("\nErrore. Inserire un valore intero e positivo. Riprova")

    somma_dadi = dado_1 + dado_2
    
    if dado_1 % 2 == 0 and dado_2 % 2 == 0 and somma_dadi > 8:
        punteggio = 100
        break
    
    elif dado_1 == 6 or dado_2 == 6 or somma_dadi == 7:
        punteggio += 10
        print(f"Punteggio attuale: {punteggio}")
        if punteggio == 100:
            break
    else:
        punteggio = 0
        break
    
if punteggio >= 100:
    print("Vittoria!")
    
else:
    print("Sconfitta!")
        

# Opzione 2 - Primo diagramma

punteggio = 0

while True:
    dado_1 = int(input("Inserire il valore, da 1 a 6, del lancio del primo dado: "))
    dado_2 = int(input("Inserire il valore, da 1 a 6, del lancio del secondo dado: "))

    if 0 < dado_1 <= 6 and 0 < dado_2 <= 6:
        somma_dadi = dado_1 + dado_2
            
        if dado_1 % 2 == 0 and dado_2 % 2 == 0 and somma_dadi > 8:
            punteggio = 100
            print("Vittoria!")
            break
        
        elif dado_1 == 6 or dado_2 == 6 or somma_dadi == 7:
            punteggio += 10
            print(f"Punteggio attuale: {punteggio}")
            
            if punteggio >= 100:
                print("Vittoria!")
                break
                
        else:
            print("Sconfitta!")
            break

    else:
        print("Errore. Inserire un valore compreso tra 1 e 6")
                    
            