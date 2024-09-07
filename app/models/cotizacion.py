# models/cotizacion.py
from models.cliente import Cliente
from models.ventana import Ventana

class Cotizacion:
    def __init__(self, cliente: Cliente, descuento: float = 0):
        self.cliente = cliente
        self.ventanas = []
        self.descuento = descuento

    def agregar_ventana(self, ventana: Ventana):
        """Agrega una ventana a la cotización."""
        self.ventanas.append(ventana)

    def calcular_total(self) -> float:
        """Calcula el costo total de la cotización considerando el descuento."""
        total = sum(ventana.costo_total() for ventana in self.ventanas)
        total_con_descuento = total * (1 - self.descuento / 100)
        return round(total_con_descuento, 2)

    def __str__(self) -> str:
        return (f"Cliente:\n{self.cliente}\n"
                f"Ventanas:\n" + "\n".join(str(ventana) for ventana in self.ventanas) + "\n"
                f"Total con descuento: ${self.calcular_total():.2f}")
