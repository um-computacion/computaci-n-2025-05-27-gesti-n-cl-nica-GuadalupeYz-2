import unittest
from codigo.paciente import Paciente
from codigo.excepciones import DatosInvalidosException

class TestPaciente(unittest.TestCase):
    def test_creacion_paciente(self):
        paciente = Paciente("Guadalupe Yañez", "46546133", "01/01/2000")
        self.assertEqual(paciente.obtener_dni(), "46546133")

    def test_str(self):
        paciente = Paciente("Guadalupe Yañez", "46546133", "01/01/2000")
        esperado = "Guadalupe Yañez (DNI: 46546133, Nacimiento: 01/01/2000)"
        self.assertEqual(str(paciente), esperado)


class TestPaciente(unittest.TestCase):
    def test_creacion_valida(self):
        paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        self.assertEqual(paciente.obtener_dni(), "12345678")

    def test_str(self):
        paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        esperado = "Juan Pérez (DNI: 12345678, Nacimiento: 01/01/2000)"
        self.assertEqual(str(paciente), esperado)

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "12345678", "01/01/2000")

    def test_dni_vacio_lanza_error(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "", "01/01/2000")

    def test_fecha_nacimiento_vacia_lanza_error(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "12345678", "")

if __name__ == "__main__":
    unittest.main()

