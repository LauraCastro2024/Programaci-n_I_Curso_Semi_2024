#Pedir las calificaciones separadas por comas
calificaciones = input("Introduce las calificaciones separadas por comas: ")

# Convertir la entrada en una lista de calificaciones
calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Imprimir el promedio
print(f"El promedio de las calificaciones es: {promedio:.2f}")