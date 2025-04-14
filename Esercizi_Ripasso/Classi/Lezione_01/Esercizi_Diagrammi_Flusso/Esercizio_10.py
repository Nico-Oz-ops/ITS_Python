# Esercizio 10 - Distribuzione di una borsa di studio

reddito_familiare = float(input("Inserire il reddito familiare: "))
media_voti = float(input("Inserire la media dei voti: "))

if reddito_familiare < 20000 and media_voti > 27:
    print("Borsa di studio approvata!")
else:
    print("Borsa di studio rifiutata")