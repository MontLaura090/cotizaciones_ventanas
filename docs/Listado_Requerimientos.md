# Requerimientos del Sistema de Cotización de Ventanas

Este documento especifica los requerimientos funcionales para el sistema de cotización de ventanas.

## Registro de Entidades

- El sistema debe permitir el registro de un estilo de ventana con los siguientes atributos: tipo de ventana (O, XO, OXXO, OXO), dimensiones (ancho y alto)
- El sistema debe permitir el registro de un tipo de vidrio con los atributos: tipo (transparente, bronce, azul) y precio por cm².
- El sistema debe permitir el registro de un acabado de aluminio con los atributos: tipo (pulido, lacado brillante, lacado mate, anodizado) y precio por metro lineal.
- El sistema debe permitir el registro de elementos adicionales con atributos: esquinas (precio por unidad), chapas (precio por unidad)
- El sistema debe permitir el registro de un cliente con los atributos: nombre, cedula y dirección de contacto.
- El sistema debe permitir el registro de una cotización con los atributos: fecha, número de cotización, cliente, listado de ventanas, y descuento si corresponde.

## Gestión de Precios

- El sistema debe calcular el costo de cada ventana teniendo en cuenta los siguientes elementos:
  - El sistema debe permitir contar la cantidad de letras del tipo de ventana para calcular las naves.
  - Precio del aluminio (por metro lineal) según el tipo de acabado.
  - Precio del vidrio (por cm²) y costo adicional si el vidrio es esmerilado.
  - Precio de las esquinas (cantidad por naves).
  - Precio de la chapa si aplica (para naves tipo X).
- El sistema debe aplicar un descuento del 10% si la cantidad de ventanas solicitadas excede las 100 unidades.

## Relaciones entre Entidades

- El sistema debe permitir asociar múltiples estilos de ventanas a un cliente.
- El sistema debe relacionar naves con ventanas, calculando automáticamente sus dimensiones basadas en el ancho y alto de la ventana completa.
- El sistema debe asociar un tipo de vidrio y un acabado a cada ventana.
- El sistema debe calcular automáticamente el número de esquinas y chapas necesarias para cada nave.

## Validaciones

- El sistema debe verificar que las dimensiones de las naves sean coherentes con el ancho y alto de la ventana.
- El sistema debe garantizar que el vidrio sea siempre 1.5 cm más pequeño que la nave en cada lado.
- El sistema debe asegurar que el descuento solo se aplique para más de 100 ventanas del mismo diseño.

