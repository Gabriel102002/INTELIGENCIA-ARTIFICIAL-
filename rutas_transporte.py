import heapq  # Se importa la biblioteca heapq para manejar una cola de prioridad

class SistemaTransporte:
    def __init__(self):
        # Inicializa un diccionario vacío para representar el grafo del sistema de transporte
        # Cada clave será una estación y su valor una lista de conexiones con costos
        self.grafo = {}

    def agregar_conexion(self, inicio, destino, costo):
        # Agrega una conexión entre dos estaciones con un costo asociado
        # Si la estación no existe en el grafo, se crea una lista vacía para sus conexiones
        if inicio not in self.grafo:
            self.grafo[inicio] = []
        if destino not in self.grafo:
            self.grafo[destino] = []

        # Se agrega la conexión en ambas direcciones (suponiendo que es bidireccional)
        self.grafo[inicio].append((destino, costo))
        self.grafo[destino].append((inicio, costo))

    def heuristica(self, nodo, objetivo):
        # Función heurística utilizada en el algoritmo A*.
        # En este caso, no se usa una heurística real (se devuelve 0)
        # Se podría mejorar con distancias reales entre estaciones
        return 0

    def a_estrella(self, inicio, objetivo):
        # Implementación del algoritmo A* para encontrar la mejor ruta entre dos estaciones
        # Se usa una cola de prioridad (heap) para explorar rutas con menor costo primero
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, inicio, []))  # Insertamos el punto de partida con costo 0
        visitados = set()  # Conjunto para almacenar los nodos ya explorados

        while cola_prioridad:  # Mientras haya rutas por explorar
            costo_actual, nodo_actual, ruta_actual = heapq.heappop(cola_prioridad)  # Extrae la ruta con menor costo

            if nodo_actual in visitados:
                continue  # Si el nodo ya fue visitado, lo saltamos para evitar ciclos

            ruta_actual = ruta_actual + [nodo_actual]  # Se agrega el nodo actual a la ruta recorrida
            visitados.add(nodo_actual)  # Se marca el nodo como visitado

            if nodo_actual == objetivo:  # Si llegamos al destino, devolvemos la mejor ruta encontrada
                return ruta_actual

            # Recorremos los vecinos del nodo actual
            for vecino, costo in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:  # Solo procesamos nodos no visitados
                    nuevo_costo = costo_actual + costo + self.heuristica(vecino, objetivo)  # Calculamos el nuevo costo
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino, ruta_actual))  # Agregamos la nueva ruta a la cola

        return None  # Si no se encuentra una ruta, se devuelve None

if __name__ == "__main__":
    # Crear instancia del sistema de transporte
    transporte = SistemaTransporte()

    # Agregar conexiones de estaciones
    transporte.agregar_conexion("A", "B", 1)
    transporte.agregar_conexion("A", "C", 4)
    transporte.agregar_conexion("B", "D", 2)
    transporte.agregar_conexion("C", "D", 1)
    transporte.agregar_conexion("D", "E", 3)

    while True:  # Bucle para repetir las pruebas
        # Solicitar entrada del usuario
        inicio = input("Ingrese el punto de inicio: ").strip().upper()
        destino = input("Ingrese el punto de destino: ").strip().upper()

        # Calcular la mejor ruta
        mejor_ruta = transporte.a_estrella(inicio, destino)

        if mejor_ruta:
            print("Mejor ruta encontrada:", mejor_ruta)
        else:
            print("No hay conexión entre los puntos seleccionados.")

        # Preguntar si se quiere realizar otra prueba
        repetir = input("¿Quieres realizar otra prueba? (sí/no): ").strip().lower()
        if repetir != 'sí':
            print("Gracias por usar el sistema de transporte.")
            break  # Salir del bucle si no se desea repetir la prueba
