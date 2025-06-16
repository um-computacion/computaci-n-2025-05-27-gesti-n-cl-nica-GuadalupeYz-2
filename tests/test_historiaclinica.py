import unittest
from datetime import datetime, timedelta
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.turno import Turno
from codigo.receta import Receta
from codigo.historiaclinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("María Fernández", "12345678", "12/12/1985")
        self.medico = Medico("Dr. Gómez", "M789")
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        turno = Turno(self.paciente, self.medico, datetime.now() + timedelta(days=2), "Clínica")
        self.historia.agregar_turno(turno)
        self.assertIn(turno, self.historia.obtener_turnos())

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_receta(receta)
        self.assertIn(receta, self.historia.obtener_recetas())

    def test_str_con_datos(self):
        turno = Turno(self.paciente, self.medico, datetime.now() + timedelta(days=2), "Cardiología")
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        resumen = str(self.historia)
        self.assertIn("Turnos", resumen)
        self.assertIn("Recetas", resumen)
        self.assertIn("Paracetamol", resumen)

if __name__ == "__main__":
    unittest.main()
