# Esercizio 6
'''
Si supponga di voler calcolare l'ammontare del denaro depositato su un 
conto bancario ad interesse composto. Se m è la somma depositata sul conto, 
la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma 
presente sul conto dopo t mesi data una somma di partenza m.
'''

def compoundInterest(m:float, t:int) -> float:

    if t == 0:
        return round(m, 2)
    
    else:
        return round(float(1.005 * compoundInterest(m, t - 1)), 2)

print(f"La somma iniziale presente sul conto dopo 0 mesi, con un tasso di 0.5%: {compoundInterest(1000, 0)} euro")
print(f"La somma iniziale presente sul conto dopo 1 mesi, con un tasso di 0.5%: {compoundInterest(1000, 1)} euro")
print(f"La somma iniziale presente sul conto dopo 2 mesi, con un tasso di 0.5%: {compoundInterest(1000, 2)} euro")
print(f"La somma iniziale presente sul conto dopo 3 mesi, con un tasso di 0.5%: {compoundInterest(1000, 3)} euro")
print(f"La somma iniziale presente sul conto dopo 4 mesi, con un tasso di 0.5%: {compoundInterest(1000, 4)} euro")
