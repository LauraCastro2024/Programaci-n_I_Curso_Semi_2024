# Clase Grafo: Se desarrolla una clase que representa 
# un grafo dirigido, utilizando una matriz de adyacencia.
# La clase incluye los siguientes métodos:
 ## Añadir nuevos nodos al grafo.
 ## Definir las conexiones entre los nodos en la matriz de adyacencia.
 ## Visualizar la matriz que representa el grafo.
# Se implementa el algoritmo de Dijkstra dentro de la clase 
# para calcular el camino más corto desde un nodo origen a los demás nodos.
# La salida muestra el camino más corto y su coste.
# El usuario ingresa los nodos y aristas a través de la consola.

import numpy as np  # Importamos la biblioteca numpy para trabajar con matrices

class GrafoDirigido:  # Definimos una clase para el grafo dirigido
    def __init__(self):
        self.nodos = []  # Inicializamos una lista vacía para los nodos del grafo
        self.matriz_adyacencia = np.zeros((0, 0))  # Inicializamos una matriz de adyacencia vacía
    
    def agregar_nodo(self, nodo):
        # Método para agregar un nuevo nodo al grafo
        if nodo not in self.nodos:  # Solo agregamos el nodo si no está ya en la lista
            self.nodos.append(nodo)  # Agregamos el nuevo nodo a la lista de nodos
            n = len(self.nodos)  # Contamos el número total de nodos en la lista
            nueva_matriz = np.zeros((n, n))  # Creamos una nueva matriz de ceros de tamaño n x n
            nueva_matriz[:n-1, :n-1] = self.matriz_adyacencia  # Copiamos los valores de la antigua matriz a la nueva
            self.matriz_adyacencia = nueva_matriz  # Actualizamos la matriz de adyacencia con la nueva matriz

    def agregar_arista(self, origen, destino, peso):
        # Método para agregar una arista entre dos nodos
        if origen in self.nodos and destino in self.nodos:  # Verificamos que ambos nodos existan en la lista de nodos
            indice_origen = self.nodos.index(origen)  # Obtenemos el índice del nodo de origen
            indice_destino = self.nodos.index(destino)  # Obtenemos el índice del nodo de destino
            self.matriz_adyacencia[indice_origen][indice_destino] = peso  # Agregamos el peso a la matriz de adyacencia
        else:
            raise ValueError("Uno o ambos nodos no existen en el grafo.")  # Lanzamos un error si algún nodo no existe
    
    def mostrar_matriz(self):
        # Método para mostrar la matriz de adyacencia
        print("Matriz de adyacencia:")  # Mensaje que indica que se mostrará la matriz
        print(self.matriz_adyacencia)  # Imprimimos la matriz de adyacencia
    
    def dijkstra(self, nodo_inicio):
        # Método para ejecutar el algoritmo de Dijkstra desde un nodo de inicio
        if nodo_inicio not in self.nodos:  # Verificamos que el nodo de inicio exista
            raise ValueError("El nodo de inicio no existe en el grafo.")  # Lanzamos un error si no existe
        
        num_nodos = len(self.nodos)  # Obtenemos el número total de nodos en el grafo
        distancias = {nodo: float('inf') for nodo in self.nodos}  # Inicializamos distancias a infinito para todos los nodos
        distancias[nodo_inicio] = 0  # La distancia al nodo de inicio es 0
        visitados = set()  # Conjunto para almacenar nodos que ya hemos visitado
        caminos = {nodo: [] for nodo in self.nodos}  # Diccionario para rastrear el camino a cada nodo
        caminos[nodo_inicio] = [nodo_inicio]  # El camino al nodo de inicio es solo él mismo
        
        while len(visitados) < num_nodos:  # Mientras no hayamos visitado todos los nodos
            # Elegimos el nodo no visitado con la menor distancia
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), 
                              key=lambda nodo: distancias[nodo])  # Buscamos el nodo no visitado con la distancia más corta
            visitados.add(nodo_actual)  # Marcamos el nodo actual como visitado
            
            # Recorremos todos los vecinos del nodo actual
            for i, peso in enumerate(self.matriz_adyacencia[self.nodos.index(nodo_actual)]):  # Iteramos sobre los pesos de la fila correspondiente al nodo actual
                if peso > 0:  # Verificamos si hay una arista (peso mayor que 0)
                    nodo_vecino = self.nodos[i]  # Obtenemos el nodo vecino
                    nueva_distancia = distancias[nodo_actual] + peso  # Calculamos la nueva distancia al nodo vecino
                    # Si encontramos un camino más corto al nodo vecino
                    if nueva_distancia < distancias[nodo_vecino]:  # Comparamos la nueva distancia con la distancia conocida
                        distancias[nodo_vecino] = float(nueva_distancia)  # Actualizamos la distancia al nodo vecino
                        caminos[nodo_vecino] = caminos[nodo_actual] + [nodo_vecino]  # Actualizamos el camino al nodo vecino
        
        return distancias, caminos  # Devolvemos las distancias y los caminos encontrados

# Ejemplo de uso
if __name__ == "__main__":  # Este bloque solo se ejecuta si el script se ejecuta directamente
    grafo = GrafoDirigido()  # Creamos una instancia de la clase GrafoDirigido
    grafo.agregar_nodo('A')  # Agregamos el nodo 'A'
    grafo.agregar_nodo('B')  # Agregamos el nodo 'B'
    grafo.agregar_nodo('C')  # Agregamos el nodo 'C'
    grafo.agregar_arista('A', 'B', 30)  # Agregamos una arista de 'A' a 'B' con peso 30
    grafo.agregar_arista('A', 'C', 90)  # Agregamos una arista de 'A' a 'C' con peso 90
    grafo.agregar_arista('B', 'C', 72)  # Agregamos una arista de 'B' a 'C' con peso 72
    
    grafo.mostrar_matriz()  # Mostramos la matriz de adyacencia del grafo
    
    distancias, caminos = grafo.dijkstra('A')  # Ejecutamos el algoritmo de Dijkstra desde el nodo 'A'
    
    for nodo, coste in distancias.items():  # Iteramos sobre cada nodo y su costo desde el nodo de inicio
        if coste < float('inf'):  # Si el nodo es alcanzable
            print(f"El camino más corto de A a {nodo} es {caminos[nodo]} con un coste de {coste}")  # Mostramos el camino y su coste
        else:
            print(f"No hay camino desde A hasta {nodo}")  # Si no hay camino, mostramos un mensaje


