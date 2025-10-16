'''
Filtra e trasforma parole

Nome dell’esercizio: filter_and_reverse

Scrivi una funzione che:

* Prende in input una lista di stringhe words e una soglia intera min_len.
* Filtra solo le parole con lunghezza maggiore o uguale a min_len.
* Restituisce una nuova lista con le parole filtrate, invertite (cioè rovesciate carattere per carattere).

Esempio:
filter_and_reverse(["ciao", "ok", "python", "hi"], 3)
# ➜ ['oaic', 'nohtyp']
'''

def filter_and_reverse(words: list[str], min_len: int) -> list[str]:
    return [word[::-1] for word in words if len(word) >= min_len]

words = ["ciao", "ok", "python", "hi"]
min_len = 3

print(filter_and_reverse(words, min_len))


# Alternativa 2
def filter_and_reverse(words: list[str], min_len: int) -> list[str]:
    risultato = []
    for word in words:
        if len(word) >= min_len:
            inverted = ""
            for i in range(len(word)-1, -1, -1):
                inverted += word[i]
            risultato.append(inverted)
    return risultato