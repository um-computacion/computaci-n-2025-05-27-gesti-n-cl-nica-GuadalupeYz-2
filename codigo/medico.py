
from typing import List
from codigo.excepciones import DatosInvalidosException
from codigo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        if not nombre.strip():
            raise DatosInvalidosException("El nombre del médico no puede estar vacío.")
        if not matricula.strip():
            raise DatosInvalidosException("La matrícula del médico no puede estar vacía.")

        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades: List[Especialidad] = []

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = ', '.join(str(e) for e in self.__especialidades)
        return f"Dr/a {self.__nombre} (Matrícula: {self.__matricula}) - Especialidades: {especialidades_str}"
