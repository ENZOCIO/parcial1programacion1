class Ventana:
    """
    Representa una ventana con varias naves (paneles).
    
    Atributos:
        tipo (str): Tipo de ventana (O, XO, OXXO, etc.).
        ancho (float): Ancho total de la ventana.
        alto (float): Alto total de la ventana.
        naves (list): Lista de naves (paneles) en la ventana.
    """
    
    def __init__(self, tipo, ancho, alto):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        self.naves = []

    def agregar_nave(self, nave):
        """Agrega una nave a la ventana."""
        self.naves.append(nave)

    def calcular_costo(self):
        """Calcula el costo total de la ventana sumando el costo de todas las naves."""
        return sum(nave.calcular_costo() for nave in self.naves)

    def __str__(self):
        return f"Ventana {self.tipo} - {self.ancho}x{self.alto} cm"