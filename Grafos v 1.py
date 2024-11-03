import numpy as np
import math

class Grafo:
    def __init__(self):
        self.ciudades = []
        self.matriz_adyacencia = np.zeros((0, 0))

    def agregar_ciudad(self, ciudad):
        """Agregar una nueva ciudad al grafo."""
        if ciudad not in self.ciudades:
            self.ciudades.append(ciudad)
            tamaño_actual = len(self.ciudades)
            nueva_matriz = np.zeros((tamaño_actual, tamaño_actual))
            nueva_matriz[:tamaño_actual-1, :tamaño_actual-1] = self.matriz_adyacencia
            self.matriz_adyacencia = nueva_matriz

    def agregar_arista(self, origen, destino, peso):
        """Definir una conexión entre ciudades en la matriz de adyacencia."""
        if origen in self.ciudades and destino in self.ciudades:
            i = self.ciudades.index(origen)
            j = self.ciudades.index(destino)
            self.matriz_adyacencia[i][j] = peso
            self.matriz_adyacencia[j][i] = peso  # Asumiendo que es un grafo no dirigido

    def mostrar_matriz_adyacencia(self):
        """Visualizar la matriz que representa el grafo."""
        print("Matriz de Adyacencia:")
        print(self.matriz_adyacencia)

    def dijkstra(self, ciudad_inicio):
        """Implementar el algoritmo de Dijkstra para encontrar el camino más corto."""
        if ciudad_inicio not in self.ciudades:
            raise ValueError("La ciudad de inicio no está en el grafo.")

        distancias = {ciudad: math.inf for ciudad in self.ciudades}
        distancias[ciudad_inicio] = 0
        visitados = set()
        caminos = {ciudad: [] for ciudad in self.ciudades}

        while len(visitados) < len(self.ciudades):
            ciudad_actual = min((ciudad for ciudad in self.ciudades if ciudad not in visitados), key=lambda ciudad: distancias[ciudad])
            visitados.add(ciudad_actual)

            for i, peso in enumerate(self.matriz_adyacencia[self.ciudades.index(ciudad_actual)]):
                if peso > 0 and self.ciudades[i] not in visitados:
                    nueva_distancia = distancias[ciudad_actual] + peso
                    if nueva_distancia < distancias[self.ciudades[i]]:
                        distancias[self.ciudades[i]] = nueva_distancia
                        caminos[self.ciudades[i]] = caminos[ciudad_actual] + [ciudad_actual]

        return distancias, {ciudad: caminos[ciudad] + [ciudad] for ciudad in self.ciudades}

if __name__ == "__main__":
    grafo = Grafo()

    # Agregar ciudades (nodos)
    for ciudad in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        grafo.agregar_ciudad(ciudad)

    # Agregar aristas (costos)
    grafo.agregar_arista('A', 'B', 30)
    grafo.agregar_arista('A', 'C', 90)
    grafo.agregar_arista('B', 'C', 72)
    grafo.agregar_arista('B', 'D', 30)
    grafo.agregar_arista('C', 'D', 48)
    grafo.agregar_arista('C', 'E', 120)
    grafo.agregar_arista('D', 'E', 100)
    grafo.agregar_arista('D', 'F', 150)
    grafo.agregar_arista('E', 'F', 180)
    grafo.agregar_arista('E', 'G', 60)
    grafo.agregar_arista('F', 'G', 150)

    # Mostrar matriz de adyacencia
    grafo.mostrar_matriz_adyacencia()

    # Calcular el camino más corto desde la ciudad 'A' a 'G'
    distancias, caminos = grafo.dijkstra('A')
    print("Distancias desde A:", distancias)
    print("Caminos desde A:", caminos)

    # Mostrar el costo mínimo para llegar a G
    costo_minimo = distancias['G']
    ruta_minima = caminos['G']
    print(f"Costo mínimo desde A hasta G: {costo_minimo}")
    print(f"Ruta mínima desde A hasta G: {' -> '.join(ruta_minima)}")