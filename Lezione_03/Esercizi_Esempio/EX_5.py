# Match statement and conditions

# insert a number

n:int = int(input("Insert a number: "))

match n:
    # case n is positive and even number
    case n if n > 0 and n % 2 == 0:
        print(f"{n} is positive and even")
    
    # case n is positive and odd number
    case n if n > 0 and n % 2 != 0:
        print(f"{n} is positive and odd")
    
    # case n is negative and even number
    case n if n < 0 and n % 2 == 0:
        print(f"{n} is negative and even")
    
    # case n is negative and odd number
    case n if n < 0 and n % 2 != 0:
        print(f"{n} is negative and odd")