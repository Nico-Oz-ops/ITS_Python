# Exercise 6: Display numbers divisible by 5

list_num = [10, 20, 33, 46, 55]

print(f"Della seguente lista {list_num}\ni numeri divisibili per 5 sono:")
for i in list_num:
    if i % 5 == 0:
        print(i)