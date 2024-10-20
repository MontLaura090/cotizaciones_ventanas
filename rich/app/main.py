from rich.console import Console
from rich.table import Table
from rich.text import Text
from ventana import Ventana 
from cotizacion import Cotizacion
from cliente import Cliente
from nave import Nave

console = Console()

def main():
    console.print("----- [bold blue]Bienvenido a la tienda de ventanas[/bold blue] -----", style="bold white")

    # Información del cliente
    nombre = console.input("[yellow]Ingrese su nombre: [/yellow]")
    cedula = console.input("[yellow]Ingrese su cédula: [/yellow]")
    direccion = console.input("[yellow]Ingrese su dirección: [/yellow]")
    
    cliente = Cliente(nombre, cedula, direccion)
    cotizacion = Cotizacion(cliente)

    # Cantidad de ventanas
    cantidad_ventanas = int(console.input("[yellow]¿Cuántas ventanas desea comprar? [/yellow]"))
    
    # Para cada ventana solicitamos los detalles
    for i in range(cantidad_ventanas):
        console.print(f"\n--- [bold magenta]Ventana {i + 1}[/bold magenta] ---", style="bold white")
        alto = float(console.input("[cyan]Ingrese el alto de la ventana en cm: [/cyan]"))
        ancho = float(console.input("[cyan]Ingrese el ancho de la ventana en cm: [/cyan]"))
        estilo = console.input("[cyan]Ingrese el estilo de la ventana (O, XO, OXO, OXXO): [/cyan]").upper()
        acabado = console.input("[cyan]Ingrese el tipo de acabado: [/cyan]")
        vidrio = console.input("[cyan]Ingrese el tipo de vidrio: [/cyan]")
        esmerilado = console.input("[cyan]¿Desea añadir esmerilado adicional? (Sí/No): [/cyan]").strip().lower() == 'sí'
        
        nave = Nave(tipo_de_acabado=acabado, tipo_de_vidrio=vidrio, esmerilado=esmerilado, alto=alto, ancho_ventana=ancho, cantidad_naves=1, estilo=estilo)

        # Calcular el precio de la nave
        precio_nave = nave.calcular_precio_nave()

        # Crear la instancia de Ventana
        ventana = Ventana(estilo=estilo, alto=alto, ancho=ancho, valor_nave=precio_nave, nave=nave, cantidad_naves=1)  
        # Agregar la ventana a la cotización
        cotizacion.agregar_ventana(ventana)

    total = cotizacion.calcular_total()
    
    # Usar una tabla para mostrar el total
    table = Table(title="[bold green]Total de la Cotización[/bold green]")
    table.add_column("Descripción", style="cyan", no_wrap=True)
    table.add_column("Total", style="magenta")

    table.add_row("Total de la cotización", str(total))
    
    console.print(table)
    console.print("[bold green]¡Gracias por su compra![/bold green]")

if __name__ == "__main__":
    main()
