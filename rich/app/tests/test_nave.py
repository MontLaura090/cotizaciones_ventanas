import sys
import os

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from nave import Nave

def test_calcular_precio_vidrio():
    nave = Nave("pulido", "transparente", False, 15, 12, 1, "XO")
    precio_vidrio = nave.calcular_precio_vidrio()
    
    # Área del vidrio ajustado: (15 - 3) * (12 - 3) = 12 * 9 = 108 cm2
    # Precio por cm2 del vidrio transparente = 8.25
    precio_esperado = 108 * 8.25
    assert pytest.approx(precio_vidrio, 0.01) == precio_esperado

def test_calcular_precio_aluminio():
    nave = Nave("pulido", "transparente", False, 15, 12, 1, "XO")
    precio_aluminio = nave.calcular_precio_aluminio()

    # Ancho ajustado: (12 - 8 + 2) = 6, Alto ajustado: (15 - 8 + 2) = 9
    # Perímetro: 2 * (6 + 9) = 30
    # Precio por metro del aluminio pulido = 507
    precio_esperado = 30 * 507
    assert pytest.approx(precio_aluminio, 0.01) == precio_esperado

def test_calcular_precio_chapas():
    nave = Nave("pulido", "transparente", False, 15, 12, 1, "OXXO")
    precio_chapas = nave.calcular_precio_chapas()

    # Cantidad de chapas: 2 (por cada 'X')
    precio_esperado = 2 * 16200
    assert precio_chapas == precio_esperado

def test_calcular_precio_nave():
    nave = Nave("pulido", "transparente", False, 15, 12, 1, "XO")
    precio_nave = nave.calcular_precio_nave()

    # Sumar todos los componentes: vidrio, aluminio, chapas y esquinas
    precio_vidrio = nave.calcular_precio_vidrio()
    precio_aluminio = nave.calcular_precio_aluminio()
    precio_chapas = nave.calcular_precio_chapas()
    precio_esquinas = 17240  # Para una nave
    precio_esperado = precio_vidrio + precio_aluminio + precio_chapas + precio_esquinas

    assert pytest.approx(precio_nave, 0.01) == precio_esperado
