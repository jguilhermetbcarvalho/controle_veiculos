import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

import unittest
from app.controllers.abastecimento_controller import AbastecimentoController
from app.entities.veiculo import Veiculo
from app.entities.motorista import Motorista

class TestRegistrarAbastecimento(unittest.TestCase):
    def test_registrar_abastecimento(self):
        abastecimento_controller = AbastecimentoController()

        # Dados fictícios
        veiculo = Veiculo("NDS3536", "STRADA", 2014)
        motorista = Motorista('Guilherme', '02129796206', 'Dev')
        data = "24/12/2023"
        combustivel_litros = 44
        custo = 288

        # Executar o caso de uso
        abastecimento = abastecimento_controller.registrar_abastecimento(veiculo.placa, motorista.nome, data, combustivel_litros, custo)

        # Verificar se o abastecimento foi registrado corretamente
        self.assertEqual(abastecimento.veiculo_placa, veiculo.placa)
        self.assertEqual(abastecimento.motorista_nome, motorista.nome)
        self.assertEqual(abastecimento.data, data)
        self.assertEqual(abastecimento.combustivel_litros, combustivel_litros)
        self.assertEqual(abastecimento.custo, custo)

if __name__ == '__main__':
    unittest.main()



