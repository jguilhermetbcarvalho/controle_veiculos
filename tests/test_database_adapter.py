import unittest
from app.adapters.sqlite_database_adapter import SQLiteDatabaseAdapter
from app.entities.veiculo import Veiculo
from app.entities.resgistro_uso import RegistroUso
from app.entities.motorista import Motorista
from app.entities.abastecimento import RegistroAbastecimento
from app.infrastructure.sqlite_database import create_veiculos_table, create_motorista_table, create_uso_veiculo_table, create_abastecimento_table
import os

class TestDatabaseAdapter(unittest.TestCase):
    def setUp(self):
        self.database_adapter = SQLiteDatabaseAdapter(db='test.db')
        create_veiculos_table()
        create_uso_veiculo_table()
        create_motorista_table()
        create_abastecimento_table()
    
    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_salvar_entidade(self):
        # Testar salvar_entidade, atualizar_entidade, buscar_entidade e remover_entidade
        veiculo_teste = Veiculo(placa='NDS3536', modelo='STRADA', ano=2013)
        print('Objeto Veículo criado!')

        motorista_teste = Motorista('Guilherme', '02129796206', 'Dev')
        print('Objeto Motorista criado!')

        uso_veiculo_teste = RegistroUso(veiculo_teste.placa, motorista_teste.nome, '05/12/2023', '05/12/2023', 100, 200)
        print('Objeto Registro Uso criado!')

        abastecimento_teste = RegistroAbastecimento(veiculo_teste.placa, motorista_teste.nome, '05/12/2023', 44.52, 288.45)
        print('Objeto Registro Abastecimento criado!')
        
        # Testar salvar_entidade
        self.database_adapter.salvar_entidade('veiculos', placa=veiculo_teste.placa, modelo=veiculo_teste.modelo, ano=veiculo_teste.ano)
        print('Veículo cadastrado no banco!')

        self.database_adapter.salvar_entidade('motoristas', nome=motorista_teste.nome, cpf=motorista_teste.cpf, funcao=motorista_teste.funcao)
        print('Motorista cadastrado no banco!')

        self.database_adapter.salvar_entidade('uso_veiculo', veiculo_placa=uso_veiculo_teste.veiculo_placa, motorista_nome=uso_veiculo_teste.motorista_nome, data_inicial=uso_veiculo_teste.data_inicial, data_final=uso_veiculo_teste.data_final, km_inicial=uso_veiculo_teste.km_inicial, km_final=uso_veiculo_teste.km_final)
        print('Registro de uso de veículo cadastrado no banco!')

        self.database_adapter.salvar_entidade('abastecimentos', veiculo_placa=abastecimento_teste.veiculo_placa, motorista_nome=abastecimento_teste.motorista_nome, data=abastecimento_teste.data, combustivel_litros=abastecimento_teste.combustivel_litros, custo=abastecimento_teste.custo)
        print('Registro de abastecimento de veículo cadastrado no banco!')

        # Teste atualizar_entidade
        veiculo_teste.modelo = 'FIAT STRADA'
        veiculo_teste.ano = 2014
        self.database_adapter.atualizar_entidade('veiculos', 'placa', veiculo_teste.placa, modelo=veiculo_teste.modelo, ano=veiculo_teste.ano)
        print('Veículo editado no banco!')

        motorista_teste.funcao = 'Desenvolvedor'
        self.database_adapter.atualizar_entidade('motoristas', 'cpf', motorista_teste.cpf, funcao=motorista_teste.funcao)
        print('Motorista editado no banco!')

        uso_veiculo_teste.motorista_nome = 'Guilherme Carvalho'
        self.database_adapter.atualizar_entidade('uso_veiculo', 'veiculo_placa', uso_veiculo_teste.veiculo_placa, motorista_nome=uso_veiculo_teste.motorista_nome)
        print('Uso de veículo editado no banco!')

        abastecimento_teste.combustivel_litros = 45.82
        self.database_adapter.atualizar_entidade('abastecimentos', 'veiculo_placa', str(abastecimento_teste.veiculo_placa), combustivel_litros=abastecimento_teste.combustivel_litros)
        print('Abastecimento editado no banco!')

        # Testar buscar_veiculo
        veiculo_recuperado = self.database_adapter.buscar_entidade('veiculos', 'placa', veiculo_teste.placa)
        self.assertIsNotNone(veiculo_recuperado)
        self.assertEqual(veiculo_recuperado.placa, veiculo_teste.placa)
        print('Veículo encontrado no banco!')

        motorista_recuperado = self.database_adapter.buscar_entidade('motoristas', 'cpf', motorista_teste.cpf)
        self.assertIsNotNone(motorista_recuperado)
        self.assertEqual(motorista_recuperado.cpf, motorista_teste.cpf)
        print('Motorista encontrado no banco!')

        uso_veiculo_recuperado = self.database_adapter.buscar_entidade('uso_veiculo', 'veiculo_placa', uso_veiculo_teste.veiculo_placa)
        self.assertIsNotNone(uso_veiculo_recuperado)
        self.assertEqual(uso_veiculo_recuperado.veiculo_placa, uso_veiculo_teste.veiculo_placa)
        print('Registro de uso de veículo encontrado no banco!')

        abastecimento_recuperado = self.database_adapter.buscar_entidade('abastecimentos', 'veiculo_placa', abastecimento_teste.veiculo_placa)
        self.assertIsNotNone(abastecimento_recuperado)
        self.assertEqual(abastecimento_recuperado.veiculo_placa, abastecimento_teste.veiculo_placa)
        print('Registro de abastecimento de veículo encontrado no banco!')

        # Testar remover_entidade
        self.database_adapter.remover_entidade('veiculos', 'placa', veiculo_teste.placa)
        print('Veículo removido!')

        self.database_adapter.remover_entidade('motoristas', 'cpf', motorista_teste.cpf)
        print('Motorista removido!')

        self.database_adapter.remover_entidade('uso_veiculo', 'veiculo_placa', uso_veiculo_teste.veiculo_placa)
        print('Registro de uso de veículo removido!')

        self.database_adapter.remover_entidade('abastecimentos', 'veiculo_placa', abastecimento_teste.veiculo_placa)
        print('Registro de abastecimento de veículo removido!')

if __name__ == '__main__':
    unittest.main()
