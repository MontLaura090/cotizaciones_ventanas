from nave import Nave

class Ventana:
    def __init__(self, estilo: str, alto: int, ancho: int, valor_nave: float, nave: Nave, cantidad_naves: int = 0):
        self.estilo = estilo
        self.alto = alto
        self.ancho = ancho
        self.valor_nave = valor_nave
        self.cantidad_naves = cantidad_naves if cantidad_naves > 0 else self.calcular_numero_naves()
        self.nave = nave

    def calcular_numero_naves(self) -> int:
        # El número de naves es el número de caracteres en el estilo (p. ej., "XO" -> 2 naves)
        return len(self.estilo)

    def calcular_precio(self) -> float:
        # Si la cantidad de naves no está definida, la calculamos
        if self.cantidad_naves == 0:
            self.cantidad_naves = self.calcular_numero_naves()

        # Calcular el precio total en función del valor por nave y la cantidad de naves
        precio_total = self.valor_nave * self.cantidad_naves
        return precio_total

