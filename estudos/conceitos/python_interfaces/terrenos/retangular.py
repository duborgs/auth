from interfaces.formas import FormasInterfaces

class TerrenoRetangular(FormasInterfaces):
    
    def __init__(self, largura, comprimento) -> None:
        self.largura = largura
        self.comprimento = comprimento
        
    def get_perimetro(self) -> int:
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro
    
    def get_area(self) -> int:
        area = self.largura * self.comprimento
        return area
    
    