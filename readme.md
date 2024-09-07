# Sistema de Cotización de Ventanas

## Descripción

Este proyecto es una implementación en Python de un sistema de cotización de ventanas que permite crear clientes, agregar ventanas con naves, seleccionar tipos de vidrio y acabados, calcular costos y generar cotizaciones aplicando descuentos cuando corresponde.

## Requerimientos

- Python 3.7 o superior

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/usuario/sistema-cotizacion-ventanas.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd sistema-cotizacion-ventanas
    ```

3. (Opcional) Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - En macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. No es necesario instalar dependencias adicionales.

## Estructura del Proyecto

- `cliente.py`: Definición de la clase `Cliente`.
- `ventana.py`: Definición de la clase `Ventana`.
- `nave.py`: Definición de la clase `Nave`.
- `vidrio.py`: Definición de la clase `Vidrio`.
- `acabado.py`: Definición de la clase `Acabado`.
- `elementos_adicionales.py`: Definición de elementos adicionales (esquinas, chapas).
- `cotizacion.py`: Definición de la clase `Cotización`.
- `utils.py`: Funciones utilitarias (opcional).
- `main.py`: Archivo principal para la interacción del usuario.

## Uso

1. Ejecuta el sistema de cotización de ventanas:

    ```bash
    python main.py
    ```

2. Usa la interfaz de texto interactiva para agregar clientes, ventanas y generar cotizaciones.

## Diagrama de Clases

Aquí se incluiría un enlace al diagrama de clases UML, si estuviera disponible.

![Diagrama UML](imagenes/Cotizacion.png)

## Autor

Enzo Gonzalez Caicedo

## Licencia

MIT

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.
