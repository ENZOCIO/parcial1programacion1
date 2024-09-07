from models.vidrio import Vidrio
from models.acabado import Acabado

class Nave:
    def __init__(self, tipo: str, ancho: float, alto: float, vidrio: Vidrio, acabado: Acabado, esmerilado: bool):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        self.vidrio = vidrio
        self.acabado = acabado
        self.esmerilado = esmerilado

    def __str__(self) -> str:
        esmerilado_str = "Sí" if self.esmerilado else "No"
        return (f"Tipo: {self.tipo}, Ancho: {self.ancho} cm, Alto: {self.alto} cm\n"
                f"Vidrio: {self.vidrio}\n"
                f"Acabado: {self.acabado}\n"
                f"Esmerilado: {esmerilado_str}")
