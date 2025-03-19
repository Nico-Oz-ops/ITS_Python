# Exercise 2: Print the Sum of a Current Number and a Previous number

previous_num = 0

for current_num in range(10):
    sum_num = current_num + previous_num
    print(f"Current Number: {current_num} Previous Number: {previous_num} Sum: {sum_num}")
    previous_num = current_num

