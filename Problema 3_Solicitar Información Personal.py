# Pedimos al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
# Pedimos al usuario que ingrese su apellido
apellido = input("Ingrese su apellido: ")
# Pedimos al usuario que ingrese su año de nacimiento
anio_nacimiento = input("Ingrese su año de nacimiento: ")
anio_nacimiento = int(anio_nacimiento)
# Pedimos al usuario que ingrese el año actual
anio_actual = input("Ingrese el año actual: ")
anio_actual = int(anio_actual)
# Calculamos la edad aproximada del usuario
edad = anio_actual - anio_nacimiento
# Imprimimos la información en un formato específico
print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad aproximada: {edad} años.")