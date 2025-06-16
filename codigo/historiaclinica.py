from codigo.paciente import Paciente
from codigo.turno import Turno
from codigo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos: list[Turno] = []
        self.__recetas: list[Receta] = []

    def agregar_turno(self, turno: Turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

    def __str__(self) -> str:
        texto = f"\n Historia clínica de {self.__paciente}\n"
        texto += "\n--- Turnos ---\n"
        texto += "\n".join(str(t) for t in self.__turnos) if self.__turnos else "Sin turnos registrados."
        texto += "\n\n--- Recetas ---\n"
        texto += "\n".join(str(r) for r in self.__recetas) if self.__recetas else "Sin recetas registradas."
        return texto
