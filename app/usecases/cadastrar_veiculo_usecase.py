import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.veiculo import Veiculo

class CadastrarVeiculoUseCase:
    def cadastrar_veiculo(self, placa, modelo, ano):
        veiculo = Veiculo(placa, modelo, ano)
        print('Use Case - Veículo cadastrado com sucesso!')
        # Lógica de persistência (pode ser em um banco de dados, por exemplo)
        return veiculo
