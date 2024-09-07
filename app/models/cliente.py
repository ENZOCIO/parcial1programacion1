class Cliente:
    def __init__(self, nombre: str, tipo: str, direccion: str):
        """
        Inicializa un nuevo cliente con el nombre, tipo y dirección.

        Parámetros:
        nombre (str): El nombre del cliente.
        tipo (str): El tipo de cliente (por ejemplo, empresa constructora, particular, etc.).
        direccion (str): La dirección de contacto del cliente.
        """
        self.nombre = nombre  # Nombre del cliente
        self.tipo = tipo  # Tipo de cliente
        self.direccion = direccion  # Dirección de contacto del cliente

    def __str__(self) -> str:
        """
        Retorna una representación en forma de cadena del objeto Cliente.

        Retorno:
        str: Una cadena que describe al cliente, incluyendo su nombre, tipo y dirección.
        """
        return (f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Dirección: {self.direccion}")
