def area_triangulo(base, altura):
  """
  Calcula el área de un triángulo.


  Parámetros:
    base: La base del triángulo (un número real).
    altura: La altura del triángulo (un número real).


  Retorno:
    El área del triángulo (un número real).
  """


  if base <= 0:
    raise ValueError("La base debe ser un número positivo")
  if altura <= 0:
    raise ValueError("La altura debe ser un número positivo")


  area = (base * altura) / 2
  return area


# Leer la base y la altura del triángulo
base = float(input("Introduzca la base del triángulo: "))
altura = float(input("Introduzca la altura del triángulo: "))


# Calcular el área del triángulo
try:
  area = area_triangulo(base, altura)
except ValueError as error:
  print(error)
else:
  print(f"El área del triángulo es: {area}")
