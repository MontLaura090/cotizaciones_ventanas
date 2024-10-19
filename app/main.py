from ventana import Ventana 
from cotizacion import Cotizacion
from cliente import Cliente
from nave import Nave

def main():
    print("----- Bienvenido a la tienda de ventanas -----")

    # Información del cliente
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese su cédula: ")
    direccion = input("Ingrese su dirección: ")
    
    cliente = Cliente(nombre, cedula, direccion)
    cotizacion = Cotizacion(cliente)

    # Cantidad de ventanas
    cantidad_ventanas = int(input("¿Cuántas ventanas desea comprar? "))
    
    # Para cada ventana solicitamos los detalles
    for i in range(cantidad_ventanas):
        print(f"\n--- Ventana {i + 1} ---")
        alto = float(input("Ingrese el alto de la ventana en cm: "))
        ancho = float(input("Ingrese el ancho de la ventana en cm: "))
        estilo = input("Ingrese el estilo de la ventana (O, XO, OXO, OXXO): ").upper()
        acabado = input("Ingrese el tipo de acabado: ")
        vidrio = input("Ingrese el tipo de vidrio: ")
        esmerilado = input("¿Desea añadir esmerilado adicional? (Sí/No): ").strip().lower() == 'sí'
        
        nave = Nave(tipo_de_acabado=acabado, tipo_de_vidrio=vidrio, esmerilado=esmerilado, alto=alto, ancho_ventana=ancho, cantidad_naves=1, estilo=estilo)

        # Calcular el precio de la nave
        precio_nave = nave.calcular_precio_nave()

        # Crear la instancia de Ventana
        ventana = Ventana(estilo=estilo, alto=alto, ancho=ancho, valor_nave=precio_nave, nave=nave, cantidad_naves=1)  
        # Agregar la ventana a la cotización
        cotizacion.agregar_ventana(ventana)
        
    total = cotizacion.calcular_total()
    print(f"\nEl total de la cotización es: {total}")

if __name__ == "__main__":
    main()
