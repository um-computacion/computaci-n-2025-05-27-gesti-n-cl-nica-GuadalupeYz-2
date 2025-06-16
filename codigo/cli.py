from codigo.clinica import Clinica
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.especialidad import Especialidad
from codigo.excepciones import *
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Seleccione una opción: ")

            try:
                match opcion:
                    case "1": self.agregar_paciente()
                    case "2": self.agregar_medico()
                    case "3": self.agendar_turno()
                    case "4": self.agregar_especialidad_a_medico()
                    case "5": self.emitir_receta()
                    case "6": self.ver_historia_clinica()
                    case "7": self.ver_turnos()
                    case "8": self.ver_pacientes()
                    case "9": self.ver_medicos()
                    case "0": print("Saliendo..."); break
                    case _: print("Opción inválida.")
            except ValueError as ve:
                print(f" Error de datos: {ve}")
            except DatosInvalidosException as e:
                print(f" Datos inválidos: {e}")
            except PacienteNoEncontradoException as e:
                print(f" {e}")
            except MedicoNoDisponibleException as e:
                print(f" {e}")
            except TurnoOcupadoException as e:
                print(f" {e}")
            except RecetaInvalidaException as e:
                print(f" {e}")
            except Exception as e:
                print(f" Error inesperado: {str(e)}")

    def agregar_paciente(self):
        nombre = input("Nombre completo: ")
        dni = input("DNI: ")
        fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha)
        self.clinica.agregar_paciente(paciente)
        print(" Paciente registrado.")

    def agregar_medico(self):
        nombre = input("Nombre completo: ")
        matricula = input("Matrícula: ")
        medico = Medico(nombre, matricula)
        self.clinica.agregar_medico(medico)
        print(" Médico registrado.")

    def agregar_especialidad_a_medico(self):
        matricula = input("Matrícula del médico: ")
        tipo = input("Especialidad: ")
        dias = input("Días de atención (ej: lunes,miércoles): ").split(",")
        especialidad = Especialidad(tipo, [d.strip() for d in dias])
        medico = self.clinica.obtener_medico_por_matricula(matricula)
        medico.agregar_especialidad(especialidad)
        print(" Especialidad agregada al médico.")

    def agendar_turno(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        fecha_str = input("Fecha y hora (formato: aaaa-mm-dd HH:MM): ")

        try:
            fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print(" Formato de fecha inválido. Use aaaa-mm-dd HH:MM")
            return

        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
        print(" Turno agendado.")

    def emitir_receta(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos = input("Medicamentos (separados por coma): ").split(",")
        self.clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
        print(" Receta emitida.")

    def ver_historia_clinica(self):
        dni = input("DNI del paciente: ")
        historia = self.clinica.obtener_historia_clinica(dni)
        print(historia)

    def ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print(" No hay turnos registrados.")
        for turno in turnos:
            print(turno)

    def ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print(" No hay pacientes registrados.")
        for paciente in pacientes:
            print(paciente)

    def ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print(" No hay médicos registrados.")
        for medico in medicos:
            print(medico)


if __name__ == "__main__":
    cli = CLI()
    cli.mostrar_menu()
