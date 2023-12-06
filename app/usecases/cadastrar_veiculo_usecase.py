import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.veiculo import Veiculo
from app.interfaces_adapters.adapters.database_adapter import IDatabaseAdapter

class CadastrarVeiculoUseCase:
    def __init__(self, database_adapter: IDatabaseAdapter):
        self.database_adapter = database_adapter

    def cadastrar_veiculo(self, placa, modelo, ano):
        veiculo = Veiculo(placa, modelo, ano)
        self.database_adapter.salvar_entidade('veiculos', placa=veiculo.placa, modelo=veiculo.modelo, ano=veiculo.ano)
        # print('Use Case - Veículo cadastrado com sucesso!')
        return veiculo
