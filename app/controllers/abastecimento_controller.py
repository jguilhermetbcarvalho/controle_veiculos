import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.usecases.registrar_abastecimento_usecase import RegistrarAbastecimentoUseCase

class AbastecimentoController:
    def __init__(self):
        self.registrar_abastecimento_use_case = RegistrarAbastecimentoUseCase()

    def registrar_abastecimento(self, veiculo_placa, motorista_nome, data, combustivel_litros, custo):
        abastecimento = self.registrar_abastecimento_use_case.registrar_abastecimento(veiculo_placa, motorista_nome, data, combustivel_litros, custo)
        print('Controller - Registo de abastecimento cadastrado com sucesso!')
        return abastecimento
