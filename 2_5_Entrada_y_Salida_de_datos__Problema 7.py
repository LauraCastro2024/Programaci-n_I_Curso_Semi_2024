import pandas as pd
import matplotlib.pyplot as plt #utiliza matplotlib para crear un histograma de las calificaciones

# Leemos el archivo CSV
df = pd.read_csv('calificaciones.csv')
# Calculamos el promedio
promedio = df['Calificacion'].mean() #mean() calcula la media aritmetica
print(f"El promedio de las calificaciones es: {promedio}")

# Definimos los bordes de los contenedores para que estén centrados en los números enteros
bins = [i - 0.5 for i in range(2, 12)] # Los contenedores estarán centrados en números de 1 a 10
# Creamos un histograma de las calificaciones
plt.hist(df['Calificacion'], bins=bins, edgecolor='black')
plt.title('Distribución de las Calificaciones')
plt.xlabel('Calificaciones')
plt.ylabel('Cantidad de Estudiantes')
plt.xticks(range(1, 11)) # Para que los números enteros aparezcan en el eje x
plt.show()