# modelo/paciente.py
import mysql.connector

class Paciente:
    def __init__(self, id, nombre, fecha_nacimiento, correo, telefono):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.telefono = telefono

class PacienteDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='12345678', host='localhost', database='miBaseDeDatos')
        self.cursor = self.conexion.cursor()

    def insertar(self, paciente):
        query = "INSERT INTO Paciente (nombre, fecha_nacimiento, correo, telefono) VALUES (%s, %s, %s, %s)"
        valores = (paciente.nombre, paciente.fecha_nacimiento, paciente.correo, paciente.telefono)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def actualizar(self, paciente):
        query = "UPDATE Paciente SET nombre=%s, fecha_nacimiento=%s, correo=%s, telefono=%s WHERE id=%s"
        valores = (paciente.nombre, paciente.fecha_nacimiento, paciente.correo, paciente.telefono, paciente.id)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def eliminar(self, paciente_id):
        query = "DELETE FROM Paciente WHERE id=%s"
        self.cursor.execute(query, (paciente_id,))
        self.conexion.commit()

    def obtener(self, paciente_id):
        query = "SELECT * FROM Paciente WHERE id=%s"
        self.cursor.execute(query, (paciente_id,))
        resultado = self.cursor.fetchone()
        if resultado:
            return Paciente(*resultado)
        return None

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM Paciente")
        resultados = self.cursor.fetchall()
        return [Paciente(*fila) for fila in resultados]

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
