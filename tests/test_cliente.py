import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app.cliente import Cliente

# Test para verificar que los tipos de datos son los correctos.
def test_cliente_data_types():
    cliente = Cliente("Juan Perez", "123456789", "Calle Falsa 123")
    assert isinstance(cliente.nombre, str)
    assert isinstance(cliente.cedula, str)
    assert isinstance(cliente.direccion, str)

# Test para verificar que los atributos se asignan correctamente al instanciar un objeto Cliente.
def test_cliente_attributes():
    cliente = Cliente("Juan Perez", "123456789", "Calle Falsa 123")
    assert cliente.nombre == "Juan Perez"
    assert cliente.cedula == "123456789"
    assert cliente.direccion == "Calle Falsa 123"

# Test para verificar que un cliente con datos vacíos aún se puede crear.
def test_cliente_empty_attributes():
    cliente = Cliente("", "", "")
    assert cliente.nombre == ""
    assert cliente.cedula == ""
    assert cliente.direccion == ""
