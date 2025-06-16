import unittest
from codigo.medico import Medico
from codigo.especialidad import Especialidad
from codigo.excepciones import DatosInvalidosException

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dra. Ruiz", "M001")

    def test_agregar_especialidad(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(esp)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Pediatría")

    def test_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "M001")


class TestMedico(unittest.TestCase):
    def test_creacion_valida(self):
        medico = Medico("Laura Méndez", "A123")
        self.assertEqual(medico.obtener_matricula(), "A123")

    def test_str(self):
        medico = Medico("Laura Méndez", "A123")
        self.assertIn("Laura Méndez", str(medico))
        self.assertIn("Matrícula: A123", str(medico))

    def test_nombre_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Medico("", "A123")

    def test_matricula_vacia(self):
        with self.assertRaises(DatosInvalidosException):
            Medico("Laura Méndez", "")

if __name__ == "__main__":
    unittest.main()
