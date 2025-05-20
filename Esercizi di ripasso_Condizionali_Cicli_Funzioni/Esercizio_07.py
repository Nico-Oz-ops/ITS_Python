# Esercizio 7
'''
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso 
come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei 
secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, 
vengono considerate come orario di partenza, dunque, come uno zero).
Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero 
sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.
Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, 
entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare 
la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, 
entrambi contenuti entro un ciclo dell'orologio di 12 ore.
Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
'''

def seconds_since_noon(ore:int, minuti:int, secondi:int) -> int:
    '''
    ora = 60 minuti
    minuto = 60 secondi
    facendo il totale dei secondi dalle 00:00:00 (mezzanotte, è più ottimale farlo a partire 
    dalle 00:00:00 piutttosto che dalle 12:00:00)

    secondi totali = (ora - 0) x (60 x 60) + (minuto x 60) + secondi

    ad esempio: se l'ora fosse 3:15:50...
                secondi_totali = (3 - 0) * 3600 + (15 * 60) + 50
                secondi_totali = 10800 + 900 + 50 = 11750
    '''

    return ore * 3600 + (minuti * 60) + secondi


print(seconds_since_noon(3, 15, 50))


def time_difference(ora, minu, sec, ore, minuti, secondi):
    time1 = seconds_since_noon(ora, minu, sec)
    time2 = seconds_since_noon(ore, minuti, secondi)

    dif = abs(time1 - time2) # la funzione abs() rende assoluto un valore numerico, quindi non è necessario controllare + o -     

    return dif

print(time_difference(1, 0, 0, 3, 15, 30))


'''
def time_difference(ora, minu, sec, ore, minuti, secondi):
    time1 = ora * 3600 + (minu * 60) + sec
    time2 = seconds_since_noon(ore, minuti, secondi)

    dif = time1 - time2       

    if dif < 0:
        return dif * -1

    return dif
'''

