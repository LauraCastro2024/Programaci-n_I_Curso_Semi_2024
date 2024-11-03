
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

import numpy as np
class GrafoDirigido:
    def __init__(self):
        self.nodos = []  # Iniciamos una lista para los nodos
        self.matriz_adyacencia = np.zeros((0, 0))  # Iniciamod una matriz de adyacencia vacía
    
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:  # Solo agregamos el nodo si no está ya en la lista
            self.nodos.append(nodo)  # Agregamos el nuevo nodo a la lista
            n = len(self.nodos)  # Obtenemos el tamaño actual de la lista de nodos
            nueva_matriz = np.zeros((n, n))  # Creamos una nueva matriz de ceros
            nueva_matriz[:n-1, :n-1] = self.matriz_adyacencia  # Copiamos la antigua matriz
            self.matriz_adyacencia = nueva_matriz  # Actualizamos la matriz

    def agregar_arista(self, origen, destino, peso):
        if origen in self.nodos and destino in self.nodos:  # Verificamos que ambos nodos existan
            indice_origen = self.nodos.index(origen)  # Encontramos el índice de origen
            indice_destino = self.nodos.index(destino)  # Encontramos el índice de destino
            self.matriz_adyacencia[indice_origen][indice_destino] = peso  # Agregamos el peso a la matriz de adyacencia
        else:
            raise ValueError("Uno o ambos nodos no existen en el grafo.")  # Da error si los nodos no existen
    
    def mostrar_matriz(self):
        print("Matriz de adyacencia:")  # Mostramos un encabezado
        print(self.matriz_adyacencia)  # Mostramos la matriz de adyacencia
    
    def dijkstra(self, nodo_inicio):
        if nodo_inicio not in self.nodos:  # Verificamos que el nodo de inicio exista
            raise ValueError("El nodo de inicio no existe en el grafo.")  # Da error si el nodo no existe
        
        num_nodos = len(self.nodos)  # Número total de nodos en el grafo
        distancias = {nodo: float('inf') for nodo in self.nodos}  # Iniciamos distancias con infinito
        distancias[nodo_inicio] = 0  # La distancia al nodo de inicio es 0
        visitados = set()  # Conjunto para almacenar nodos visitados
        caminos = {nodo: [] for nodo in self.nodos}  # Para rastrear el camino
        caminos[nodo_inicio] = [nodo_inicio]  # El camino al nodo de inicio es el mismo
        
        while len(visitados) < num_nodos:  # Mientras no hayamos visitado todos los nodos
            nodo_actual = min((nodo for nodo in self.nodos if nodo not in visitados), 
                              key=lambda nodo: distancias[nodo])  # Elegimos el nodo no visitado con la menor distancia
            visitados.add(nodo_actual)  # Marcamos el nodo actual como visitado
            
            for i, peso in enumerate(self.matriz_adyacencia[self.nodos.index(nodo_actual)]):  # Recorremos los vecinos
                if peso > 0:  # Si hay una arista
                    nodo_vecino = self.nodos[i]  # Obtenemos el nodo vecino
                    nueva_distancia = distancias[nodo_actual] + peso  # Calculamos nueva distancia
                    if nueva_distancia < distancias[nodo_vecino]:  # Si encontramos un camino más corto
                        distancias[nodo_vecino] = float(nueva_distancia)  # Actualizamos la distancia
                        caminos[nodo_vecino] = caminos[nodo_actual] + [nodo_vecino]  # Actualizamos el camino
        
        return distancias, caminos  # Devuelve las distancias y los caminos

# Ejemplo de uso
if __name__ == "__main__":
    grafo = GrafoDirigido()  # Creamos un grafo dirigido
    
    while True:
        nodo = input("Ingrese el nombre del nodo (o 'fin' para terminar): ")  # Ingreso de nodos
        if nodo.lower() == 'fin':  # Opción para terminar el ingreso
            break
        if nodo.strip() == "":  # Validación de entrada vacía
            print("Por favor, ingrese un nombre de nodo válido.")  # Mensaje de error
            continue
        grafo.agregar_nodo(nodo)  # Agregamos el nodo al grafo
    
    print("Ingrese las aristas en el formato 'origen destino peso' (o 'fin' para terminar):")  # Ingreso de aristas
    while True:
        entrada = input()  # Capturamos la entrada del usuario
        if entrada.lower() == 'fin':  # Opción para terminar el ingreso
            break
        try:
            origen, destino, peso_str = entrada.split()  # Dividimos la entrada en origen, destino y peso
            peso = float(peso_str)  # Convertimos el peso a float
            grafo.agregar_arista(origen, destino, peso)  # Agregamos la arista al grafo
        except ValueError:  # Capturamos errores de entrada
            print("Error en la entrada. Asegúrese de usar el formato 'origen destino peso'.")  # Mensaje de error
            continue
    
    grafo.mostrar_matriz()  # Mostramos la matriz de adyacencia
    
    nodo_inicio = input("Ingrese el nodo de inicio para Dijkstra: ")  # Ingreso del nodo de inicio
    try:
        distancias, caminos = grafo.dijkstra(nodo_inicio)  # Ejecutamos el algoritmo de Dijkstra
        
        for nodo, costo in distancias.items():  # Mostramos cada camino y su coste
            if costo < float('inf'):  # Si el nodo es alcanzable
                print(f"El camino más corto de {nodo_inicio} a {nodo} es {caminos[nodo]} con un coste de {costo}")  # Mensaje de resultado
            else:
                print(f"No hay camino desde {nodo_inicio} hasta {nodo}")  # Mensaje si no hay camino
    except ValueError as e:
        print(e)  # Imprimimos el mensaje de error


