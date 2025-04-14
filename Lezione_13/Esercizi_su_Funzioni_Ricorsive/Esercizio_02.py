# Esercizio 2
'''
Si supponga di voler calcolare l'ammontare del denaro depositato su 
un conto bancario ad interesse composto. Se m è la somma depositata sul conto, 
la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la 
somma presente sul conto dopo t mesi data una somma di partenza m.
'''

# opzione 1
def compoundInterest(m:float, t:int) -> float:

    if t == 0: # se "t" è 0, l'ammontare "m" è la somma iniziale
        return m
    
    else:
        return (1.005 * compoundInterest(m, t - 1)) # moltiplico "m" per 1.005 ad ogni chiamata ricorsiva


print(f"Se la somma di partenza è 1000£, dopo 3 mesi avrò ammontato :{compoundInterest(1000, 3):.2f}")
    

# opzione 2

def compoundInterest(m:float, t:int) -> float:
    # t <= 0, non è passato ancora un mese da quando ho depositasto il saldo m, quindi il saldo sarà "mn"
    if t <= 0:
        return round(m, 2)
    
    else:
        # se t = 1, è passato un mese, saldo sul conto sarà 1.005 * m. Se "m" è 1000, il saldo sarà 1000 * 1.005 = 1005
        # se t = 2, 1005 * 1.005 = 1010.03
        # se t = 3, 1010.03 * 1.005 = 1015.08

        return round(1.005 * compoundInterest(m, t - 1), 2)
    
print(compoundInterest(1000, 3))















