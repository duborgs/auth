from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Eduardo')

terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(10, 20)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_area(terrenoRetangular)