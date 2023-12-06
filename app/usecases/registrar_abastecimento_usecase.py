import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.abastecimento import RegistroAbastecimento
from app.interfaces_adapters.adapters.database_adapter import IDatabaseAdapter

class RegistrarAbastecimentoUseCase:
    def __init__(self, database_adapter: IDatabaseAdapter):
        self.database_adapter = database_adapter

    def registrar_abastecimento(self, veiculo_placa, motorista_nome, data, combustivel_litros, custo):
        abastecimento = RegistroAbastecimento(veiculo_placa, motorista_nome, data, combustivel_litros, custo)
        self.database_adapter.salvar_entidade('abastecimentos', veiculo_placa=abastecimento.veiculo_placa, motorista_nome=abastecimento.motorista_nome, data=abastecimento.data, combustivel_litros=abastecimento.combustivel_litros, custo=abastecimento.custo)
        # print('Use Case - Registo de abastecimento cadastrado com sucesso!')
        return abastecimento
