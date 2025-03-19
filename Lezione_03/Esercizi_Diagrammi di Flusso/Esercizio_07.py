# Esercizio 7 - Algoritmo per il calcolo della media dei voti con inserimento iterativo

cont = 0
somma = 0
scelta = input("Vuole inserire un voto? Scegliere tra SI/NO: ").lower()

while scelta == "si":
        voto = input("Inserire un voto positivo: ")

        if voto.lstrip("-").isdigit():
            voto = int(voto)
            if voto > 0:
                cont += 1
                somma += voto     
            else:
                print("Errore. Il voto inserito deve essere positivo. Riprova a inserirlo")
        else:
            print("Errore. Il voto inserito deve essere un numero valido. Riprova a inserirlo")

        scelta = input("Vuole inserire un nuovo voto? Scegliere tra SI/NO: ").lower()
                
if cont > 0:
    media = somma / cont
    print(f"La media è {media}")
    
else:
    print("Nessun voto inserito")



        