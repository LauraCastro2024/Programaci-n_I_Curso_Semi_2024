# Definir es múltiplo
def es_multiplo(numero, divisor):
  if numero % divisor == 0:
    return True
  else:
    return False

# Número dado
numero = int(input("Ingrese un número: "))

# Verificar si el número es múltiplo de 2, 3, 5, 7, 9, 10, y 11
divisores = [2, 3, 5, 7, 9, 10, 11]

# Resultados
for divisor in divisores:
  if es_multiplo(numero, divisor):
    print(f"¿Es {numero} múltiplo de {divisor}? Sí")
  else:
    print(f"¿Es {numero} múltiplo de {divisor}? No")
