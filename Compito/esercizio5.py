N = int(input("Inserire la quantità di euro disponibili: "))

barrette = 0 # conta il numero totale di barrette ottenute
buono_sconto = 0 # conta i buoni sconti accumulati
euro_rimanente = N #tiene traccia dei soldi rimasti

while euro_rimanente >= 1: #il ciclo continua finché ha almeno 1 euro per comprare una barretta.

    euro_rimanente -= 1 #si spende 1 euro.
    barrette +=1 #si ottiene una barretta.
    buono_sconto += 1 #si guadagna un buono sconto
    
    if buono_sconto == 6: #se si accumulano 6 buoni sconto allora si ottiene una barretta gratis e si eliminano i 6 buoni sconto.
        barrette += 1
        buono_sconto -= 6

print(f"Il numero totale di barrette di cioccolato è: \"{barrette}\"")
print(f"I buoni sconto disponibili sono: \"{buono_sconto}\"")

