import sqlite3
from adapters.database_adapter import IDatabaseAdapter
from entities.veiculo import Veiculo

class SQLiteDatabaseAdapter(IDatabaseAdapter):
    def __init__(self, db='controle_veiculos.db'):
        self.db = db

    def salvar_veiculo(self, veiculo: Veiculo) -> None:
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO veiculos (placa, modelo, ano) VALUES (?, ?, ?)',
                           (veiculo.placa, veiculo.modelo, veiculo.ano))
            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao persistir veículo: {e}')

        finally:
            conn.close()

    def buscar_veiculo(self, placa: str) -> Veiculo:
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            # Executar uma instrução SQL para buscar o veículo com base na placa
            cursor.execute('SELECT * FROM veiculos WHERE placa = ?', (placa,))
            
            # Recuperar os resultados da consulta
            resultado = cursor.fetchone()

            if resultado:
                # Criar uma instância de Veiculo com os dados encontrados no banco de dados
                veiculo_encontrado = Veiculo(placa=resultado[0], modelo=resultado[1], ano=resultado[2])
                return veiculo_encontrado
            else:
                # Retornar None se nenhum veículo foi encontrado
                return None

        except sqlite3.Error as e:
            print(f'Erro ao buscar veículo: {e}')
            # Retornar None em caso de erro
            return None

        finally:
            conn.close()

    def atualizar_veiculo(self, veiculo: Veiculo) -> None:
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            # Executar uma instrução SQL para atualizar o veículo com base na placa
            cursor.execute('''
                UPDATE veiculos
                SET modelo = ?, ano = ?
                WHERE placa = ?
            ''', (veiculo.modelo, veiculo.ano, veiculo.placa))
            
            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao editar veículo: {e}')

        finally:
            conn.close()

    def remover_veiculo(self, placa: str) -> None:
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            # Executar uma instrução SQL para remover o veículo com base na placa
            cursor.execute('DELETE FROM veiculos WHERE placa = ?', (placa,))
            
            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao remover veículo: {e}')

        finally:
            conn.close()


