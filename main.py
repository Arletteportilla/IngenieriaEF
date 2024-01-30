from controlador.controlador_paciente import ControladorPaciente
from vista.vista_paciente import VistaPaciente

def main():
    controlador = ControladorPaciente()
    vista = VistaPaciente(controlador)
    vista.mainloop()

if __name__ == "__main__":
    main()
