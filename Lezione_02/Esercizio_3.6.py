dinner_guest = ["Marco Aurelio", "Leonardo", "Homer Simpson"]
print(f"Ragazzi {dinner_guest}, a cena adesso saremo in 6")

new_guest_1 = dinner_guest.insert(0, "Lisa")
new_guest_2 = dinner_guest.insert(3, "Dante")
new_guest_3 = dinner_guest.append("Michelangelo")

print(f"Carissima {dinner_guest[0]}, sei stata invitata a cena venerdì sera!")
print(f"Carissimo {dinner_guest[1]}, sei stata invitato a cena venerdì sera!")
print(f"Carissimo {dinner_guest[2]}, sei stata invitato a cena venerdì sera!")
print(f"Carissimo {dinner_guest[3]}, sei stata invitato a cena venerdì sera!")
print(f"Carissimo {dinner_guest[4]}, sei stata invitato a cena venerdì sera!")
print(f"Carissimo {dinner_guest[5]}, sei stata invitato a cena venerdì sera!")

femmine: list = ["lisa", "francesca", "martina", "giorgia"]

for guest in dinner_guest:
    final = "a" if guest.lower() in femmine else "o"
    print(f"Carissim{final} {guest}, sei invitat{final} a cena venerdì sera!")

print(dinner_guest)