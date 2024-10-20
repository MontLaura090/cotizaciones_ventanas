import sys
import os

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app.nave import Nave


# Test para verificar la correcta inicialización de los atributos
def test_nave_attributes():
    nave = Nave("pulido", "transparente", False, 120, 100, 2, "XX")
    assert nave.tipo_de_acabado == "pulido"
    assert nave.tipo_de_vidrio == "transparente"
    assert nave.esmerilado == False
    assert nave.alto == 120
    assert nave.ancho_ventana == 100
    assert nave.cantidad_naves == 2
    assert nave.estilo == "XX"

# Test para verificar el cálculo del ancho por nave
def test_ancho_nave():
    nave = Nave("pulido", "transparente", False, 120, 100, 2, "XX")
    assert nave.ancho_nave == 50  # 100 dividido entre 2 naves

def test_calcular_precio_vidrio_transparente():
    nave = Nave("pulido", "transparente", False, 120, 100, 2, "XX")
    precio_vidrio = nave.calcular_precio_vidrio()
    assert pytest.approx(precio_vidrio, 0.01) == 8064.00