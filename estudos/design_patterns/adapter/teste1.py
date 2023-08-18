class Computador:
    def __init__(self) -> None:
        pass
    
    def JogosComputador(self):
        print('Jogo: CS GO, Valor: 80,00')  

class Console:
    def __init__(self) -> None:
        pass
    
    def Jogos(self):
        print('Jogo: Sonic, Valor: 200,00')  

def func_main(obj):
    obj.Jogos()
    
class ComputadorAdapter:
    def __init__(self, computador) -> None:
        self.computador = computador

    def Jogos(self):
        self.computador.JogosComputador()
    
sonic = Console()
cs = ComputadorAdapter(Computador())
func_main(cs)
func_main()
    
    