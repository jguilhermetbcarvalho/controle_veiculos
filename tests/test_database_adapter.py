import unittest
from app.adapters.sqlite_database_adapter import SQLiteDatabaseAdapter
from app.entities.veiculo import Veiculo
from app.infrastructure.sqlite_database import create_veiculos_table
import os

class TestDatabaseAdapter(unittest.TestCase):
    def setUp(self):
        self.database_adapter = SQLiteDatabaseAdapter(db='test.db')
        create_veiculos_table()
    
    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_salvar_entidade(self):
        # Testar salvar_entidade, atualizar_entidade, buscar_entidade e remover_entidade
        veiculo_teste = Veiculo(placa='NDS3536', modelo='STRADA', ano=2013)
        print('Objeto veiculo criado!')

        # Testar salvar_entidade
        self.database_adapter.salvar_entidade('veiculos', placa=veiculo_teste.placa, modelo=veiculo_teste.modelo, ano=veiculo_teste.ano)
        print('Veículo cadastrado no banco!')

        # Teste atualizar_entidade
        veiculo_teste.modelo = 'FIAT STRADA'
        veiculo_teste.ano = 2014
        self.database_adapter.atualizar_entidade('veiculos', 'placa', placa=veiculo_teste.placa, modelo=veiculo_teste.modelo, ano=veiculo_teste.ano)
        print('Veículo editado!')

        # Testar buscar_veiculo
        veiculo_recuperado = self.database_adapter.buscar_entidade('veiculos', 'placa', veiculo_teste.placa)
        self.assertIsNotNone(veiculo_recuperado)
        self.assertEqual(veiculo_recuperado.placa, veiculo_teste.placa)
        print('Encontrado veículo na busca!')

        # Testar remover_entidade
        self.database_adapter.remover_entidade('veiculos', 'placa', veiculo_teste.placa)
        print('Veículo removido!')

if __name__ == '__main__':
    unittest.main()
