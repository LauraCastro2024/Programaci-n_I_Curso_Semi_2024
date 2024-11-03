import numpy as np

class Grafo:
    def __init__(self):
        self.nodos = []  # Lista para almacenar los nodos
        self.matriz_adyacencia = np.zeros((0, 0))  # Matriz de adyacencia inicializada como matriz vacía

    def agregar_nodos(self, nodos):
        """Añadir múltiples nodos al grafo."""
        for nodo in nodos:
            if nodo not in self.nodos:
                self.nodos.append(nodo)
                # Aumentar la matriz de adyacencia
                n = len(self.nodos)
                nueva_matriz = np.zeros((n, n))
                nueva_matriz[:n-1, :n-1] = self.matriz_adyacencia  # Copiar la matriz anterior
                self.matriz_adyacencia = nueva_matriz

    def agregar_aristas(self, aristas):
        """Definir múltiples conexiones entre los nodos en la matriz de adyacencia."""
        for origen, destino, peso in aristas:
            if origen in self.nodos and destino in self.nodos:
                indice_origen = self.nodos.index(origen)
                indice_destino = self.nodos.index(destino)
                self.matriz_adyacencia[indice_origen][indice_destino] = peso  # Establecer el peso de la arista

    def mostrar_matriz(self):
        """Visualizar la matriz que representa el grafo en formato de tabla cuadrada."""
        print("Matriz de Adyacencia:")
        print(" ", end=" ")
        for nodo in self.nodos:
            print(f"[{nodo}]", end=" ")
        print()
        
        for i, fila in enumerate(self.matriz_adyacencia):
            print(f"[{self.nodos[i]}]", end=" ")
            for valor in fila:
                print(f"[{int(valor)}]", end=" ")
            print()

    def dijkstra(self, nodo_inicio):
        """Implementar el algoritmo de Dijkstra para encontrar el camino más corto desde un nodo origen."""
        if nodo_inicio not in self.nodos:
            print("El nodo de inicio no está en el grafo.")
            return

        n = len(self.nodos)
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[nodo_inicio] = 0
        visitados = set()
        caminos = {nodo: [] for nodo in self.nodos}
        caminos[nodo_inicio] = [nodo_inicio]

        while len(visitados) < n:
            # Seleccionar el nodo no visitado con la distancia más corta
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), 
                              key=lambda nodo: distancias[nodo])

            visitados.add(nodo_actual)

            for i, peso in enumerate(self.matriz_adyacencia[self.nodos.index(nodo_actual)]):
                if peso > 0:  # Si hay una arista
                    nodo_vecino = self.nodos[i]
                    nueva_distancia = distancias[nodo_actual] + peso
                    if nueva_distancia < distancias[nodo_vecino]:
                        distancias[nodo_vecino] = nueva_distancia
                        caminos[nodo_vecino] = caminos[nodo_actual] + [nodo_vecino]

        # Mostrar resultados
        for nodo, distancia in distancias.items():
            if distancia < float('inf'):
                print(f"Distancia desde {nodo_inicio} a {nodo}: {distancia}, Camino: {' -> '.join(caminos[nodo])}")
            else:
                print(f"Distancia desde {nodo_inicio} a {nodo}: Infinito (no alcanzable)")

def main():
    grafo = Grafo()
    
    # Solicitar el ingreso de nodos
    nodos_input = input("Ingrese los nombres de los nodos separados por comas: ")
    nodos = [nodo.strip() for nodo in nodos_input.split(",")]
    grafo.agregar_nodos(nodos)
    
    # Solicitar el ingreso de aristas
    aristas_input = input("Ingrese las aristas en el formato 'origen,destino,peso' separados por comas: ")
    aristas = []
    for arista in aristas_input.split(","):
        # Limpiar espacios y dividir
        partes = arista.strip().split(",")
        if len(partes) == 3:  # Verificar que tenga 3 partes
            origen, destino, peso = partes
            aristas.append((origen.strip(), destino.strip(), float(peso.strip())))
        else:
            print(f"Saltando arista inválida: {arista}")
    
    grafo.agregar_aristas(aristas)

    while True:
        print ("\nMenú:")
        print("1. Mostrar matriz de adyacencia")
        print("2. Ejecutar Dijkstra")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            grafo.mostrar_matriz()
        
        elif opcion == '2':
            nodo_inicio = input("Ingrese el nodo de inicio para ejecutar Dijkstra: ")
            grafo.dijkstra(nodo_inicio)
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
