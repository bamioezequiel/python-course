"""
  Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
  Ejemplos:
  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

import math

def is_prime(number: int):
  if number < 2 or (is_even(number) and number != 2):
    return False

  for i in range(3, int(math.sqrt(number))+1, 2):
    if number % i == 0:
      return False

  return True

def is_even(number: int):
  return number % 2 == 0

def is_fibonacci(number: int):
  a = 0
  b = 1

  for i in range(number+1):
    aux = a
    a = b
    b = aux + b

  return a == number

number = int(input("Enter a number: "))

menssage_is_prime = "is prime" if is_prime(number) else "is not prime"
menssage_is_even = "is even" if is_even(number) else "is odd"
menssage_is_fibonacci = "is fibonacci" if is_fibonacci(number) else "is not fibonacci"

print(f"""
  {number} {menssage_is_prime}, {menssage_is_fibonacci} and {menssage_is_even}
""")