class Cotizacion:
    """
    Representa una cotización de ventanas.
    
    Atributos:
        cliente (Cliente): Cliente que solicita la cotización.
        ventanas (list): Lista de ventanas cotizadas.
        descuento (float): Porcentaje de descuento si aplica.
    """
    
    def __init__(self, cliente, descuento=0.0):
        self.cliente = cliente
        self.ventanas = []
        self.descuento = descuento

    def agregar_ventana(self, ventana):
        """Agrega una ventana a la cotización."""
        self.ventanas.append(ventana)

    def calcular_total(self):
        """Calcula el costo total de la cotización, aplicando el descuento si corresponde."""
        total = sum(ventana.calcular_costo() for ventana in self.ventanas)
        if len(self.ventanas) > 100:
            total *= 1 - (self.descuento / 100)
        return total

    def __str__(self):
        return f"Cotización para {self.cliente.nombre}, {len(self.ventanas)} ventanas"
