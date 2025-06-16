import unittest
from datetime import datetime, timedelta
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.especialidad import Especialidad
from codigo.clinica import Clinica
from codigo.excepciones import *

def proximo_dia_semana(dia_deseado: int) -> datetime:
    hoy = datetime.now()
    dias_hasta = (dia_deseado - hoy.weekday() + 7) % 7
    if dias_hasta == 0:
        dias_hasta = 7
    return hoy + timedelta(days=dias_hasta)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("María", "999", "01/01/1990")
        self.medico = Medico("Dr. López", "M789")
        self.esp = Especialidad("Cardiología", ["miércoles"])
        self.medico.agregar_especialidad(self.esp)

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_correcto_miercoles(self):
        fecha = proximo_dia_semana(2)  # 2 = miércoles
        self.clinica.agendar_turno("999", "M789", "Cardiología", fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_turno_ocupado_miercoles(self):
        fecha = proximo_dia_semana(2)  # 2 = miércoles
        self.clinica.agendar_turno("999", "M789", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("999", "M789", "Cardiología", fecha)

    def test_emitir_receta_valida(self):
        self.clinica.emitir_receta("999", "M789", ["Medicamento X"])
        historia = self.clinica.obtener_historia_clinica("999")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_vacia(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("999", "M789", [])
