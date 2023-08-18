class Funcionario:
    def __init__(self, nome, cpf, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10
    
class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self.qtd_gerenciaveis = qtd_gerenciaveis
        
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.0

class ControleDeBonificacoes():
    def __init__(self, total_bonificacoes=0) -> None:
        self._total_bonificacoes = total_bonificacoes
        
    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))  
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes 
    
if __name__ == '__main__':
    funcionario = Funcionario('João', '111111111-11', 2000.0)
    print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))

    gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    print("bonificacao gerente: {}".format(gerente.get_bonificacao()))
    
    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    
    print("total: {}".format(controle.total_bonificacoes))