from datetime import datetime
from codigo.paciente import Paciente
from codigo.medico import Medico
from codigo.excepciones import RecetaInvalidaException

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not isinstance(paciente, Paciente):
            raise RecetaInvalidaException("Debe proporcionar un paciente válido.")
        if not isinstance(medico, Medico):
            raise RecetaInvalidaException("Debe proporcionar un médico válido.")
        if not medicamentos or not all(m.strip() for m in medicamentos):
            raise RecetaInvalidaException("Debe proporcionar al menos un medicamento no vacío.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return (
            f"Receta para {self.__paciente} por {self.__medico} "
            f"el {self.__fecha.strftime('%d/%m/%Y')}: Medicamentos: {medicamentos_str}"
        )
