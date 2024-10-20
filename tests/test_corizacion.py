import datetime
import sys
import os

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app.cliente import Cliente
from app.cotizacion import Cotizacion

def test_crear_cotizacion():
    cliente = Cliente("Juan Pérez", "123456789", "Calle Falsa 123")
    cotizacion = Cotizacion(cliente, datetime.date.today(), 1234)
    assert cotizacion.cliente == cliente
    assert cotizacion.ventanas == []
    assert cotizacion.fecha == datetime.date.today()
    assert cotizacion.num_factura == 1234