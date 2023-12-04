import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos\app")

import unittest
from app.controllers.uso_veiculo_controller import UsoVeiculoController
from app.entities.veiculo import Veiculo
from app.entities.motorista import Motorista

class TestRegistrarUsoVeiculo(unittest.TestCase):
    def test_registrar_uso_veiculo(self):
        registrar_uso_veiculo_controller = UsoVeiculoController()

        # Dados fictícios
        veiculo = Veiculo("NDS3536", "STRADA", 2014)
        motorista = Motorista('Guilherme', '02129796206', 'Dev')
        data_inicial = '04/12/2023'
        data_final = '04/12/2023'
        km_inicial = 100
        km_final = 200

        # Executar o caso de uso
        registro_uso = registrar_uso_veiculo_controller.registrar_uso(veiculo, motorista, data_inicial, data_final, km_inicial, km_final)

        # Verificar se o registro de uso foi criado corretamente
        self.assertEqual(registro_uso.veiculo, veiculo)
        self.assertEqual(registro_uso.motorista, motorista)
        self.assertEqual(registro_uso.data_inicial, data_inicial)
        self.assertEqual(registro_uso.data_final, data_final)
        self.assertEqual(registro_uso.km_inicial, km_inicial)
        self.assertEqual(registro_uso.km_final, km_final)

if __name__ == '__main__':
    unittest.main()
