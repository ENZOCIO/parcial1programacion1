from models.cliente import Cliente
from models.vidrio import Vidrio
from models.acabado import Acabado
from models.nave import Nave
from models.ventana import Ventana
from models.cotizacion import Cotizacion
from typing import List

def seleccionar_vidrio() -> Vidrio:
    """Permite seleccionar un tipo de vidrio."""
    opciones_vidrio = {
        "1": Vidrio("Transparente", 8.25),
        "2": Vidrio("Bronce", 9.15),
        "3": Vidrio("Azul", 12.75)
    }
    while True:
        print("Selecciona tipo de vidrio:")
        for clave, vidrio in opciones_vidrio.items():
            print(f"{clave}. {vidrio.nombre} - ${vidrio.precio:.2f} por cm²")
        opcion = input("Elige una opción: ")
        if opcion in opciones_vidrio:
            return opciones_vidrio[opcion]
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

def seleccionar_acabado() -> Acabado:
    """Permite seleccionar un tipo de acabado."""
    opciones_acabado = {
        "1": Acabado("Pulido", 50.7),
        "2": Acabado("Lacado Brillante", 54.2),
        "3": Acabado("Lacado Mate", 53.6),
        "4": Acabado("Anodizado", 57.3)
    }
    while True:
        print("Selecciona tipo de acabado:")
        for clave, acabado in opciones_acabado.items():
            print(f"{clave}. {acabado.nombre} - ${acabado.precio:.2f} por metro lineal")
        opcion = input("Elige una opción: ")
        if opcion in opciones_acabado:
            return opciones_acabado[opcion]
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

def seleccionar_tipo_ventana() -> str:
    """Permite seleccionar un tipo de ventana."""
    opciones_ventana = ["O", "XO", "OXXO", "OXO"]
    while True:
        print("Selecciona tipo de ventana:")
        for opcion in opciones_ventana:
            print(f"- {opcion}")
        tipo = input("Elige un tipo de ventana: ")
        if tipo in opciones_ventana:
            return tipo
        else:
            print("Tipo de ventana no válido. Por favor, elige una opción del menú.")

def crear_cliente() -> Cliente:
    """Solicita al usuario la información del cliente y crea un nuevo cliente."""
    nombre = input("Ingrese su nombre: ")
    tipo_cliente = input("Ingrese su tipo de cliente (por ejemplo, empresa constructora): ")
    direccion = input("Ingrese su dirección de contacto: ")
    return Cliente(nombre, tipo_cliente, direccion)

def crear_ventana(tipo: str, ancho: float, alto: float, naves: List[Nave]) -> Ventana:
    """Crea una nueva ventana."""
    return Ventana(tipo, ancho, alto, naves)

def crear_nave(tipo: str, ancho: float, alto: float, vidrio: Vidrio, acabado: Acabado, esmerilado: bool) -> Nave:
    """Crea una nueva nave (panel)."""
    return Nave(tipo, ancho, alto, vidrio, acabado, esmerilado)

def main():
    """Función principal que ejecuta el sistema."""
    print("Bienvenido al sistema de cotización de ventanas")

    cliente = crear_cliente()
    cotizacion = Cotizacion(cliente, descuento=10)  # Descuento de 10% si aplica

    while True:
        print("\nMenú Principal:")
        print("1. Agregar ventana")
        print("2. Ver cotización")
        print("3. Calcular total")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tipo_ventana = seleccionar_tipo_ventana()
            ancho_ventana = float(input("Ancho de la ventana (en cm): "))
            alto_ventana = float(input("Alto de la ventana (en cm): "))

            num_naves = int(input("Número de naves: "))
            naves = []
            for _ in range(num_naves):
                tipo_nave = input("Tipo de nave (O, X): ")
                ancho_nave = float(input("Ancho de la nave (en cm): "))
                alto_nave = float(input("Alto de la nave (en cm): "))
                vidrio = seleccionar_vidrio()
                acabado = seleccionar_acabado()
                esmerilado = input("¿El vidrio es esmerilado? (s/n): ").lower() == 's'

                nave = crear_nave(tipo_nave, ancho_nave, alto_nave, vidrio, acabado, esmerilado)
                naves.append(nave)

            ventana = crear_ventana(tipo_ventana, ancho_ventana, alto_ventana, naves)
            cotizacion.agregar_ventana(ventana)
            print("Ventana agregada a la cotización.")

        elif opcion == "2":
            print("Detalles de la cotización:")
            print(cotizacion)

        elif opcion == "3":
            total = cotizacion.calcular_total()
            print(f"El total de la cotización es: ${total:.2f}")

        elif opcion == "4":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
            print(f"Nombre del cliente: {cliente.nombre}")
            print(f"Tipo de cliente: {cliente.tipo}")
            print(f"Dirección del cliente: {cliente.direccion}")

if __name__ == "__main__":
    main()