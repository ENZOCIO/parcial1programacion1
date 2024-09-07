from typing import List
from models.nave import Nave

class Ventana:
    def __init__(self, tipo: str, ancho: float, alto: float, naves: List[Nave]):
        """
        Inicializa una nueva ventana con el tipo, dimensiones y naves especificadas.

        Parámetros:
        tipo (str): El tipo de ventana (por ejemplo, "OXXO", "XO").
        ancho (float): El ancho total de la ventana en centímetros.
        alto (float): El alto total de la ventana en centímetros.
        naves (List[Nave]): Una lista de naves que componen la ventana.
        """
        self.tipo = tipo  # Tipo de ventana (O, XO, OXXO, etc.)
        self.ancho = ancho  # Ancho de la ventana en cm
        self.alto = alto  # Alto de la ventana en cm
        self.naves = naves  # Lista de naves (paneles) de la ventana

    def agregar_nave(self, nave: Nave):
        """
        Agrega una nave a la ventana validando que sus dimensiones sean menores
        o iguales a las de la ventana.

        Parámetros:
        nave (Nave): La nave a agregar.

        Excepciones:
        ValueError: Se lanza si las dimensiones de la nave exceden las dimensiones de la ventana.
        """
        if nave.ancho <= self.ancho and nave.alto <= self.alto:
            self.naves.append(nave)  # Agregar la nave si sus dimensiones son válidas
        else:
            raise ValueError("Las dimensiones de la nave deben ser menores o iguales a las dimensiones de la ventana.")

    def costo_total(self) -> float:
        """
        Calcula el costo total de la ventana sumando los costos de las naves.

        Retorno:
        float: El costo total de la ventana, considerando el costo del vidrio y del acabado.
        """
        # Calcula el costo del vidrio en función de las dimensiones de cada nave
        costo_vidrio = sum(nave.ancho * nave.alto * nave.vidrio.precio for nave in self.naves)
        
        # Calcula el costo del acabado en función del ancho de cada nave
        costo_acabado = sum(nave.ancho * nave.acabado.precio for nave in self.naves)
        
        # Retorna la suma total del costo del vidrio y del acabado
        return costo_vidrio + costo_acabado

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena de la ventana y sus naves.

        Retorno:
        str: Una cadena que describe la ventana y las naves que la componen.
        """
        # Genera una descripción detallada de la ventana y sus naves
        return (f"Tipo: {self.tipo}, Ancho: {self.ancho} cm, Alto: {self.alto} cm\n"
                f"Naves:\n" + "\n".join(str(nave) for nave in self.naves))
