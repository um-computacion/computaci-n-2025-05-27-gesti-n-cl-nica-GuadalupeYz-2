
import unittest
from codigo.especialidad import Especialidad
from codigo.excepciones import DatosInvalidosException

class TestEspecialidad(unittest.TestCase):
    def test_creacion_valida(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Cardiología")
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertFalse(esp.verificar_dia("domingo"))

    def test_str(self):
        esp = Especialidad("Dermatología", ["lunes", "viernes"])
        esperado = "Dermatología (Días: lunes, viernes)"
        self.assertEqual(str(esp), esperado)

    def test_tipo_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("", ["lunes"])

    def test_dias_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("Pediatría", [])

    def test_dia_invalido(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("Oftalmología", ["lunes", "funday"])

if __name__ == "__main__":
    unittest.main()
