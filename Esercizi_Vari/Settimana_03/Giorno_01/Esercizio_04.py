'''
Tema: Liste di dizionari → Dizionari di liste
Obiettivo: Riorganizzare dati categorizzati
'''

# Esercizio 04
# Titolo: "Raggruppa per categoria"

'''
Traccia:
Hai una lista di dizionari in cui ogni dizionario rappresenta un prodotto con nome e categoria.
Scrivi una funzione che restituisca un dizionario di liste, dove ogni chiave è una categoria e 
il valore associato è una lista con i nomi dei prodotti appartenenti a quella categoria.

Suggerimento:
Controlla se la categoria esiste già nel dizionario: se non c’è, crea una nuova lista. 
Se esiste, aggiungi semplicemente il nome del prodotto.

prodotti = [
    {"nome": "Mela", "categoria": "Frutta"},
    {"nome": "Carota", "categoria": "Verdura"},
    {"nome": "Banana", "categoria": "Frutta"},
    {"nome": "Zucchina", "categoria": "Verdura"},
    {"nome": "Biscotti", "categoria": "Dolci"}
]

Output atteso:
{
    "Frutta": ["Mela", "Banana"],
    "Verdura": ["Carota", "Zucchina"],
    "Dolci": ["Biscotti"]
}
'''

def ragruppa_categoria(prodotti: list[dict]) -> dict[str, list[str]]:
    risultato = {}

    for elemento in prodotti:
        categoria = elemento["categoria"]
        nome = elemento["nome"]

        if categoria not in risultato:
            risultato[categoria] = []
        
        risultato[categoria].append(nome)
    
    return risultato

prodotti = [
    {"nome": "Mela", "categoria": "Frutta"},
    {"nome": "Carota", "categoria": "Verdura"},
    {"nome": "Banana", "categoria": "Frutta"},
    {"nome": "Zucchina", "categoria": "Verdura"},
    {"nome": "Biscotti", "categoria": "Dolci"}
]

print(ragruppa_categoria(prodotti))


