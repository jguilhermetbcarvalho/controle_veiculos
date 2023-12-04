import sqlite3
from datetime import datetime

class SistemaControleVeiculos:
    def __init__(self, db_path="controle_veiculos.db"):
        self.db_path = db_path
        self.criar_tabelas()

    def criar_tabelas(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS veiculos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    modelo TEXT
                    ano INTEGER,
                    placa TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS registros_uso (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    veiculo_id INTEGER,
                    motorista TEXT,
                    data_inicial TEXT,
                    data_final TEXT,
                    km_inicial INTEGER,
                    km_final INTEGER,
                    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS registros_abastecimento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    veiculo_id INTEGER,
                    motorista TEXT,
                    data TEXT,
                    combustivel_litros REAL,
                    custo REAL,
                    km_abastecimento REAL,
                    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
                )
            ''')

    def cadastrar_veiculo(self, modelo, marca, ano, placa, chassi):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO veiculos (modelo, marca, ano, placa, chassi)
                VALUES (?, ?, ?, ?, ?)
            ''', (modelo, marca, ano, placa, chassi))
        print(f"Veículo {modelo} cadastrado com sucesso.")

    def cadastrar_uso_veiculo(self, veiculo_id, motorista, data, km_inicial, km_final):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO registros_uso (veiculo_id, motorista, data, km_inicial, km_final)
                VALUES (?, ?, ?, ?, ?)
            ''', (veiculo_id, motorista, data, km_inicial, km_final))
        print(f"Registro de uso cadastrado para o veículo ID {veiculo_id}.")

    def cadastrar_abastecimento(self, veiculo_id, data, combustivel_litros, custo):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO registros_abastecimento (veiculo_id, data, combustivel_litros, custo)
                VALUES (?, ?, ?, ?)
            ''', (veiculo_id, data, combustivel_litros, custo))
        print(f"Registro de abastecimento cadastrado para o veículo ID {veiculo_id}.")
