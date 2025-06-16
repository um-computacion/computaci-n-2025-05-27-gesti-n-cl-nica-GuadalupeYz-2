
from datetime import datetime
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.excepciones import DatosInvalidosException

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("Debe proporcionar un paciente válido.")
        if not isinstance(medico, Medico):
            raise DatosInvalidosException("Debe proporcionar un médico válido.")
        if not isinstance(fecha_hora, datetime):
            raise DatosInvalidosException("La fecha y hora deben ser un objeto datetime.")
        if fecha_hora < datetime.now():
            raise DatosInvalidosException("No se puede agendar un turno de una fecha pasada.")
        if not especialidad.strip():
            raise DatosInvalidosException("Debe indicar una especialidad.")

        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Turno: {self.__paciente} con {self.__medico} "
                f"({self.__especialidad}) el {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}")
