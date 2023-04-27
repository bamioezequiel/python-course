"""
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  Podrás configurar generar contraseñas con los siguientes parámetros:
  - Longitud: Entre 8 y 16.
  - Con o sin letras mayúsculas.
  - Con o sin números.
  - Con o sin símbolos.
  (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string
import random

def generate_password(length, capital_letter: bool, numbers: bool, symbols: bool):
    letters_lowercase =  list(string.ascii_lowercase)
    letters_uppercase =  list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)
    list_total = letters_lowercase
    password = ""
    i = 0

    if capital_letter:
        list_total += letters_uppercase 
    if numbers:
        list_total += digits 
    if symbols:
        list_total += punctuation 

    while i <= length:
        index_random = random.randint(0, len(list_total)-1)
        password += list_total[index_random]
        i += 1

    return password


while True:
    command = "Y"
    length = int(input("Enter the length of your password between 8 and 16: "))
    capital_letter = bool(int(input("Do you want uppercase letters? [1] Yes [0] No: ")))
    numbers = bool(int(input("Do you want numbers? [1] Yes [0] No: ")))
    symbols = bool(int(input("Do you want symbols? [1] Yes [0] No: ")))
    print(length, capital_letter, numbers, symbols)

    print(generate_password(length, capital_letter, numbers, symbols))
    
    command = input("\nDo you want to generate another? (Y/n): ")
    if command.lower() != "y":
        break
