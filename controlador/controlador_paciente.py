# controlador/controlador_paciente.py

from modelo.paciente import Paciente, PacienteDB

class ControladorPaciente:
    def __init__(self):
        self.modelo = PacienteDB()
        
    def agregar_paciente(self, nombre, fecha_nacimiento, correo, telefono):
        paciente = Paciente(None, nombre, fecha_nacimiento, correo, telefono)
        self.modelo.insertar(paciente)
        return "Paciente agregado con éxito"

    def actualizar_paciente(self, paciente_id, nombre, fecha_nacimiento, correo, telefono):
        paciente = Paciente(paciente_id, nombre, fecha_nacimiento, correo, telefono)
        self.modelo.actualizar(paciente)
        return "Paciente actualizado con éxito"

    def eliminar_paciente(self, paciente_id):
        self.modelo.eliminar(paciente_id)
        return "Paciente eliminado con éxito"

    def obtener_paciente(self, paciente_id):
        paciente = self.modelo.obtener(paciente_id)
        return paciente

    def obtener_todos_los_pacientes(self):
        pacientes = self.modelo.obtener_todos()
        return pacientes
