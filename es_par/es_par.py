def es_par(numero):
  """
  Determina si un número es par o impar.
  Parámetros:
    numero: Un número entero.
  Retorno:
    True si el número es par, False si es impar.
  """
  
  resto = numero % 2
  return resto == 0


# Leer un número
numero = int(input("Introduzca un número: "))


# Determinar si el número es par o impar
if es_par(numero):
  print("El número es par")
else:
  print("El número es impar")
