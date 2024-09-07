# models/cliente.py
class Cliente:
    def __init__(self, nombre: str, tipo: str, direccion: str):
        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Dirección: {self.direccion}")
