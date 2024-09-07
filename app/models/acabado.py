class Acabado:
    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un nuevo acabado con el nombre y el precio por metro lineal.

        Parámetros:
        nombre (str): El nombre del tipo de acabado (por ejemplo, "Pulido", "Lacado Mate").
        precio (float): El precio del acabado por metro lineal.
        """
        self.nombre = nombre  # Nombre del tipo de acabado
        self.precio = precio  # Precio del acabado por metro lineal

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena del objeto Acabado.

        Retorno:
        str: Una cadena que describe el acabado, incluyendo su nombre y precio por metro lineal.
        """
        return f"{self.nombre} - ${self.precio} por metro lineal"
