from nave import Nave

class Ventana:
    def __init__(self, estilo: str, alto: int, ancho: int, valor_nave: float,nave: Nave, cantidad_naves: int = 0):
        self.estilo = estilo
        self.alto = alto
        self.ancho = ancho
        self.valor_nave = valor_nave
        self.cantidad_naves = cantidad_naves
        self.nave = nave 

    def calcular_numero_naves(self) -> int:
        return len(self.estilo)

    def calcular_precio(self) -> float:
        self.calcular_numero_naves()  
        precio_total = self.valor_nave * self.cantidad_naves
        return precio_total
