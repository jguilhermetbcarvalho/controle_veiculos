import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.motorista import Motorista
from app.interfaces_adapters.adapters.database_adapter import IDatabaseAdapter

class CadastrarMotoristaUseCase:
    def __init__(self, database_adapter: IDatabaseAdapter):
        self.database_adapter = database_adapter

    def cadastrar_motorista(self, nome, cpf, funcao):
        motorista = Motorista(nome, cpf, funcao)
        self.database_adapter.salvar_entidade('motoristas', nome=motorista.nome, cpf=motorista.cpf, funcao=motorista.funcao)
        # print('Use Case - Motorista cadastrado com sucesso!')
        return motorista
