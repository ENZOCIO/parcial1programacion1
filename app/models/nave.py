from models.vidrio import Vidrio
from models.acabado import Acabado

class Nave:
    def __init__(self, tipo: str, ancho: float, alto: float, vidrio: Vidrio, acabado: Acabado, esmerilado: bool):
        """
        Inicializa una nueva nave (panel) con el tipo, dimensiones, vidrio, acabado y opción de esmerilado.

        Parámetros:
        tipo (str): El tipo de nave (por ejemplo, "O" o "X").
        ancho (float): El ancho de la nave en centímetros.
        alto (float): El alto de la nave en centímetros.
        vidrio (Vidrio): El tipo de vidrio utilizado en la nave.
        acabado (Acabado): El tipo de acabado aplicado en la nave.
        esmerilado (bool): Indica si el vidrio es esmerilado (True) o no (False).
        """
        self.tipo = tipo  # Tipo de la nave (O, X, etc.)
        self.ancho = ancho  # Ancho de la nave en cm
        self.alto = alto  # Alto de la nave en cm
        self.vidrio = vidrio  # Tipo de vidrio utilizado en la nave
        self.acabado = acabado  # Tipo de acabado aplicado en la nave
        self.esmerilado = esmerilado  # Indica si el vidrio es esmerilado

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena del objeto Nave.
        
        Retorno:
        str: Una cadena que describe el tipo de nave, sus dimensiones, vidrio, acabado y si es esmerilado.
        """
        esmerilado_str = "Sí" if self.esmerilado else "No"  # Cadena que representa si el vidrio es esmerilado
        return (f"Tipo: {self.tipo}, Ancho: {self.ancho} cm, Alto: {self.alto} cm\n"
                f"Vidrio: {self.vidrio}\n"
                f"Acabado: {self.acabado}\n"
                f"Esmerilado: {esmerilado_str}")
