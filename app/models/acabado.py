class Acabado:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio} por metro lineal"
