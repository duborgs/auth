from typing import Type

class Casa:

    def __init__(self) -> None:
        self._endereco = 'Rua dos Limoeiros'
        
    def acender_luzes(self) -> None:
        print('Estou acendendo as Luzes')
        
    def get_endereco(self) -> str:
        return self._endereco
    
class Pessoa: 
    
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self._nome = nome 
        self._local = local
    def entrar_no_local(self) -> None:
        self._local.acender_luzes()
        
    def apresentar_local(self) -> None:
        endereco = self._local.get_endereco()
        print(endereco)
        
casa_de_amigo = Casa()
ana = Pessoa('Ana', casa_de_amigo)

ana.entrar_no_local()
ana.apresentar_local()