class ElementoAdicional:
    """
    Representa elementos adicionales en las ventanas como esquinas o chapas.
    
    Atributos:
        tipo (str): Tipo de elemento (esquina, chapa).
        precio (float): Precio del elemento.
    """
    
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"{self.tipo} - ${self.precio}"