import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.entities.motorista import Motorista

class CadastrarMotoristaUseCase:
    def cadastrar_motorista(self, nome, cpf, funcao):
        motorista = Motorista(nome, cpf, funcao)
        print('Use Case - Motorista cadastrado com sucesso!')
        # Lógica de persistência (pode ser em um banco de dados, por exemplo)
        return motorista
