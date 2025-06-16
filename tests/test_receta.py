import unittest
from datetime import datetime
from codigo.receta import Receta
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.especialidad import Especialidad
from codigo.excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):
    def test_crear_receta_valida(self):
        paciente = Paciente("Lucía", "123", "01/01/2000")
        medico = Medico("Dr. Salas", "M123")
        esp = Especialidad("Clínica", ["lunes"])
        medico.agregar_especialidad(esp)

        receta = Receta(paciente, medico, ["Ibuprofeno", "Paracetamol"])
        self.assertIn("Ibuprofeno", str(receta))
        self.assertIn("Dr. Salas", str(receta))

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana Gómez", "12345678", "01/01/1980")
        self.medico = Medico("Dra. López", "M987")

    def test_receta_valida(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Ibuprofeno", str(receta))

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])

    def test_receta_con_medicamento_vacio(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [""])

if __name__ == "__main__":
    unittest.main()
