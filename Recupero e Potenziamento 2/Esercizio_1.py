# Esercizio 1

'''
Un garage fa pagare una tariffa minima di 2.00 $ per parcheggiare fino a tre ore, più 0.50 $ all'ora per ogni ora 
o parte di essa oltre le tre ore. Il costo massimo per un dato periodo di 24 ore di parcheggio ammonta a 10.00 $. 
Supponete che nessuna macchina resti parcheggiata per più di 24 ore.
Elaborare un algoritmo che calcoli e stampi i costi del parcheggio per una data periodo di tempo.
Una volta elaborato l'algoritmo, scrivere in Python, una funzione calculateCharges che consenta di determinare 
il costo del parcheggio per un dato cliente.
 
Scrivere un codice Python che consenta di calcolare i costi del parcheggio per ciascuno dei tre clienti che 
ieri hanno parcheggiato le loro auto in questo garage.

Mostra, poi, i risultati in forma tabellare.
Il vostro output deve avere il seguente formato:

Car         Hours          Charge
 1          1.5            2.00 $
 2          4.0            2.50 $
 3          24.0           10.00 $
 TOTAL      29.5           14.50 $  
'''

def calculateCharges(ore_parcheggio: float) -> float:

    costo_parcheggio = 2
    tariffa_extra = 0.5


    if ore_parcheggio <= 3:
        return f"{costo_parcheggio}"
    
    elif ore_parcheggio > 3 and ore_parcheggio < 24:
        costo_parcheggio_2 = ((ore_parcheggio - 3) * tariffa_extra) + costo_parcheggio
        return costo_parcheggio_2
    
    elif ore_parcheggio == 24:
        costo_parcheggio = 10
        return costo_parcheggio
    
    else:
        return "Errore, numero di ore di parcheggio superiori al massimo stabilito"
    
veicoli = [("Vei_1", 1.5),("Vei_2", 4.0),("Vei_3", 24.0)]

print(f"{'Car':<10}{'Hours':<10}{'Charge':<10}")


costo_totale = 0
ore_totale = 0

for veicolo, ore in veicoli:
    costo = float(calculateCharges(ore))
    costo_totale += costo
    ore_totale += ore

    print(f"{veicolo:<10}{ore:<10}{costo:<10}")
    
print(f"{'TOTAL':<10}{ore_totale:<10}{costo_totale:<10}")



        
