# 6 - Definire una funzione che ritorni un dizionario

def get_user(myname, myrole) -> dict[str, str]:
    return{"name": myname, "role": myrole}

user = get_user("Nico", "el papi")

print(f"User: {user['name']}")
print(f"Role: {user['role']}")


