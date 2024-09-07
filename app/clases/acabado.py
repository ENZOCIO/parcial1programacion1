class Acabado:
    """
    Representa el tipo de acabado para el aluminio de las naves de las ventanas.
    
    Atributos:
        tipo (str): Tipo de acabado (pulido, lacado brillante, lacado mate, anodizado).
        precio_por_metro_lineal (float): Precio del acabado por metro lineal.
    """
    
    def __init__(self, tipo, precio_por_metro_lineal):
        self.tipo = tipo
        self.precio_por_metro_lineal = precio_por_metro_lineal

    def __str__(self):
        return f"{self.tipo} - ${self.precio_por_metro_lineal} por metro lineal"