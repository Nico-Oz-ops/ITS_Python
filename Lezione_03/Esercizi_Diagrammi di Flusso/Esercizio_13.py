# Esercizio 13 - Esercizio di controllo numerico con condizioni arbitrarie

# while True:
#     x = input("Inserire un numero \"X\" intero positivo: ")
    
#     if x.isdigit() and int(x) >= 0:
#         x = int(x)
#         break
#     else:
#         print("Errore. Il valore di \"X\" deve essere intero e positivo. Riprova")

# while True:
#     y = input("Inserire un numero \"Y\" intero positivo: ")
    
#     if y.isdigit() and int(y) >= 0:
#         y = int(y)
#         break
#     else:
#         print("Errore. Il valore di \"Y\" deve essere intero e positivo. Riprova")

# while True:
#     z = input("Inserire un numero \"Z\" intero positivo: ")
    
#     if z.isdigit() and int(z) >= 0:
#         z = int(z)
#         break
#     else:
#         print("Errore. Il valore di \"Z\" deve essere intero e positivo. Riprova")

# somma = x + y + z

# if somma % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
#     print("Regole rispettate")

# else: 
#     print("Regole non rispettate")


# Opzione 2 - Funzione

def chiedere_numero_positivo(name:str):
    while True:
        valore = input(f"Inserire un valore \"{name}\" intero e positivo: ")

        if valore.isdigit() and int(valore) >= 0:
            valore = int(valore)
            return valore # restituisce il numero intero inserito. Permette di utilizzare il valore inserito fuori dalla funzione, assegnandolo alle variabili
        else:
            print(f"Errore. Il valore di \"{name}\" deve essere intero e positivo. Riprova")

valore_X = chiedere_numero_positivo("X")
valore_Y = chiedere_numero_positivo("Y")
valore_Z = chiedere_numero_positivo("Z")

somma = valore_X + valore_Y + valore_Z

if somma % 2 == 0 and valore_X % 3 == 0 and valore_Y % 5 == 0 and valore_Z % 7 == 0:
    print("Regole rispettate")

else: 
    print("Regole non rispettate")
