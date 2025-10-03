'''
Conta quante sono invocando `count_even(nums)`, 
che restituisce quante voci della lista sono **pari** (incluso `0`).
'''

def count_even(nums: list[int]) -> int:
    return sum(1 for num in nums if num % 2 == 0)



nums = [1, 5, 4, 8, 9, 0]
print(count_even(nums))