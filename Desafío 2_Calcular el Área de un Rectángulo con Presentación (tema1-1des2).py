# Definir variables numéricas para el ancho y el largo del rectángulo
# Estas variables almacenan las medidas del rectángulo
ancho = 68
largo = 23

# Definir variables de tipo string con texto explicativo
# Se utiliza para dar una explicación sobre el propósito del programa
texto_explicativo = "Este programa calcula el área de un rectángulo."

# Calcular el área del rectángulo
# El área se calcula multiplicando el ancho por el largo
area_rectangulo = ancho * largo

# Presentación del resultado
# Se muestra primero el texto explicativo y luego los datos y el resultado del área
print(texto_explicativo)
print("Datos para calcular el área:")
print("Ancho:", str (ancho) + " cm") # Convertimos el valor del ancho a texto y lo mostramos con la unidad "cm"
print("Largo:", str (largo) + " cm")  # Convertimos el valor del largo a texto y lo mostramos con la unidad "cm"
print("El área se calcula multiplicando ancho * largo:")
print("El área del rectángulo es:", str (area_rectangulo) + " cm²") # Convertimos el área a texto y añadimos "cm²"