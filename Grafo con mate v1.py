import numpy as np
import math

class Grafo:
    def __init__(self):
        self.nodos = []
        self.matriz_adyacencia = np.zeros((0, 0))
    
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos.append(nodo)
            # Ampliar la matriz de adyacencia
            nueva_matriz = np.zeros((len(self.nodos), len(self.nodos)))
            nueva_matriz[:-1, :-1] = self.matriz_adyacencia
            self.matriz_adyacencia = nueva_matriz
    
    def agregar_arista(self, origen, destino, peso):
        if origen in self.nodos and destino in self.nodos:
            i = self.nodos.index(origen)
            j = self.nodos.index(destino)
            self.matriz_adyacencia[i][j] = peso
    
    def mostrar_matriz_adyacencia(self):
        print("Matriz de Adyacencia:")
        print(self.matriz_adyacencia)
    
    def dijkstra(self, inicio):
        if inicio not in self.nodos:
            return "El nodo de inicio no está en el grafo."
        
        distancias = {nodo: math.inf for nodo in self.nodos}
        distancias[inicio] = 0
        visitados = set()
        caminos = {nodo: [] for nodo in self.nodos}
        caminos[inicio] = [inicio]
        
        while len(visitados) < len(self.nodos):
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), key=lambda nodo: distancias[nodo])
            visitados.add(nodo_actual)
            
            for vecino in self.nodos:
                if self.matriz_adyacencia[self.nodos.index(nodo_actual)][self.nodos.index(vecino)] > 0:
                    peso = self.matriz_adyacencia[self.nodos.index(nodo_actual)][self.nodos.index(vecino)]
                    if distancias[nodo_actual] + peso < distancias[vecino]:
                        distancias[vecino] = distancias[nodo_actual] + peso
                        caminos[vecino] = caminos[nodo_actual] + [vecino]
        
        return distancias, caminos

def main():
    grafo = Grafo()
    
    # Solicitar número de nodos
    num_nodos = int(input("Ingrese el número de nodos: "))
    
    # Agregar nodos
    for i in range(num_nodos):
        nodo = input(f"Ingrese el nombre del nodo {i + 1}: ")
        grafo.agregar_nodo(nodo)
    
    # Solicitar número de aristas
    num_aristas = int(input("Ingrese el número de aristas: "))
    
    # Agregar aristas
    for i in range(num_aristas):
        origen = input(f"Ingrese el nodo de origen de la arista {i + 1}: ")
        destino = input(f"Ingrese el nodo de destino de la arista {i + 1}: ")
        peso = float(input(f"Ingrese el peso de la arista de {origen} a {destino}: "))
        grafo.agregar_arista(origen, destino, peso)
    
    # Mostrar la matriz de adyacencia
    grafo.mostrar_matriz_adyacencia()
    
    # Solicitar nodo de inicio para Dijkstra
    nodo_inicio = input("Ingrese el nodo de inicio para calcular el camino más corto: ")
    distancias, caminos = grafo.dijkstra(nodo_inicio)
    
    # Mostrar resultados
    print("Distancias desde", nodo_inicio, ":", distancias)
    print("Caminos más cortos:", caminos)

if __name__ == "__main__":
    main()