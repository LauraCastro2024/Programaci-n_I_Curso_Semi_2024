import json
import os

# Definimos la función que calcula el promedio
def calcularPromedio(file):
    if not os.path.exists(file):
        return 0  # Retorna 0 si el archivo no existe

    with open(file, 'r') as archivo_calificaciones:
        estudiantes = json.load(archivo_calificaciones)

        suma_total = 0
        contador = 0
        for estudiante in estudiantes:
            suma_total += estudiante['calificacion']
            contador += 1

    # Calculamos el promedio
    promedio = suma_total / contador if contador != 0 else 0    
    return promedio

# Definimos la función que escribe el promedio en un nuevo archivo
def escribirPromedio(file, promedio):
    with open(file, 'w') as archivo_promedio:
        json.dump({"El promedio de las calificaciones es": promedio}, archivo_promedio)

# Definimos la función para agregar un estudiante y su calificación
def agregarEstudiante(file, estudiante, calificacion):
    # Cargar estudiantes existentes
    if os.path.exists(file):
        with open(file, 'r') as archivo_estudiante:
            estudiantes = json.load(archivo_estudiante)
    else:
        estudiantes = []  # Si no existe, inicializa una lista vacía

    # Agregar nuevo estudiante
    estudiantes.append({"nombre": estudiante, "calificacion": calificacion})

    # Escribir de nuevo en el archivo
    with open(file, 'w') as archivo_estudiante:
        json.dump(estudiantes, archivo_estudiante, indent=4)

# Definir la función que crea el archivo JSON
def crearArchivo(file):
    if not os.path.exists(file):
        with open(file, 'w') as archivo_json:
            json.dump([], archivo_json)  # Inicializa con una lista vacía

if __name__ == '__main__':
    # Se crean las variables con el nombre de los ficheros
    file = 'calificaciones.json'
    file_promedio = 'promedio_calificaciones.json'

    # Crear el archivo JSON si no existe
    crearArchivo(file)

    # Calcular el promedio
    promedio = calcularPromedio(file)
    escribirPromedio(file_promedio, promedio)

    opcion = 'S' 
    while opcion == 'S':
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion = input("Calificacion del estudiante: ")
        calificacion = float(calificacion)

        agregarEstudiante(file, nombre, calificacion)

        opcion = input("¿Desea agregar otro estudiante? (S/N): ")
        opcion = opcion.upper()