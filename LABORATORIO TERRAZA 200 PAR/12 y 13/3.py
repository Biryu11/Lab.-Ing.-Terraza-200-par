class BuscadorLaberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.visitado = set()
        self.cola = []

    def es_movimiento_valido(self, fila, columna):
        return 0 <= fila < len(self.laberinto) and 0 <= columna < len(self.laberinto[0]) and self.laberinto[fila][columna] == 1 and (fila, columna) not in self.visitado

    def encontrar_camino(self, inicio, destino):
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
        fila_inicio, columna_inicio = inicio
        fila_destino, columna_destino = destino
        self.cola.append((fila_inicio, columna_inicio, 0))  
        while self.cola:
            fila, columna, distancia = self.cola.pop(0)
            if fila == fila_destino and columna == columna_destino:
                return distancia 
            for movimiento in movimientos:
                nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
                if self.es_movimiento_valido(nueva_fila, nueva_columna):
                    self.visitado.add((nueva_fila, nueva_columna))
                    self.cola.append((nueva_fila, nueva_columna, distancia + 1))

        return -1 
    
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

buscador = BuscadorLaberinto(laberinto)
inicio = (0, 0)
destino = (4, 4)
distancia = buscador.encontrar_camino(inicio, destino)

if distancia != -1:
    print(f"La distancia más corta al destino es: {distancia}")
else:
    print("No se encontró un camino al destino")
