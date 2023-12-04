import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

import unittest
from app.controllers.veiculo_controller import VeiculoController

class TestCadastrarVeiculo(unittest.TestCase):
    def test_cadastrar_veiculo(self):
        cadastrar_veiculo_controller = VeiculoController()

        # Dados fictícios
        placa = "NDS3536"
        modelo = "STRADA"
        ano = 2014

        # Executar o caso de uso
        veiculo = cadastrar_veiculo_controller.cadastrar_veiculo(placa, modelo, ano)

        # Verificar se o veículo foi criado corretamente
        self.assertEqual(veiculo.placa, placa)
        self.assertEqual(veiculo.modelo, modelo)
        self.assertEqual(veiculo.ano, ano)

if __name__ == '__main__':
    unittest.main()
