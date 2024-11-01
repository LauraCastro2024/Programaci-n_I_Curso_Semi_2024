# Pedimos al usuario que ingrese la temperatura en grados Fahrenheit
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Convertimos la temperatura a grados Celsius
celsius = (fahrenheit - 32) * 5/9

# Imprimimos el resultado
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius:.2f} grados Celsius.")
