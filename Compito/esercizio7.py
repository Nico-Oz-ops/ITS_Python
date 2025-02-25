n = int(input("Inserire la lunghezza delle liste: ")) #si inserisce la lunghezza della lista e viene convertito in un numero intero.

lista_a = [int(input(f"Inserire un valore intero \"A\"[{i}]: ")) for i in range(n)]
lista_b = [int(input(f"Inserire un valore intero \"B\"[{i}]: "))for i in range(n)]
lista_c = []

for i in range(len(lista_a)):
    lista_c.append(lista_a[i] + lista_b[n - 1 - i]) #ogni elemento lista_a[i] viene sommato con l'elemento opposto di lista_b, cioè lista_b[n - 1 - i]. 
                                                    #il valore risultante viene aggiunto a lista_c.
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C: {lista_c}")

