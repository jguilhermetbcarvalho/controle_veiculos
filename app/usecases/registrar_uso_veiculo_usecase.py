import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.resgistro_uso import RegistroUso

class RegistrarUsoVeiculoUseCase:
    def registrar_uso(self, veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final):
        registro_uso = RegistroUso(veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final)
        print('Use Case - Registro de uso do veículo cadastrado com sucesso!')
        # Lógica de persistência (pode ser em um banco de dados, por exemplo)
        return registro_uso
