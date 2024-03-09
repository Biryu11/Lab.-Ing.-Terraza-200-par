class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = []

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido {pedido} agregado a la cola de pedidos")

    def procesar_pedido(self):
        if self.cola_pedidos:
            pedido = self.cola_pedidos.pop(0)
            print(f"Procesando pedido {pedido}")
        else:
            print("No hay pedidos para procesar")

    def mostrar_estado_cola(self):
        if self.cola_pedidos:
            print("Estado actual de la cola de pedidos:")
            for pedido in self.cola_pedidos:
                print(pedido)
        else:
            print("La cola de pedidos está vacía")

sistema_pedidos = SistemaGestionPedidos()

sistema_pedidos.agregar_pedido("Pedido 1")
sistema_pedidos.agregar_pedido("Pedido 2")
sistema_pedidos.agregar_pedido("Pedido 3")

sistema_pedidos.mostrar_estado_cola()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado_cola()
