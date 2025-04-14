def find_element(lst: list[int], element:int) -> bool:
    for item in lst:
        if item == element:
            return True
                
    return False

t_e = find_element([1, 8, 9, 4, 45], 45)
print(t_e)