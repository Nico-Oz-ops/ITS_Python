# 6 - Definire una funzione che ritorni un dizionario

def get_user(myname, myrole, myage) -> dict[str, str, int]:
    return{"name": myname, "role": myrole, "age": myage}

user = get_user("Nico", "admin", 36)

print(f"Utente: {user['name']}")
print(f"Ruolo: {user['role']}")
print(f"Età: {user['age']} anni")


