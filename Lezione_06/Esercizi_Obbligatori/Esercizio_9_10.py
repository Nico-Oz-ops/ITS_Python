# Esercizio 9.10
'''
Restaurant importato: utilizzando la tua ultima classe Restaurant, memorizzala in un modulo. 
Crea un file separato che importi Restaurant. Crea un'istanza di Restaurant e chiama uno dei 
metodi di Restaurant per mostrare che l'istruzione import funziona correttamente.
'''
from Esercizio_9_1 import Ristorante

rest_2 = Ristorante("Nicolino Salchichòn", "cileno")
rest_2.describe_restaurant()

rest_3 = Ristorante("La Puzzona Mangia Bene", "americana")
rest_3.describe_restaurant()