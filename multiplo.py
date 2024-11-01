# Función que determina si un número es múltiplo de otro
def es_multiplo (a, b):
    print a % b == 0

# Número dado
numero = int(input("Introduce un número: "))

# Verificar si el número es múltiplo de los números mencionados
print(f"¿Es {numero} múltiplo de 2? {'Sí' if es_multiplo(numero, 2) else 'No'}")

print(f"¿Es {numero} múltiplo de 3? { 'Sí' if es_multiplo(numero, 3) else 'No'}")

print(f"¿Es {numero} múltiplo de 5? {'Sí' if es_multiplo(numero, 5) else 'No'}")

print(f"¿Es {numero} múltiplo de 7? {'Sí' if es_multiplo(numero, 7) else 'No'}")

print(f"¿Es {numero} múltiplo de 9? {'Sí' if es_multiplo(numero, 9)  else 'No'}")

print(f"¿Es {numero} múltiplo de 10? {'Sí' if es_multiplo(numero, 10)  else 'No'}")

print(f"¿Es {numero} múltiplo de 11? {'Sí' if es_multiplo(numero, 11)  else 'No'}")
