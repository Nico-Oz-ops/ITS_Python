# Esercizio 2

def calcola_stipendio(ore_lavorate:int) -> float:
    paga_oraria = 10
    paga_straordinaria = 1.5 * paga_oraria

    if ore_lavorate <= 40:
        return ore_lavorate * paga_oraria
    
    elif ore_lavorate > 40:
        ore_straordinarie = ore_lavorate - 40
        return (40 * paga_oraria) + (ore_straordinarie * paga_straordinaria)

print(calcola_stipendio(40))
print(calcola_stipendio(0))
print(calcola_stipendio(45))
