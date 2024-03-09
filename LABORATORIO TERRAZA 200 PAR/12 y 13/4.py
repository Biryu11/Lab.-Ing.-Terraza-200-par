class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_completada(self, tarea):
        for t in self.tareas:
            if t["tarea"] == tarea:
                t["completada"] = True
                break

    def proxima_tarea_pendiente(self):
        for t in self.tareas:
            if not t["completada"]:
                return t["tarea"]
        return "No hay tareas pendientes"


sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Preparar informe")
sistema_tareas.agregar_tarea("Enviar correo electrónico")
sistema_tareas.marcar_completada("Enviar correo electrónico")
proxima_tarea = sistema_tareas.proxima_tarea_pendiente()
print(f"La próxima tarea pendiente es: {proxima_tarea}")
