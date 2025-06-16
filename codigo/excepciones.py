
class PacienteNoEncontradoException(Exception):
    """Se lanza cuando un paciente no está registrado en la clínica."""
    pass

class MedicoNoDisponibleException(Exception):
    """Se lanza cuando el médico no atiende en el día o especialidad solicitada."""
    pass

class TurnoOcupadoException(Exception):
    """Se lanza cuando ya existe un turno en la fecha/hora para ese médico."""
    pass

class RecetaInvalidaException(Exception):
    """Se lanza cuando la receta es inválida (por ejemplo, sin medicamentos)."""
    pass

class DatosInvalidosException(Exception):
    """Se lanza cuando algún dato obligatorio está vacío o es incorrecto."""
    pass

