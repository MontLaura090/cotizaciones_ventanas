class Cotizacion:
    def __init__(self, cliente):
        self.cliente = cliente
        self.ventanas = []

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def calcular_total(self):
        total = 0
        for ventana in self.ventanas:
            total += ventana.calcular_precio()  # Suponiendo que la clase Ventana tiene un método calcular_precio()
        return total

    def mostrar_cotizacion(self):
        print("Cotización para:")
        print(f"Nombre: {self.cliente.nombre}")
        print(f"Cédula: {self.cliente.cedula}")
        print(f"Dirección: {self.cliente.direccion}")
        print("\nDetalle de ventanas:")
        for i, ventana in enumerate(self.ventanas, start=1):
            print(f"Ventana {i}: {ventana.estilo} - Precio: ${ventana.calcular_precio():.2f}")
        print(f"\nTotal a pagar: ${self.calcular_total():.2f}")
