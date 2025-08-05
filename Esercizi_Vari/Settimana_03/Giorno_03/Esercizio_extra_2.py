'''Ordina un dizionario per valore
dizionario può essere una roba tipo: 
dizionario: dict = {"a": 3, "b": 2, "c": 1}'''

# Ordinare secondo la chiave
def ordina_dizionario(random: dict[str, int]) -> dict[str, int]:
    return {k: random[k] for k in sorted(random)}

print(ordina_dizionario({"e": 4, "b": 11, "c": 8}))


# Ordinare secondo il valore, crescente
def ordina_dizionario_cres(d: dict[str, int]) -> dict[str, int]:
    return dict(sorted(d.items(), key = lambda valore: valore[1]))

print(ordina_dizionario_cres({"a": 3, "b": 5, "c": 1}))

# Ordinare secondo il valore, decrescente
def ordina_dizionario_desc(d: dict[str, int]) -> dict[str, int]:
    return dict(sorted(d.items(), key=lambda valore: valore[1], reverse=True))

print(ordina_dizionario_desc({"a": 3, "b": 5, "c": 1}))



# Uso di bubble sort
def ordina_per_valore(d: dict[str, int]) -> dict[str, int]:
    # Step 1: Ottenere gli item come lista di tuple (chiave, valore)
    items = list(d.items())

    # Step 2: Ordinare la lista manualmente (es: bubble sort)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:  # confronto tra valori
                # scambia
                items[j], items[j + 1] = items[j + 1], items[j]

    # Step 3: Ricostruire il dizionario
    risultato = {}
    for k, v in items:
        risultato[k] = v

    return risultato

d = {"c": 8, "a": 3, "b": 4}
print(ordina_per_valore(d)) 


