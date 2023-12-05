import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

from app.usecases.cadastrar_motorista_usecase import CadastrarMotoristaUseCase

class MotoristaController:
    def __init__(self):
        self.cadastrar_motorista_use_case = CadastrarMotoristaUseCase()

    def cadastrar_motorista(self, nome, cpf, funcao):
        motorista = self.cadastrar_motorista_use_case.cadastrar_motorista(nome, cpf, funcao)
        print('Controller - Motorista cadastrado com sucesso!')
        return motorista
