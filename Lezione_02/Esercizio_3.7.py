dinner_guest = ['Lisa', 'Marco Aurelio', 'Leonardo', 'Dante', 'Homer Simpson', 'Michelangelo']

print(f"Carissimi {dinner_guest}, purtroppo per cena dovrò invitare soltanto due di voi")

remove_guest_1 = dinner_guest.pop()
print(f"Caro {remove_guest_1} purtroppo non sei stato invitato a cena, alla prossima ;)!")

remove_guest_2 = dinner_guest.pop()
print(f"Caro {remove_guest_2} purtroppo non sei stato invitato a cena, alla prossima ;)!")

remove_guest_3 = dinner_guest.pop()
print(f"Caro {remove_guest_3} purtroppo non sei stato invitato a cena, alla prossima ;)!")

remove_guest_4 = dinner_guest.pop(1)
print(f"Caro {remove_guest_4} purtroppo non sei stato invitato a cena, alla prossima ;)!")

print(f"Carissimi {dinner_guest} siete stati invitati a cena, vi aspetto!")
print(f"{dinner_guest[0]} ci vediamo a cena!")
print(f"{dinner_guest[1]} ci vediamo a cena!")

# for guest in dinner_guest:
#     print(f"{guest} ci vediamo a cena!")



