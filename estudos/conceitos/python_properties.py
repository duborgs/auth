class Casa:
    def __init__(self, preco, tipo) -> None:
        self.__preco = preco
        self.tipo = tipo
        
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0 and isinstance(novo_preco, float):
            self.__preco = novo_preco
        else:
            print("Insira um preço válido")

    @preco.deleter
    def preco(self):
        del self.__preco
    
mansao = Casa(10000000, 'Mansao')
        

  

  
