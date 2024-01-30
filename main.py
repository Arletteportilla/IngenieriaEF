# main.py
import tkinter as tk
from controlador.controlador_paciente import ControladorPaciente
from vista.vista_paciente import VistaPaciente

def main():
    root = tk.Tk()
    root.title("Gestión de Pacientes")
    controlador = ControladorPaciente()
    vista_paciente = VistaPaciente(root, controlador)
    vista_paciente.mainloop()

if __name__ == "__main__":
    controlador = ControladorPaciente()
    vista = VistaPaciente(controlador)
    vista.mainloop()
