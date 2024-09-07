class Cliente:
    """
    Representa a un cliente del sistema de cotización de ventanas.
    
    Atributos:
        nombre (str): Nombre del cliente.
        tipo_cliente (str): Tipo de cliente (ej. empresa constructora).
        direccion (str): Dirección del cliente.
    """
    
    def __init__(self, nombre, tipo_cliente, direccion):
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} - {self.tipo_cliente} - {self.direccion}"
