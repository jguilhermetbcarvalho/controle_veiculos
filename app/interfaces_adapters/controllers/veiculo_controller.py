import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.usecases.cadastrar_veiculo_usecase import CadastrarVeiculoUseCase

class VeiculoController:
    def __init__(self):
        self.cadastrar_veiculo_use_case = CadastrarVeiculoUseCase()

    def cadastrar_veiculo(self, placa, modelo, ano):
        veiculo = self.cadastrar_veiculo_use_case.cadastrar_veiculo(placa, modelo, ano)
        print('Controller - Veículo cadastrado com sucesso!')
        return veiculo
