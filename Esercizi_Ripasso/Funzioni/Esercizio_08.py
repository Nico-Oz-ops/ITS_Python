# Esercizio 8
'''Maglietta: scrivi una funzione chiamata make_shirt() che accetti una taglia e 
il testo di un messaggio che dovrebbe essere stampato sulla maglietta. 
La funzione dovrebbe stampare una frase che riassuma la taglia della maglietta 
e il messaggio stampato su di essa. 
Chiama la funzione una volta usando argomenti posizionali per creare una maglietta. 
Chiama la funzione una seconda volta usando argomenti per parole chiave.'''

def make_shirt(taglia:str, frase:str):
    print(f"Il messaggio della maglietta, di taglia \"{taglia}\", dice: \"{frase}\".")

make_shirt("large", "Il Pitone mangia Python")
make_shirt(taglia="media", frase="El buena onda")


