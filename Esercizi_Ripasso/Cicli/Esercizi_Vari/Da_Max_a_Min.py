'''
Scrivere una funzione in cui si possa ordinare una lista di numeri dal più grande al più piccolo,
e anche al contrario (dal più piccolo al più grande).
'''

def ordernar_lista(lista: list[float], reverse=False) -> list[float]:
    lista_ordenada = lista.copy() # creo una copia de la lista original

    for i in range(len(lista_ordenada)):
        indice_seleccionado = i # indice del elemento a comparar

        for j in range(i + 1, len(lista_ordenada)):
            if reverse: # orden descendente (de mayor a menor)
                if lista_ordenada[j] > lista_ordenada[indice_seleccionado]:
                    indice_seleccionado = j
            else: # orden ascendente (de menor a mayor)
                if lista_ordenada[j] < lista_ordenada[indice_seleccionado]:
                    indice_seleccionado = j
        
        # intercambio los elementos
        lista_ordenada[i], lista_ordenada[indice_seleccionado] = lista_ordenada[indice_seleccionado], lista_ordenada[i]
    
    return lista_ordenada

numeros = [1, 8, 79, 5.5, 45.21, 63, 71, 69]
print(f"Lista de numero de menor a mayor: {ordernar_lista(numeros)}")
print(f"Lista de numeros de mayor a menor: {ordernar_lista(numeros, reverse=True)}")

