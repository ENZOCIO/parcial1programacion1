from models.cliente import Cliente
from models.ventana import Ventana

class Cotizacion:
    def __init__(self, cliente: Cliente, descuento: float = 0):
        """
        Inicializa una nueva cotización con el cliente y un descuento opcional.

        Parámetros:
        cliente (Cliente): El cliente para quien se realiza la cotización.
        descuento (float, opcional): El porcentaje de descuento aplicado a la cotización. Por defecto es 0.
        """
        self.cliente = cliente  # Cliente al que se le realiza la cotización
        self.ventanas = []  # Lista de ventanas incluidas en la cotización
        self.descuento = descuento  # Porcentaje de descuento aplicado a la cotización

    def agregar_ventana(self, ventana: Ventana):
        """
        Agrega una ventana a la cotización.

        Parámetros:
        ventana (Ventana): La ventana a agregar a la cotización.
        """
        self.ventanas.append(ventana)  # Añade la ventana a la lista de ventanas de la cotización

    def calcular_total(self) -> float:
        """
        Calcula el costo total de la cotización, aplicando el descuento.

        Retorno:
        float: El costo total de la cotización después de aplicar el descuento, redondeado a dos decimales.
        """
        # Calcula el costo total de todas las ventanas en la cotización
        total = sum(ventana.costo_total() for ventana in self.ventanas)
        
        # Aplica el descuento al costo total
        total_con_descuento = total * (1 - self.descuento / 100)
        
        # Retorna el costo total después de aplicar el descuento, redondeado a dos decimales
        return round(total_con_descuento, 2)

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena de la cotización.

        Retorno:
        str: Una cadena que describe el cliente, las ventanas en la cotización y el total con descuento.
        """
        return (f"Cliente:\n{self.cliente}\n"
                f"Ventanas:\n" + "\n".join(str(ventana) for ventana in self.ventanas) + "\n"
                f"Total con descuento: ${self.calcular_total():.2f}")
