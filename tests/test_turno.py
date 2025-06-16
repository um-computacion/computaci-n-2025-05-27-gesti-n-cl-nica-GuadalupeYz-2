import unittest
from datetime import datetime, timedelta
from codigo.turno import Turno
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.especialidad import Especialidad
from codigo.excepciones import DatosInvalidosException

class TestTurno(unittest.TestCase):
    def test_crear_turno(self):
        paciente = Paciente("Carlos Soto", "12345678", "01/01/1990")
        medico = Medico("Dr. Fernández", "M002")
        esp = Especialidad("Clínica", ["martes"])
        medico.agregar_especialidad(esp)
        fecha = datetime(2025, 6, 10, 10, 0)
        turno = Turno(paciente, medico, fecha, "Clínica")

        self.assertEqual(turno.obtener_medico(), medico)
        self.assertEqual(turno.obtener_fecha_hora(), fecha)


class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. González", "M123")

    def test_turno_valido(self):
        fecha = datetime.now() + timedelta(days=1)
        turno = Turno(self.paciente, self.medico, fecha, "Pediatría")
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), fecha)

    def test_turno_con_fecha_pasada(self):
        fecha_pasada = datetime.now() - timedelta(days=1)
        with self.assertRaises(DatosInvalidosException):
            Turno(self.paciente, self.medico, fecha_pasada, "Pediatría")

    def test_turno_sin_especialidad(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(DatosInvalidosException):
            Turno(self.paciente, self.medico, fecha, "")

if __name__ == "__main__":
    unittest.main()
