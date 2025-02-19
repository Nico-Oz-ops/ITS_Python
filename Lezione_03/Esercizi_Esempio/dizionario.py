my_dict:dict = {
    "Pizza":10.00,
    "Pasta":20.00,
    "Lasagna":30.00,
}

# I Modo - stampa chiave e valore
# print("Primo Modo:")
# for key, value in my_dict.items():
    # print(f"{key}: {value}")

# II Modo - stampa solo chiave
# print("Secondo Modo:")
# for key in my_dict:
    # print(my_dict[key])
    
# III Modo - stampa chiave e valore
# print("Terzo Modo:")
# for key in my_dict:
    # print(f"{key}: {my_dict[key]}")


# Uso di metodo .get()

# 1. Quando la chiave esiste
diz = {1: "a", 2: "b", 3: "c"}
print(diz.get(1))

# 2. Quando la chiave non esiste
diz = {1: "a", 2: "b", 3: "c"}
print(diz.get(4))

# 3. Quando la chiave non esiste e si passa un valore di default
diz = {1: "a", 2: "b", 3: "c"}
print(diz.get(4, "Chiave non esistente"))




