import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

import unittest
from app.controllers.motorista_controller import MotoristaController


class TestCadastrarMotorista(unittest.TestCase):
    def test_cadastrar_motorista(self):
        cadastrar_motorista_controller = MotoristaController()

        # Dados fictícios
        nome = "Guilherme Carvalho"
        cpf = "02129796206"
        funcao = 'Dev'

        # Executar o caso de uso
        motorista = cadastrar_motorista_controller.cadastrar_motorista(nome, cpf, funcao)

        # Verificar se o motorista foi criado corretamente
        self.assertEqual(motorista.nome, nome)
        self.assertEqual(motorista.cpf, cpf)
        self.assertEqual(motorista.funcao, funcao)

if __name__ == '__main__':
    unittest.main()
