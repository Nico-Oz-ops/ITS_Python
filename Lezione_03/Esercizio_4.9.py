list_comprehension_cube = [cube ** 3 for cube in range(1, 11)]
print(list_comprehension_cube)

print("-" * 76)




# dictionary comprehension
dict_list_comprehension_cube = {key: key ** 3 for key in range(1, 11)}
print(dict_list_comprehension_cube)