from typing import Type
from interfaces.formas import FormasInterfaces

class Engenheiro:
    
    def __init__(self, nome: str) -> None:
        self.nome = nome
        
    def medir_perimetro(self, terreno: Type[FormasInterfaces]):
        perimetro = terreno.get_perimetro()
        print('{} mediu o perimetro: {} m'.format(self.nome, perimetro))
        pass
    
    def medir_area(self, terreno: Type[FormasInterfaces]):
        area = terreno.get_perimetro()
        print('{} mediu o perimetro: {} m'.format(self.nome, area))
        pass