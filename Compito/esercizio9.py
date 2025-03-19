# Prima Soglia (pi = 3.14)

pi_app = 0 # numero pi approssimato.
termine = 1 # termine che è uguale al denominatore, inizia con 1.
segno = 1 # inizia con un segno positivo, poiché il primo termine della serie è positivo, ma poi viene invertito per alternare i segni + e - della serie.
count = 0

while True:
    pi_app += segno * 4 / termine
    segno *= -1 
    termine += 2 
    count += 1

    differenza = pi_app - 3.14 # stanza tra pi approssimato e la soglia desiderata.
    if -0.01 < differenza < 0.01: # si verifica se l'approssimazione di pi ha ragiunto la soglia desiderata. 
        print(f"Per ottenere il valore di pi = 3.14, sono necessari usare \"{count}\" termini della serie")
        break # se la condizione è vera, allora pi_app è vicino alla soglia e il ciclo si interrompe.

# Seconda Soglia (pi = 3.141)
while True:
    pi_app += segno * 4 / termine
    segno *= -1 
    termine += 2 
    count += 1

    differenza = pi_app - 3.141 
    if -0.001 < differenza < 0.001: 
        print(f"Per ottenere il valore di pi = 3.141, sono necessari usare \"{count}\" termini della serie")
        break

# Terza Soglia (pi = 3.1415)
while True:
    pi_app += segno * 4 / termine
    segno *= -1 
    termine += 2 
    count += 1

    differenza = pi_app - 3.1415 
    if -0.0001 < differenza < 0.0001: 
        print(f"Per ottenere il valore di pi = 3.1415, sono necessari usare \"{count}\" termini della serie")
        break

# Quarta Soglia (pi = 3.14159)
while True:
    pi_app += segno * 4 / termine
    segno *= -1 
    termine += 2 
    count += 1

    differenza = pi_app - 3.14159 
    if -0.00001 < differenza < 0.00001: 
        print(f"Per ottenere il valore di pi = 3.14159, sono necessari usare \"{count}\" termini della serie")
        break