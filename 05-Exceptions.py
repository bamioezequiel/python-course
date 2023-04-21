try:
    division = 10/0
except:
    print("ERROR: No se puede dividir por 0")

try:
    division = 10/0
except ZeroDivisionError:
    print("ERROR: No se puede dividir por 0")