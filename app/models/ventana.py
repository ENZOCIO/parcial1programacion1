from typing import List
from models.nave import Nave

class Ventana:
    def __init__(self, tipo: str, ancho: float, alto: float, naves: List[Nave]):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        self.naves = naves

    def agregar_nave(self, nave: Nave):
        """Agrega una nave a la ventana y valida dimensiones."""
        if nave.ancho <= self.ancho and nave.alto <= self.alto:
            self.naves.append(nave)
        else:
            raise ValueError("Las dimensiones de la nave deben ser menores o iguales a las dimensiones de la ventana.")

    def costo_total(self) -> float:
        """Calcula el costo total de la ventana, incluyendo naves."""
        costo_vidrio = sum(nave.ancho * nave.alto * nave.vidrio.precio for nave in self.naves)
        costo_acabado = sum(nave.ancho * nave.acabado.precio for nave in self.naves)
        return costo_vidrio + costo_acabado

    def __str__(self) -> str:
        return (f"Tipo: {self.tipo}, Ancho: {self.ancho} cm, Alto: {self.alto} cm\n"
                f"Naves:\n" + "\n".join(str(nave) for nave in self.naves))
