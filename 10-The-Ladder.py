"""
  Crea una función que dibuje una escalera según su número de escalones.
  - Si el número es positivo, será ascendente de izquiera a derecha.
  - Si el número es negativo, será descendente de izquiera a derecha.
  - Si el número es cero, se dibujarán dos guiones bajos (__).
  
  Ejemplo: 4
          _
        _|       
      _|
    _|
  _|
  
"""

def draw_ladder(number: int):
    str_ladder_asc = "_|" 
    str_ladder_des = "|_\n" 
    str_ladder_zero = "__"
    draw = ""
    space_des = 1
    space_asc = 2 * number

    if number == 0:
      return str_ladder_zero
    elif number > 0:
      for i in range(number):
        if i == 0:
          draw += (" " * (space_asc)) + "_\n"
          space_asc -= 2
        else:     
          draw += (" " * (space_asc)) + str_ladder_asc + "\n"
          space_asc -= 2
      return draw
    else:
      for i in range(abs(number)):
        if i == 0:
          draw += "_ " + "\n" + (" " * space_des)
          space_des += 2
        else:      
          draw += str_ladder_des + (" " * (space_des)) 
          space_des += 2
      return draw
    
print("==============================")
print(draw_ladder(4))
print("==============================")
print(draw_ladder(-4))
print("==============================")
print(draw_ladder(0))
print("==============================")