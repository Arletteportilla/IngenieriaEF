# vista/vista_paciente.py
import tkinter as tk
from tkinter import messagebox, simpledialog

class VistaPaciente(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Gestión de Pacientes")
        self.crear_widgets()

    def crear_widgets(self):
        # Entradas de texto y etiquetas
        tk.Label(self, text="Nombre:").grid(row=0, column=0)
        self.nombre = tk.Entry(self)
        self.nombre.grid(row=0, column=1)

        tk.Label(self, text="Fecha de Nacimiento (YYYY-MM-DD):").grid(row=1, column=0)
        self.fecha_nacimiento = tk.Entry(self)
        self.fecha_nacimiento.grid(row=1, column=1)

        tk.Label(self, text="Correo Electrónico:").grid(row=2, column=0)
        self.correo = tk.Entry(self)
        self.correo.grid(row=2, column=1)

        tk.Label(self, text="Teléfono:").grid(row=3, column=0)
        self.telefono = tk.Entry(self)
        self.telefono.grid(row=3, column=1)

        # Botones para CRUD
        tk.Button(self, text="Agregar", command=self.agregar_paciente).grid(row=4, column=0)
        tk.Button(self, text="Actualizar", command=self.actualizar_paciente).grid(row=4, column=1)
        tk.Button(self, text="Eliminar", command=self.eliminar_paciente).grid(row=5, column=0)
        tk.Button(self, text="Listar Todos", command=self.listar_pacientes).grid(row=5, column=1)

    def agregar_paciente(self):
        resultado = self.controlador.agregar_paciente(
            self.nombre.get(),
            self.fecha_nacimiento.get(),
            self.correo.get(),
            self.telefono.get()
        )
        messagebox.showinfo("Resultado", resultado)
        self.limpiar_campos()

    def actualizar_paciente(self):
        id_paciente = simpledialog.askstring("Actualizar Paciente", "Ingrese el ID del paciente:")
        if id_paciente:
            resultado = self.controlador.actualizar_paciente(
                id_paciente,
                self.nombre.get(),
                self.fecha_nacimiento.get(),
                self.correo.get(),
                self.telefono.get()
            )
            messagebox.showinfo("Resultado", resultado)
            self.limpiar_campos()

    def eliminar_paciente(self):
        id_paciente = simpledialog.askstring("Eliminar Paciente", "Ingrese el ID del paciente:")
        if id_paciente:
            resultado = self.controlador.eliminar_paciente(id_paciente)
            messagebox.showinfo("Resultado", resultado)

    def listar_pacientes(self):
        pacientes = self.controlador.obtener_todos_los_pacientes()
        lista_pacientes = "\n".join(f"{p.id} - {p.nombre}" for p in pacientes)
        messagebox.showinfo("Lista de Pacientes", lista_pacientes)

    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.fecha_nacimiento.delete(0, tk.END)
        self.correo.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
