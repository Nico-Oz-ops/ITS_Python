# Esercizio 2. 
'''
Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi 
di una lista in ordine inverso.

Una volta elaborato il diagramma, appena consentitovi dal docente, scrivere una funzione 
ricorsiva in Python, chiamata printListBackward che stampi in output gli elementi di una 
lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver date le seguenti liste, stampi ogni lista in ordine 
inverso sfruttando la funzione ricorsiva printListBackward.

* lista1: 1, 2, 3, 4, 5

* lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"
''' 

def printListBackward(list_bw, indice = None):

    if not list_bw:
        print("Errore, lista vuota")
        return

    if indice is None:
        indice = len(list_bw) - 1
    
    if indice < 0:
        return
    
    print(list_bw[indice], end=", ")
    printListBackward(list_bw, indice - 1)

lista1 = [1, 2, 3, 4, 5]
lista3 = []
lista2 = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

printListBackward(lista1)
print("\n") 
printListBackward(lista2)
print("\n")
printListBackward(lista3)


#print(*lista1, sep=", ")





