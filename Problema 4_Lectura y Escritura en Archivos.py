## Problema 4: Lectura y Escritura en Archivos
#Supongamos que somos profesores y necesitamos procesar
#las calificaciones de nuestros alumnos. 
#Los datos se almacenan en un archivo CSV, y nuestro 
#trabajo es leer ese archivo, calcular el promedio 
#de las calificaciones y luego escribir ese promedio 
#en un nuevo archivo.
#input() y print() no son adecuados aquí porque estamos
#trabajando con archivos y no con entradas de usuario 
#o impresiones en la consola.

import csv

#Definimos la funcion que calcula el promedio
def calcularPromedio(file):
	# Leemos el archivo CSV
	with open(file, 'r') as archivo_calificaciones:
			lector = csv.reader(archivo_calificaciones)
			next(lector)  # Saltamos la cabecera del archivo

			suma_total = 0
			contador = 0
			for fila in lector:
					suma_total += float(fila[1])  # Asumimos que la calificación está en la segunda columna
					contador += 1 #contador = contador + 1

	# Calculamos el promedio
	promedio = suma_total / contador if contador != 0 else 0	
	print(f"El promedio es: {promedio:.2f}")
	return promedio

#Definimos la funcion que escribe el promedio en un nuevo archivo
def escribirPromedio(file, promedio):
	# Escribimos el promedio de calificaciones en un nuevo archivo
	with open(file, 'w') as archivo_promedio:
			archivo_promedio.write(f"El promedio de las calificaciones es: {promedio}\n")
		
# Definimos la funcion para agregar un estudiante y su promedio
def agregarEstudiante (file, estudiante, calificacion):
	with open(file, 'a+') as archivo_estudiante:
			archivo_estudiante.write(f"\n{estudiante}, {calificacion}")

	# Definir la funcion que crea el archivo CSV, con las cabeceras "Nombre, Calificacion"
def crearArchivo(file, campos):
	try:
		with open(file, 'x') as archivo_csv:
				archivo_csv.write(f"{campos}")
	except FileExistsError:
		pass

if __name__ == '__main__':
	# Se crean las variables con el nombre de los ficheros
	file = 'calificaciones.csv'
	file_promedio = 'promedio_calificaciones.txt'

	# Creo el archivo csv con los Campos "Nombre, Calificacion"
	campos = "Nombre, Calificacion"
	crearArchivo(file, campos)

	opcion = 'S' 
	while opcion =='S':

		nombre = input("Ingrese el nombre del estudiante: ")
		calificacion = input("Calificacion del estudiante: ")
		calificacion = float(calificacion)

		agregarEstudiante(file, nombre, calificacion)
		
		opcion = input("¿Desea agregar otro estudiante? (S/N): ")
		opcion = opcion.upper()
	
	#agregarEstudiante(file, "Ana", 4)
	
	promedio = calcularPromedio(file)
	escribirPromedio(file_promedio, promedio)