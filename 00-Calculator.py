# Calculator: Make a calculator where basic mathematical operations must be performed

number_one = int(input("Enter a number one: "))
number_two = int(input("Enter a number two: "))

addition = number_one + number_two
subtraction = number_one - number_two
multiplication = number_one * number_two
division = number_one / number_two

result = f"""
    Sum: {addition}
    Subtraction: {subtraction} 
    Multiplication: {multiplication} 
    Division: {division} 
"""

print(result)