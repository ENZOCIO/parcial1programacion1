class Vidrio:
    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un nuevo objeto Vidrio.

        Parámetros:
        nombre (str): El nombre del tipo de vidrio.
        precio (float): El precio del vidrio por centímetro cuadrado (cm²).
        """
        self.nombre = nombre  # Nombre del vidrio (por ejemplo, "Transparente", "Bronce")
        self.precio = precio  # Precio por cm² del vidrio

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena del objeto Vidrio.
        
        Retorno:
        str: Una cadena que describe el tipo de vidrio y su precio por cm².
        """
        return f"{self.nombre} - ${self.precio:.2f} por cm²"
