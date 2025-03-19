# Esercizio 7
'''Libro preferito: scrivi una funzione chiamata favorite_book() che accetti un parametro, title. 
La funzione dovrebbe stampare un messaggio, come "Uno dei miei libri preferiti è Alice nel paese delle meraviglie". 
Chiama la funzione, assicurandoti di includere un titolo di libro come argomento nella chiamata di funzione.'''

def favorite_book(title:str):
    print(f"Uno dei miei libri preferiti è \"{title}\"")

favorite_book("Niebla")
