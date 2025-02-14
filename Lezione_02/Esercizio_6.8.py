dict_pet_1 = {
    "kind": "cane",
    "owner": "Jack"
}

dict_pet_2 = {
    "kind": "gatto",
    "owner": "Alice"
}

dict_pet_3 = {
    "kind": "pappagallo",
    "owner": "Davide"
}

list_pets = [dict_pet_1, dict_pet_2, dict_pet_3]

for pet in list_pets:
    print(f"Animale: {pet['kind']}\nPadrone: {pet['owner']}")