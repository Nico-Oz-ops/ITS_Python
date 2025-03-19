# Esercizio 17 - Sistema di gestione delle temperature

temp_max = -1000000000
giorno_max = 0
temp_min = 1000000000
giorno_min = 0
cont_temp_norma = 0
temp_media = 0
i = 1

while i <= 7:
    while True:
        temp = input(f"\nInserire la {i}° temperatura: °C")

        try:
            temp = float(temp)
            break
        
        except ValueError:
            print("\nErrore. Inserire un valore valido")

    temp_media += temp

    if temp > temp_max:
        temp_max = temp
        giorno_max = i

    else: 
        if temp < temp_min:
            temp_min = temp
            giorno_min = i
    
    if temp >= 10 and temp <= 30:
        cont_temp_norma += 1

        if cont_temp_norma <= 7:
            print("\n'Temperatura nella norma'")
    else:
        if temp < 5 or temp > 35:
            print("\n'Allerta temperatura!'")
    
    i += 1

temp_media = temp_media / 7

print(f"\nLa temperatura media è: {temp_media:.2f}°C")
print(f"\nIl {giorno_max}° giorno si è registrata la temperatura massima della settimana,\ncorrispondente a {temp_max}°C")
print(f"\nIl {giorno_min}° giorno si è registrata la temperatura minima della settimana,\ncorrispondente a {temp_min}°C")
        

