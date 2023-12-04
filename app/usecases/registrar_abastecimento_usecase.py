import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.abastecimento import RegistroAbastecimento

class RegistrarAbastecimentoUseCase:
    def registrar_abastecimento(self, veiculo, motorista, data, combustivel_litros, custo):
        abastecimento = RegistroAbastecimento(veiculo, motorista, data, combustivel_litros, custo)
        print('Use Case - Registo de abastecimento cadastrado com sucesso!')
        # Lógica de persistência (pode ser em um banco de dados, por exemplo)
        return abastecimento