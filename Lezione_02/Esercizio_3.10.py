#Every Function
cities_list:list = ["Rome", "New York", "Firenze", "Budapest", "Capo Verde", "Valdivia", "Pamplona"]
print(cities_list)

#pop, append, extend, insert, remove
cities_list_pop = cities_list.pop(0)
print(cities_list)

cities_list_append = cities_list.append("Bangkok")
print(cities_list)

cities_list_extend = cities_list.extend(["Berlino", "Madrid", "Santiago"])
print(cities_list)

cities_list_insert = cities_list.insert(1, "Puntarenas")
print(cities_list)

cities_list_remove = cities_list.remove("Firenze")
print(cities_list)

#sorted (si crea una lista nuova partendo dalla lista originale)
new_cities_list = sorted(cities_list)
print(new_cities_list)

new_cities_list_reverse = sorted(cities_list, reverse = True)
print(new_cities_list_reverse)

#sort (modifica la lista originale e la mette in ordine)
new_cities_list_2 = cities_list[:]
new_cities_list_2.sort()
print(new_cities_list_2)

#reverse (modifica la lista originale e non la ordine)
new_cities_list_3 = cities_list[:]
new_cities_list_3.reverse()
print(new_cities_list_3)
