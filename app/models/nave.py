class Nave:
    """
    Representa una nave (panel) en una ventana.
    
    Atributos:
        tipo (str): Tipo de nave (O o X).
        ancho (float): Ancho de la nave.
        alto (float): Alto de la nave.
        vidrio (Vidrio): Tipo de vidrio asociado a la nave.
        acabado (Acabado): Tipo de acabado asociado a la nave.
        esmerilado (bool): Indica si el vidrio es esmerilado.
    """
    
    def __init__(self, tipo, ancho, alto, vidrio, acabado, esmerilado=False):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        self.vidrio = vidrio
        self.acabado = acabado
        self.esmerilado = esmerilado

    def calcular_area_vidrio(self):
        """Calcula el área del vidrio, restando los márgenes de 1.5 cm."""
        return (self.ancho - 3) * (self.alto - 3)

    def calcular_costo(self):
        """Calcula el costo de la nave basado en el aluminio y el vidrio."""
        metros_lineales_aluminio = 2 * (self.ancho + self.alto)
        costo_acabado = metros_lineales_aluminio * self.acabado.precio_por_metro_lineal
        area_vidrio = self.calcular_area_vidrio()
        costo_vidrio = area_vidrio * self.vidrio.precio_por_cm2
        
        if self.esmerilado:
            costo_vidrio += area_vidrio * 5.20  # Costo adicional por esmerilado
        
        return costo_acabado + costo_vidrio

    def __str__(self):
        return f"Nave {self.tipo} - {self.ancho}x{self.alto} cm"