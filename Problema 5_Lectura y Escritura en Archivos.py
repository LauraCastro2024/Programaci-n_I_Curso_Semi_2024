import json

#Definimos la funcion que calcula el promedio
def calcularPromedio(file):
	# Leemos el archivo json
	with open(file, 'r') as archivo_calificaciones:
			estudiantes = json.load(archivo_calificaciones)

			suma_total = 0
			contador = 0
			for estudiante in estudiantes:
					suma_total += estudiante['calificacion']
					contador += 1

	# Calculamos el promedio
	promedio = suma_total / contador if contador != 0 else 0	
	print(f"El promedio es: {promedio:.2f}")
	return promedio

#Definimos la funcion que escribe el promedio en un nuevo archivo
def escribirPromedio(file, promedio):
	# Escribimos el promedio de calificaciones en un nuevo archivo
	with open(file, 'w') as archivo_promedio:
		json.dump({"El promedio de las calificaciones es": promedio}, archivo_promedio)

# Definimos la funcion para agregar un estudiante y su promedio
def agregarEstudiante (file, estudiante, calificacion):
	with open(file, 'a+') as archivo_estudiante:
			json.dump(f"\n{estudiante}, {calificacion}")

	# Definir la funcion que crea el archivo JSON, con las cabeceras "Nombre, Calificacion"
def crearArchivo(file, campos):
	try:
		with open(file, 'x') as archivo_json:
				archivo_json.dump(f"{campos}")
	except FileExistsError:
		pass

if __name__ == '__main__':
	# Se crean las variables con el nombre de los ficheros
	file = 'calificaciones.json'
	file_promedio = 'promedio_calificaciones.json'

	# Creo el archivo json con los Campos "Nombre, Calificacion"
	campos = "Nombre, Calificacion"
	# crearArchivo(file, campos)

	promedio = calcularPromedio(file)
	escribirPromedio(file_promedio, promedio)
 
	opcion = 'S' 
	while opcion =='S':

		nombre = input("Ingrese el nombre del estudiante: ")
		calificacion = input("Calificacion del estudiante: ")
		calificacion = float(calificacion)

		agregarEstudiante(file, nombre, calificacion)

		opcion = input("¿Desea agregar otro estudiante? (S/N): ")
		opcion = opcion.upper()

	#agregarEstudiante(file, "Ana", 4)