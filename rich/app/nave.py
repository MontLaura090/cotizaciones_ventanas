class Nave:
    def __init__(self, tipo_de_acabado: str, tipo_de_vidrio: str, esmerilado: bool, alto: int, ancho_ventana: int, cantidad_naves: int, estilo: str):
        self.tipo_de_acabado = tipo_de_acabado
        self.tipo_de_vidrio = tipo_de_vidrio
        self.esmerilado = esmerilado
        self.alto = alto
        self.ancho_ventana = ancho_ventana  
        self.cantidad_naves = cantidad_naves  
        self.estilo = estilo

    @property
    def ancho_nave(self) -> int:
        if self.cantidad_naves > 0:
            return self.ancho_ventana // self.cantidad_naves
        return 0

    def calcular_precio_vidrio(self) -> float:
        precios_vidrio = {
            "transparente": 8.25,
            "bronce": 9.15,
            "azul": 12.75
        }
        area_nave = (self.alto - 3) * (self.ancho_nave - 3)  # Ajustar área
        precio_vidrio_cm2 = precios_vidrio.get(self.tipo_de_vidrio.lower(), 0)
        precio_vidrio = area_nave * precio_vidrio_cm2
        
        if self.esmerilado:
            precio_vidrio += area_nave * 5.20  # Costo adicional por esmerilado
        
        return precio_vidrio

    def calcular_precio_aluminio(self) -> float:
        # Diccionario con precios por tipo de acabado
        precios_aluminio = {
            "pulido": 507,
            "lacado brillante": 542,
            "lacado mate": 536,
            "anodizado": 573
        }

        # Ajustar las dimensiones del aluminio
        a = self.ancho_nave - 8 + 2  # Ajustes en el ancho
        b = self.alto - 8 + 2  # Ajustes en la altura
        
        # Calcular el perímetro (2a + 2b)
        perimetro = 2 * a + 2 * b

        precio_aluminio_metro = precios_aluminio.get(self.tipo_de_acabado.lower(), 0)
        precio_aluminio = perimetro * precio_aluminio_metro
        return precio_aluminio

    def calcular_precio_chapas(self) -> float:
        cantidad_chapas = self.estilo.count('X')
        precio_chapa = 16200  
        return cantidad_chapas * precio_chapa

    def calcular_precio_nave(self) -> float:
        precio_esquinas = 17240 * self.cantidad_naves
        precio_vidrio = self.calcular_precio_vidrio()
        precio_aluminio = self.calcular_precio_aluminio()
        precio_chapas = self.calcular_precio_chapas()

        precio_nave = precio_vidrio + precio_aluminio + precio_chapas + precio_esquinas
        
        # Mostrar detalles
        print(f"Precio del vidrio: {precio_vidrio:.2f}")
        print(f"Precio del aluminio: {precio_aluminio:.2f}")
        print(f"Precio de las chapas: {precio_chapas:.2f}")
        print(f"Precio de las esquinas: {precio_esquinas:.2f}")
        print(f"Precio total de la nave: {precio_nave:.2f}")

        return precio_nave
