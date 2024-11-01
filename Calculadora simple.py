#Escriba un programa que pida al usuario que ingrese 
# dos números y luego imprima la suma, la resta, 
# la multiplicación y la división de esos números.

# Pedimos al usuario que ingrese un número y luego otro número
# Se utilizan las variables "numero1" y "numero2"
# La función "imput" permite solicitar información al usuario
# Se utiliza la función "int" para que el valor ingresado se convierte en un número entero
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

#Se definen las variables para las diferentes operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

#Resultados de las operaciones
#Cada resultado hace referencia a una variable diferente
print (f"La suma es: ", suma) 
print (f"La resta es: ", resta) 
print (f"La multiplicación es: ", multiplicacion)
print (f"La división es: ", division)


