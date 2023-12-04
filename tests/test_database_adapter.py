import unittest
from app.adapters.sqlite_database_adapter import SQLiteDatabaseAdapter
from app.entities.veiculo import Veiculo
from app.infrastructure.database import create_veiculos_table
import os

class TestDatabaseAdapter(unittest.TestCase):
    def setUp(self):
        # Configurar o adaptador de banco de dados para testes
        self.database_adapter = SQLiteDatabaseAdapter(db='test.db')
        # Executar operações de configuração, como criar tabelas de teste se necessário
        create_veiculos_table()
    
    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_salvar_buscar_atualizar_remover_veiculo(self):
        # Testar salvar_veiculo, buscar_veiculo e remover_veiculo
        veiculo_teste = Veiculo(placa='NDS3536', modelo='STRADA', ano=2013)
        print('Objeto veiculo criado!')

        # Testar salvar_veiculo
        self.database_adapter.salvar_veiculo(veiculo_teste)
        print('Veículo cadastrado no banco!')

        # Testar buscar_veiculo
        veiculo_recuperado = self.database_adapter.buscar_veiculo(veiculo_teste.placa)
        self.assertIsNotNone(veiculo_recuperado)
        self.assertEqual(veiculo_recuperado.placa, veiculo_teste.placa)
        print('Encontrado veículo na busca!')

        # Testar atualizar_veiculo
        veiculo_teste.modelo = 'FIAT STRADA'
        veiculo_teste.ano = 2014
        self.database_adapter.atualizar_veiculo(veiculo_teste)
        print('Veículo editado!')

        # Buscar veículo após edição
        veiculo_editado = self.database_adapter.buscar_veiculo(veiculo_teste.placa)
        self.assertIsNotNone(veiculo_editado)
        self.assertEqual(veiculo_editado.modelo, 'FIAT STRADA')
        self.assertEqual(veiculo_editado.ano, 2014)
        print('Encontrado veículo editado na busca!')

        # Testar remover_veiculo
        self.database_adapter.remover_veiculo(veiculo_teste.placa)
        veiculo_recuperado_apos_remover = self.database_adapter.buscar_veiculo(veiculo_teste.placa)
        self.assertIsNone(veiculo_recuperado_apos_remover)
        print('Veículo removido!')

if __name__ == '__main__':
    unittest.main()
