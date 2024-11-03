import numpy as np

class Grafo:
    def __init__(self):
        self.nodos = []  # Lista para almacenar los nodos
        self.matriz_adyacencia = np.zeros((0, 0))  # Matriz de adyacencia inicializada como matriz vacía

    def agregar_nodo(self, nodo):
        """Añadir un nuevo nodo al grafo."""
        if nodo not in self.nodos:
            self.nodos.append(nodo)
            # Aumentar la matriz de adyacencia
            n = len(self.nodos)
            nueva_matriz = np.zeros((n, n))
            nueva_matriz[:n-1, :n-1] = self.matriz_adyacencia  # Copiar la matriz anterior
            self.matriz_adyacencia = nueva_matriz

    def agregar_arista(self, origen, destino, peso=1):
        """Definir la conexión entre los nodos en la matriz de adyacencia."""
        if origen in self.nodos and destino in self.nodos:
            indice_origen = self.nodos.index(origen)
            indice_destino = self.nodos.index(destino)
            self.matriz_adyacencia[indice_origen][indice_destino] = peso  # Establecer el peso de la arista

    def mostrar_matriz(self):
        """Visualizar la matriz que representa el grafo."""
        print("Matriz de Adyacencia:")
        print(" ", end="")
        for nodo in self.nodos:
            print(f"{nodo} ", end="")
        print()
        
        for i, fila in enumerate(self.matriz_adyacencia):
            print(f"{self.nodos[i]} ", end="")
            for valor in fila:
                print(f"{int(valor)} ", end="")
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

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_nodo("A")
    grafo.agregar_nodo("B")
    grafo.agregar_nodo("C")
    grafo.agregar_nodo("D")
    
    grafo.agregar_arista("A", "B", 1)
    grafo.agregar_arista("A", "C", 4)
    grafo.agregar_arista("B", "C", 2)
    grafo.agregar_arista("B", "D", 5)
    grafo.agregar_arista("C", "D", 1)
    
    grafo.mostrar_matriz()
    grafo.dijkstra("A")