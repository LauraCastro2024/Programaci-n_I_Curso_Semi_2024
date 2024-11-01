import csv 

# Leemos el archivo CSV
with open('calificaciones.csv', 'r') as archivo_calificaciones:
    lector = csv.reader(archivo_calificaciones)
    next(lector)  # Saltamos la cabecera del archivo

    suma_total = 0
    contador = 0
    for fila in lector:
        suma_total += float(fila[1])  # Asumimos que la calificación está en la segunda columna
        contador += 1

# Calculamos el promedio
promedio = suma_total / contador if contador else 0
print("El promedio es: ",promedio)

# Escribimos el promedio de calificaciones en un nuevo archivo
with open('promedio_calificaciones.txt', 'w') as archivo_promedio:
    archivo_promedio.write(f"El promedio de las calificaciones es: {promedio}\n")