my_dict:dict = {
    "Pizza":10.00,
    "Pasta":20.00,
    "Lasagna":30.00,
}

# I Modo - stampa chiave e valore
print("Primo Modo:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# II Modo - stampa solo chiave
print("Secondo Modo:")
for key in my_dict:
    print(my_dict[key])
    
# III Modo - stampa chiave e valore
print("Terzo Modo:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")