# Inicializar una lista vacía para almacenar las calificaciones ingresadas por el usuario
calificaciones = []

# Bucle para leer 5 calificaciones del usuario
for i in range(5):
    # Pedir al usuario que ingrese una calificación y convertirla a número decimal (float)
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    # Añadir la calificación ingresada a la lista "calificaciones"
    calificaciones.append(calificacion)

# Calcular la suma total de las calificaciones en la lista utilizando la función sum()
suma_calificaciones = sum(calificaciones)

# Calcular el promedio dividiendo la suma de las calificaciones entre la cantidad de calificaciones (5 en este caso)
promedio = suma_calificaciones / len(calificaciones)

# Mostrar el promedio calculado, con dos decimales de precisión
print(f"El promedio de las calificaciones es: {promedio:.2f}")