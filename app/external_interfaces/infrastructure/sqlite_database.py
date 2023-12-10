import os
import sqlite3

class DatabaseSetup:
    def __init__(self, db_name):
        self.db_name = db_name

    def setup_database(self):
        self.create_database_if_not_exists()
        self.create_veiculos_table()
        self.create_uso_veiculo_table()
        self.create_motorista_table()
        self.create_abastecimento_table()

    def create_database_if_not_exists(self):
        if not os.path.exists(self.db_name):
            print(f'O banco de dados "{self.db_name}" não existe. Criando...')
            with sqlite3.connect(self.db_name) as conn:
                pass  # Não é necessário fazer nada aqui, pois o banco será criado automaticamente.

            print('Banco de dados criado com sucesso.')

    def create_table_if_not_exists(self, table_name, columns):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')
        except sqlite3.Error as e:
            print(f'Erro ao criar tabela {table_name}: {e}')

    def create_veiculos_table(self):
        self.create_table_if_not_exists('veiculos', 'placa TEXT PRIMARY KEY, modelo TEXT, ano INTEGER')

    def create_uso_veiculo_table(self):
        self.create_table_if_not_exists('uso_veiculos', 'veiculo_placa TEXT PRIMARY KEY, motorista_nome TEXT, '
                                                        'data_inicial DATE, data_final DATE, km_inicial REAL, km_final REAL')

    def create_motorista_table(self):
        self.create_table_if_not_exists('motoristas', 'nome TEXT, cpf TEXT PRIMARY KEY, funcao TEXT')

    def create_abastecimento_table(self):
        self.create_table_if_not_exists('abastecimentos', 'veiculo_placa TEXT PRIMARY KEY, motorista_nome TEXT, '
                                                          'data DATE, combustivel_litros REAL, custo REAL')
