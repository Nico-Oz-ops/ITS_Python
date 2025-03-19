# Exercise 5: Crea una funzione interna per calcolare l'addizione nel modo seguente

def esterna(a, b):

    def addizione(a, b):
        somma = a + b
        return somma
    
    add = addizione(a, b)
    return add + 5

print(esterna(2, 5))