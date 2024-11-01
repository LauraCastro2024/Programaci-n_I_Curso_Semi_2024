import numpy as np
import math

class Grafo:
    def __init__(self):
        self.nodos = []
        self.matriz_adyacencia = np.zeros((0, 0))
    
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos.append(nodo)
            nuevo_tamano = len(self.nodos)
            nueva_matriz = np.zeros((nuevo_tamano, nuevo_tamano))
            nueva_matriz[:nuevo_tamano-1, :nuevo_tamano-1] = self.matriz_adyacencia
            self.matriz_adyacencia = nueva_matriz
    
    def agregar_arista(self, origen, destino, peso):
        if origen in self.nodos and destino in self.nodos:
            i = self.nodos.index(origen)
            j = self.nodos.index(destino)
            self.matriz_adyacencia[i][j] = peso
        else:
            raise ValueError("Origen o destino no están en el grafo.")
    
    def mostrar_matriz(self):
        print("Matriz de Adyacencia:")
        print(self.matriz_adyacencia)
    
    def dijkstra(self, inicio):
        if inicio not in self.nodos:
            raise ValueError("El nodo de inicio no está en el grafo.")
        
        num_nodos = len(self.nodos)
        distancias = {nodo: math.inf for nodo in self.nodos}
        distancias[inicio] = 0
        visitados = set()
        
        while len(visitados) < num_nodos:
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), 
                              key=lambda nodo: distancias[nodo])
            visitados.add(nodo_actual)
            
            for i, nodo_vecino in enumerate(self.nodos):
                if self.matriz_adyacencia[self.nodos.index(nodo_actual)][i] > 0:  # Si hay arista
                    peso_arista = self.matriz_adyacencia[self.nodos.index(nodo_actual)][i]
                    if distancias[nodo_actual] + peso_arista < distancias[nodo_vecino]:
                        distancias[nodo_vecino] = distancias[nodo_actual] + peso_arista
        
        return distancias

def main():
    grafo = Grafo()
    
    # Ingreso de nodos
    num_nodos = int(input("Ingrese el número de nodos: "))
    for _ in range(num_nodos):
        nodo = input("Ingrese el nombre del nodo: ")
        grafo.agregar_nodo(nodo)
    
    # Ingreso de aristas
    while True:
        agregar_arista = input("¿Desea agregar una arista? (s/n): ")
        if agregar_arista.lower() != 's':
            break
        origen = input("Ingrese el nodo de origen: ")
        destino = input("Ingrese el nodo de destino: ")
        peso = float(input("Ingrese el peso de la arista: "))
        try:
            grafo.agregar_arista(origen, destino, peso)
        except ValueError as e:
            print(e)
    
    # Mostrar matriz de adyacencia
    grafo.mostrar_matriz()
    
    # Calcular distancias usando Dijkstra
    nodo_inicio = input("Ingrese el nodo de inicio para calcular distancias: ")
    try:
        distancias = grafo.dijkstra(nodo_inicio)
        print("Distancias desde", nodo_inicio, ":", distancias)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()