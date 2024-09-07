class Vidrio:
    """
    Representa un tipo de vidrio utilizado en las naves de las ventanas.
    
    Atributos:
        tipo (str): Tipo de vidrio (transparente, bronce, azul).
        precio_por_cm2 (float): Precio por cm² del vidrio.
    """
    
    def __init__(self, tipo, precio_por_cm2):
        self.tipo = tipo
        self.precio_por_cm2 = precio_por_cm2

    def __str__(self):
        return f"{self.tipo} - ${self.precio_por_cm2} por cm²"