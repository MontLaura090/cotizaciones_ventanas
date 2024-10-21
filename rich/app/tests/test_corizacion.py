import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from cliente import Cliente
from cotizacion import Cotizacion

class MockVentana:
    def __init__(self, precio):
        self.precio = precio
    
    def calcular_precio(self):
        return self.precio

def test_agregar_ventana():
    cliente = Cliente("Juan Pérez", "1234567890", "Calle Falsa 123")
    cotizacion = Cotizacion(cliente)
    
    ventana = MockVentana(500)
    cotizacion.agregar_ventana(ventana)
    
    assert len(cotizacion.ventanas) == 1
    assert cotizacion.ventanas[0] == ventana

def test_calcular_total():
    cliente = Cliente("Juan Pérez", "1234567890", "Calle Falsa 123")
    cotizacion = Cotizacion(cliente)

    ventana1 = MockVentana(500)
    ventana2 = MockVentana(800)

    cotizacion.agregar_ventana(ventana1)
    cotizacion.agregar_ventana(ventana2)

    total = cotizacion.calcular_total()

    assert total == 1300  # 500 + 800
