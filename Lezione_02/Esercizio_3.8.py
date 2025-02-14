visit_location = ["Nuova Zelanda", "Cambogia", "Islandia", "Vietnam", "Thailandia"]
print(visit_location)

visit_location_in_order = sorted(visit_location)
print(visit_location_in_order)

ordinato_desc = sorted(visit_location_in_order, reverse = True)
print(ordinato_desc)

print(visit_location)
visit_location_copy = visit_location[:]
visit_location_copy.reverse()
print(visit_location_copy)

visit_location_copy_2 = visit_location_copy[:]
visit_location_copy_2.reverse()
print(visit_location_copy_2)

visit_location_copy_3 = visit_location[:]
visit_location_copy_3.sort()
print(visit_location_copy_3)

visit_location_copy_4 = visit_location_copy_3[:]
visit_location_copy_4.sort(reverse = True)
print(visit_location_copy_4)