# Entrada de los tres números distintos
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Clasificar los números en orden ascendente
if num1 < num2 < num3:
    print("Los números en orden ascendente son:", num1, num2, num3)
elif num1 < num3 < num2:
    print("Los números en orden ascendente son:", num1, num3, num2)
elif num2 < num1 < num3:
    print("Los números en orden ascendente son:", num2, num1, num3)
elif num2 < num3 < num1:
    print("Los números en orden ascendente son:", num2, num3, num1)
elif num3 < num1 < num2:
    print("Los números en orden ascendente son:", num3, num1, num2)
else:
    print("Los números en orden ascendente son:", num3, num2, num1)