 
from codigo.excepciones import DatosInvalidosException

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise DatosInvalidosException("El nombre no puede estar vacío.")
        if not dni.strip():
            raise DatosInvalidosException("El DNI no puede estar vacío.")
        if not fecha_nacimiento.strip():
            raise DatosInvalidosException("La fecha de nacimiento no puede estar vacía.")

        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre} (DNI: {self.__dni}, Nacimiento: {self.__fecha_nacimiento})"
  