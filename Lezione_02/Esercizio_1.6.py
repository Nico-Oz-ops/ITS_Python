# Inserire all'interno di un dizionario il menù di un ristorante

ITS_bakery_menù:dict = {
    "Pizza": 9.00,
    "Pasta": 10.50,
    "Zuppa": 7.00,
    "Hamburger": 15.50,
    "Cotoletta": 10.00,
    "Salmone": 20.20,
    "Patatine Fritte": 5.50,
    "Patate al forno": 5.50,
    "Verdura del giorno": 7.00,
    "Cheesecake": 6.00,
    "Tiramisù": 6.00,
    "Focaccia con Nutella": 6.00,
    "Coca Cola": 3.50,
    "Acqua": 1.50,
    "Vino": 5.00 
    }

ordine:dict = {
    "Zuppa": 7.00,
    "Salmone": 20.20,
    "Verdure del giorno": 7.00,
    "Tiramisù": 6.00,
    "Vino": 5.00
    } 

# zuppa_price:float = ordine["Zuppa"]
# salmone_price:float = ordine["Salmone"]
# verdure_price:float = ordine["Verdure del giorno"]
# tiramisù_price:float = ordine["Tiramisù"]
# vino_price:float = ordine["Vino"]

# ordine_total_price:float = zuppa_price + salmone_price + verdure_price + tiramisù_price + vino_price
# print(f"Il totale da pagare è:{ordine_total_price: .2f} euro")



totale_da_pagare:float = 0

totale_da_pagare += ordine["Zuppa"]
totale_da_pagare += ordine["Salmone"]
totale_da_pagare += ordine["Verdure del giorno"]
totale_da_pagare += ordine["Tiramisù"]
totale_da_pagare += ordine["Vino"]

print(f"Il totale da pagare è: {totale_da_pagare:.2f} euro")