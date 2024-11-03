# Ejemplo de uso
if __name__ == "__main__":
    grafo = GrafoDirigido()  # Creamos un grafo dirigido

    # Agregar nodos de ejemplo
    nodos_de_prueba = ["A", "B", "C"]
    for nodo in nodos_de_prueba:
        grafo.agregar_nodo(nodo)

    # Agregar aristas de ejemplo
    aristas_de_prueba = [("A", "B", 1), ("B", "C", 2)]
    for origen, destino, peso in aristas_de_prueba:
        grafo.agregar_arista(origen, destino, peso)

    grafo.mostrar_matriz()  # Mostramos la matriz de adyacencia
    
    nodo_inicio = "A"  # Usamos un nodo de inicio predeterminado
    try:
        distancias, caminos = grafo.dijkstra(nodo_inicio)  # Ejecutamos el algoritmo de Dijkstra
        
        for nodo, costo in distancias.items():  # Mostramos cada camino y su coste
            if costo < float('inf'):  # Si el nodo es alcanzable
                print(f"El camino más corto de {nodo_inicio} a {nodo} es {caminos[nodo]} con un coste de {costo}")  # Mensaje de resultado
            else:
                print(f"No hay camino desde {nodo_inicio} hasta {nodo}")  # Mensaje si no hay camino
    except ValueError as e:
        print(e)  # Imprimimos el mensaje de error
