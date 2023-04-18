command = -1
result = 0
while command != 0:
    number_one = int(input("Enter a number one: "))
    command = int(input("""
    [1] Sum
    [2] Subtraction
    [3] Multiplication
    [4] Division

    [0] Leave
    """))

    number_two = int(input("Enter a number two: "))
    
    if command == 1: 
        result = number_one + number_two
    elif command == 2:
        result = number_one - number_two
    elif command == 3:
        result = number_one * number_two
    else:
        result = number_one / number_two

    print(result)

    command = int(input("Do you want to continue? Yes [1] No [0]: "))
