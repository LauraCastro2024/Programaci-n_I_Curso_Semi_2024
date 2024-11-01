# Definimos la clase base Musico
class Musico:
    # Método que puede ser sobrescrito en las clases hijas
    def instrumento(self):
        return "Toca un instrumento"

# Definimos la clase Guitarrista que hereda de Musico
class Guitarrista(Musico):
    # Sobrescribimos el método instrumento para Guitarrista
    def instrumento(self):
        return "Toca la guitarra"

# Definimos la clase Baterista que hereda de Musico
class Baterista(Musico):
    # Sobrescribimos el método instrumento para Baterista
    def instrumento(self):
        return "Toca la batería"

# Creamos instancias de las clases
musico = Musico()           # Instancia de la clase base Musico
guitarrista = Guitarrista()  # Instancia de la clase Guitarrista
baterista = Baterista()      # Instancia de la clase Baterista

# Demostramos el polimorfismo
# Creamos una lista que contiene instancias de diferentes clases que heredan de Musico
musicos = [musico, guitarrista, baterista]

# Recorremos la lista y llamamos al método instrumento de cada instancia
# Cada objeto usa su propia versión del método gracias al polimorfismo
for m in musicos:
    print(m.instrumento())  # Se imprime el instrumento que toca cada músico según su clase