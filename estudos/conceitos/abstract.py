from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    _numero = "00000"
    _titular = "root"
    saldo = 0

    @abstractmethod
    def __init__(self, numero: str, titular: str, saldo: float):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, value: float):
        pass

    @abstractmethod
    def depositar(self, value: float):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass
    
class Poupanca(Conta):
    def __init__(self, numero: str, titular: str, saldo: float):
        super().__init__(numero, titular, saldo)
    
    def sacar(self, value: float):
        pass
    
    def depositar(self, value: float):
        pass

    def exibir_saldo(self):
        print(self._numero)
    
poup = Poupanca('0000', 'Eduardo', 0.0)
poup.exibir_saldo()