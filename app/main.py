from models.cliente import Cliente
from models.vidrio import Vidrio
from models.acabado import Acabado
from models.nave import Nave
from models.ventana import Ventana
from models.cotizacion import Cotizacion


def crear_cliente():
    """Crea un nuevo cliente."""
    nombre = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (ej. empresa constructora): ")
    direccion = input("Dirección: ")
    return Cliente(nombre, tipo_cliente, direccion)

def crear_ventana():
    """Crea una nueva ventana."""
    tipo = input("Tipo de ventana (O, XO, OXXO, etc.): ")
    ancho = float(input("Ancho de la ventana: "))
    alto = float(input("Alto de la ventana: "))
    ventana = Ventana(tipo, ancho, alto)

    num_naves = int(input("Número de naves: "))
    for _ in range(num_naves):
        ventana.agregar_nave(crear_nave())
    
    return ventana

def crear_nave():
    """Crea una nueva nave (panel)."""
    tipo = input("Tipo de nave (O, X): ")
    ancho = float(input("Ancho de la nave: "))
    alto = float(input("Alto de la nave: "))
    vidrio = seleccionar_vidrio()
    acabado = seleccionar_acabado()
    esmerilado = input("El vidrio es esmerilado? (s/n): ").lower() == 's'
    
    return Nave(tipo, ancho, alto, vidrio, acabado, esmerilado)

def seleccionar_vidrio():
    """Permite seleccionar un tipo de vidrio."""
    tipos_vidrio = {
        "1": Vidrio("Transparente", 8.25),
        "2": Vidrio("Bronce", 9.15),
        "3": Vidrio("Azul", 12.75)
    }
    
    print("Selecciona un tipo de vidrio:")
    for k, v in tipos_vidrio.items():
        print(f"{k}. {v}")
    
    opcion = input("Opción: ")
    return tipos_vidrio.get(opcion)

def seleccionar_acabado():
    """Permite seleccionar un tipo de acabado."""
    tipos_acabado = {
        "1": Acabado("Pulido", 50.7),
        "2": Acabado("Lacado Brillante", 54.2),
        "3": Acabado("Lacado Mate", 53.6),
        "4": Acabado("Anodizado", 57.3)
    }
    
    print("Selecciona un tipo de acabado:")
    for k, v in tipos_acabado.items():
        print(f"{k}. {v}")
    
    opcion = input("Opción: ")
    return tipos_acabado.get(opcion)

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
            ventana = crear_ventana()
            cotizacion.agregar_ventana(ventana)
            print(f"Ventana {ventana.tipo} agregada correctamente.")
        
        elif opcion == "2":
            print(f"\nCotización para {cliente.nombre}:")
            for ventana in cotizacion.ventanas:
                print(ventana)
        
        elif opcion == "3":
            total = cotizacion.calcular_total()
            print(f"\nEl costo total de la cotización es: ${total:.2f}")
        
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
