
---

### Archivo `requerimientos.md`

```markdown
# Requerimientos del Sistema de Cotización de Ventanas

Este documento describe los requerimientos funcionales para el sistema de cotización de ventanas.

## Registro de Entidades

- El sistema debe permitir registrar un estilo de ventana con los atributos: tipo de ventana (O, XO, OXXO, OXO), ancho, alto, y cantidad de naves.
- El sistema debe permitir registrar una nave con los atributos: tipo de nave (O o X), ancho, alto, tipo de vidrio, tipo de acabado, y si aplica, si es esmerilado.
- El sistema debe permitir registrar un tipo de vidrio con los atributos: tipo de vidrio (transparente, bronce, azul) y precio por cm².
- El sistema debe permitir registrar un acabado de aluminio con los atributos: tipo de acabado (pulido, lacado brillante, lacado mate, anodizado) y precio por metro lineal.
- El sistema debe permitir registrar los elementos adicionales con los atributos: esquinas (precio por unidad), chapas (precio por unidad), y materiales adicionales incluidos (remaches, tornillos, caucho).
- El sistema debe permitir registrar un cliente con los atributos: nombre, tipo de cliente (ej. empresa constructora), y dirección de contacto.
- El sistema debe permitir registrar una cotización con los atributos: fecha, número de cotización, cliente, listado de ventanas y descuento si aplica.

## Gestión de Precios

- El sistema debe permitir calcular el costo de cada ventana, teniendo en cuenta los siguientes elementos:
  - Precio del aluminio (en metros lineales) según el tipo de acabado.
  - Precio del vidrio (en cm²) y el costo adicional si el vidrio es esmerilado.
  - Precio de las esquinas (cantidad por ventana).
  - Precio de la chapa si aplica (para naves tipo X).
- El sistema debe permitir aplicar un descuento del 10% si la cantidad de ventanas solicitadas supera las 100 unidades.

## Relaciones entre Entidades

- El sistema debe permitir asignar varios estilos de ventanas a un cliente.
- El sistema debe permitir relacionar naves con ventanas, calculando automáticamente sus dimensiones basadas en el ancho y alto de la ventana completa.
- El sistema debe permitir asociar un tipo de vidrio y un acabado a cada nave.
- El sistema debe permitir calcular automáticamente el número de esquinas y chapas necesarias para cada ventana según el tipo y cantidad de naves.

## Consultas y Reportes

- El sistema debe permitir consultar la información de una ventana, incluyendo el tipo, las dimensiones (ancho, alto), número de naves, tipo de vidrio, acabado, y el costo total.
- El sistema debe permitir consultar la información de un cliente, incluyendo su nombre, tipo de cliente y las cotizaciones que ha solicitado.
- El sistema debe permitir consultar las cotizaciones realizadas, incluyendo el cliente, fecha de la cotización, y el costo total.
- El sistema debe generar informes de cotizaciones, mostrando el desglose de costos por ventana y aplicando los descuentos si corresponde.

## Validaciones

- El sistema debe validar que las dimensiones de las naves sean consistentes con el ancho y alto de la ventana.
- El sistema debe validar que el vidrio sea siempre 1.5 cm más pequeño que la nave por cada lado.
- El sistema debe validar que el descuento solo se aplique si se solicitan más de 100 ventanas del mismo diseño.
