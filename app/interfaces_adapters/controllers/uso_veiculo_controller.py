import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.usecases.registrar_uso_veiculo_usecase import RegistrarUsoVeiculoUseCase

class UsoVeiculoController:
    def __init__(self):
        self.registrar_uso_veiculo_use_case = RegistrarUsoVeiculoUseCase()

    def registrar_uso(self, veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final):
        registro_uso = self.registrar_uso_veiculo_use_case.registrar_uso(veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final)
        print('Controller - Registro de uso do veículo cadastrado com sucesso!')
        return registro_uso
