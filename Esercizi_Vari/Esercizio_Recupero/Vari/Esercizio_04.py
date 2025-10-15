def calculate_std_dev(nums: list[float]) -> float:
    if len(nums) == 0:
        raise ValueError("lista vuota")
    
    # Calcolo della media
    total = 0.0
    for num in nums:
        total += num
    mean = total / len(nums)

    # Calcolo della varianza
    squared_diffs_sum = 0.0
    for num in nums:
        diff = num - mean
        squared_diffs_sum += diff * diff
    varianza = squared_diffs_sum / len(nums)

    return varianza ** 0.5 

numeri = [1.2, 5.4, 2.3, 5.0, 4.4, 2.52]
print(calculate_std_dev(numeri))