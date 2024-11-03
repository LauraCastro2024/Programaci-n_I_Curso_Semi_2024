import numpy as np

class GrafoDirigido:
    def __init__(self):
        # Inicializamos una lista para los nodos y una matriz de adyacencia vacía
        self.nodos = []
        self.matriz_adyacencia = np.zeros((0, 0))
    
    def agregar_nodo(self, nodo):
        # Solo agregamos el nodo si no está ya en la lista
        if nodo not in self.nodos:
            self.nodos.append(nodo)
            # Aumentamos el tamaño de la matriz de adyacencia
            n = len(self.nodos)
            nueva_matriz = np.zeros((n, n))  # Creamos una nueva matriz de ceros
            nueva_matriz[:n-1, :n-1] = self.matriz_adyacencia  # Copiamos la antigua matriz
            self.matriz_adyacencia = nueva_matriz  # Actualizamos la matriz

    def agregar_arista(self, origen, destino, peso):
        # Verificamos que ambos nodos existan
        if origen in self.nodos and destino in self.nodos:
            # Encontramos los índices de origen y destino
            indice_origen = self.nodos.index(origen)
            indice_destino = self.nodos.index(destino)
            # Agregamos el peso a la matriz de adyacencia
            self.matriz_adyacencia[indice_origen][indice_destino] = peso
        else:
            raise ValueError("Uno o ambos nodos no existen en el grafo.")
    
    def mostrar_matriz(self):
        # Mostramos la matriz de adyacencia
        print("Matriz de adyacencia:")
        print(self.matriz_adyacencia)
    
    def dijkstra(self, nodo_inicio):
        # Verificamos que el nodo de inicio exista
        if nodo_inicio not in self.nodos:
            raise ValueError("El nodo de inicio no existe en el grafo.")
        
        num_nodos = len(self.nodos)  # Número total de nodos en el grafo
        # Inicializamos distancias con infinito para todos los nodos
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[nodo_inicio] = 0  # La distancia al nodo de inicio es 0
        visitados = set()  # Conjunto para almacenar nodos visitados
        caminos = {nodo: [] for nodo in self.nodos}  # Para rastrear el camino
        caminos[nodo_inicio] = [nodo_inicio]  # El camino al nodo de inicio es él mismo
        
        # Mientras no hayamos visitado todos los nodos
        while len(visitados) < num_nodos:
            # Elegimos el nodo no visitado con la menor distancia
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), 
                              key=lambda nodo: distancias[nodo])
            visitados.add(nodo_actual)  # Marcamos el nodo actual como visitado
            
            # Recorremos todos los vecinos del nodo actual
            for i, peso in enumerate(self.matriz_adyacencia[self.nodos.index(nodo_actual)]):
                if peso > 0:  # Hay una arista
                    nodo_vecino = self.nodos[i]
                    nueva_distancia = distancias[nodo_actual] + peso  # Calculamos nueva distancia
                    # Si encontramos un camino más corto
                    if nueva_distancia < distancias[nodo_vecino]:
                        distancias[nodo_vecino] = float(nueva_distancia)  # Convertimos a float nativo
                        caminos[nodo_vecino] = caminos[nodo_actual] + [nodo_vecino]  # Actualizamos el camino
        
        return distancias, caminos

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un grafo dirigido
    grafo = GrafoDirigido()
    # Agregamos nodos
    grafo.agregar_nodo('A')
    grafo.agregar_nodo('B')
    grafo.agregar_nodo('C')
    # Agregamos aristas con pesos
    grafo.agregar_arista('A', 'B', 1)
    grafo.agregar_arista('A', 'C', 4)
    grafo.agregar_arista('B', 'C', 2)
    
    # Mostramos la matriz de adyacencia
    grafo.mostrar_matriz()
    
    # Ejecutamos el algoritmo de Dijkstra desde el nodo 'A'
    distancias, caminos = grafo.dijkstra('A')
    
    # Mostramos cada camino y su coste desde el nodo de inicio
    for nodo, costo in distancias.items():
        if costo < float('inf'):  # Si el nodo es alcanzable
            print(f"El camino más corto de A a {nodo} es {caminos[nodo]} con un coste de {costo}")
        else:
            print(f"No hay camino desde A hasta {nodo}")

