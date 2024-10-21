import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from cliente import Cliente

def test_cliente_attributes():
    cliente = Cliente("Juan Pérez", "1234567890", "Calle Falsa 123")

    assert cliente.nombre == "Juan Pérez"
    assert cliente.cedula == "1234567890"
    assert cliente.direccion == "Calle Falsa 123"
