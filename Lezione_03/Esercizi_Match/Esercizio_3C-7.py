testa = 0
croce = 0

for i in range(8):
    risultato = input(f"Inserire il risultato del lancio {i + 1} se t o T è testa e c o C è croce: ").lower()

    match risultato:
        case "t":
            testa += 1
        case "c":
            croce += 1
        case _:
            print("Input non valido, inserire t o T per testa e c o C per croce")
            break

totale = testa + croce
perc_testa = (testa / totale) * 100 if testa > 0 else 0
perc_croce = (croce / totale) * 100 if croce > 0 else 0

print(f"Ci sono {testa} testa, che corrispondono al {perc_testa:.2f}% del totale dei lanci")
print(f"Ci sono {croce} croce, che corrispondono al {perc_croce:.2f}% del totale dei lanci")