import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.resgistro_uso import RegistroUso
from app.interfaces_adapters.adapters.database_adapter import IDatabaseAdapter

class RegistrarUsoVeiculoUseCase:
    def __init__(self, database_adapter: IDatabaseAdapter):
        self.database_adapter = database_adapter

    def registrar_uso(self, veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final):
        registro_uso = RegistroUso(veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final)
        self.database_adapter.salvar_entidade('uso_veiculos', veiculo_placa=registro_uso.veiculo_placa, motorista_nome=registro_uso.motorista_nome, data_inicial=registro_uso.data_inicial, data_final=registro_uso.data_final, km_inicial=registro_uso.km_inicial, km_final=registro_uso.km_final)
        # print('Use Case - Registro de uso do veículo cadastrado com sucesso!')
        return registro_uso
