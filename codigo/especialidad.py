
from codigo.excepciones import DatosInvalidosException

class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo.strip():
            raise DatosInvalidosException("El nombre de la especialidad no puede estar vacío.")
        if not dias:
            raise DatosInvalidosException("Debe indicar al menos un día de atención.")
        
        dias_validos = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"}
        for dia in dias:
            if dia.lower() not in dias_validos:
                raise DatosInvalidosException(f"'{dia}' no es un día válido.")

        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ', '.join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
