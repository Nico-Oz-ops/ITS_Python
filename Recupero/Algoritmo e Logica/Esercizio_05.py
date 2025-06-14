# Esercizio 05
'''
Validazione di un Indirizzo IPv4

Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.

Requisiti:

● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.

● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].

Esempi:
is_valid_ipv4("192.168.0.1") # True
is_valid_ipv4("255.255.255.255") # True
is_valid_ipv4("256.100.10.1") # False (256 è fuori range)
is_valid_ipv4("192.168.1") # False (solo 3 parti)
is_valid_ipv4("192.168.1.a") # False (parte non numerica)
'''

def is_valid_ipv4(address: str) -> bool:

    parti = address.split(".") # dividere la stringa in base ai punti (.)

    if len(parti) != 4: # restituisce false se non ci sono quattro parti numeriche
        return False
    
    for parte in parti: # verificando ciascuna parte
        if not parte.isdigit(): # se la parte non contiene solo cifre allora restitusice False
            return False
        
        num = int(parte)
        if num < 0 or num > 255: # se non si trova nel range 0-255 allora ritorna False
            return False
    
    return True

print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("255.255.255.255")) 
print(is_valid_ipv4("256.100.10.1")) 
print(is_valid_ipv4("192.168.1"))
print(is_valid_ipv4("192.168.1.a"))


# versione del prof

def check(ip: str) -> bool:

    blocchi: list[str] = ip.split(".")

    if len(blocchi) != 4:
        return False
    
    for blocco in blocchi:

        if not blocco.isdigit():
            return False
        
        if not (0 <= int(blocco) <= 255):
            return False
        
    return True




        
    
