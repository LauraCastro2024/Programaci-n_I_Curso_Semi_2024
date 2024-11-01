# Pedimos al usuario que ingrese su peso
peso = input("Ingrese su peso en kilogramos: ")
peso = float(peso)

# Pedimos al usuario que ingrese su altura
altura = input("Ingrese su altura en metros: ")
altura = float(altura)

# Calculamos el IMC
imc = peso / altura**2

# Imprimimos el resultado
print(f"Su Indice de Masa Corporal es {imc:.2f}.")