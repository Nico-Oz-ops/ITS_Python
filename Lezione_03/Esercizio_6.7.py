my_dict = {
    "first_name": "Sebastiàn",
    "last_name": "Callegari",
    "age": 42,
    "city": "Barcellona"
}

my_dict_2 = {
    "first_name": "Lisa",
    "last_name": "Bandinelli",
    "age": 26,
    "city": "Roma"
}

my_dict_3 = {
    "first_name": "Ramón",
    "last_name": "Soto",
    "age": 121,
    "city": "Tokyo"
}

list_people = [my_dict, my_dict_2, my_dict_3]
# print(list_people)

# print(type(list_people))

# for key in list_people:
    # print(f"First Name: {my_dict['first_name']}\n Age: {my_dict['age']}\n City: {my_dict['city']}")


for key in list_people:
    print(f"Nome: {key['first_name']}\nCognome: {key['last_name']}\nEtà: {key['age']}\nCittà: {key['city']}")