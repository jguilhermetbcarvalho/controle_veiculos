import sqlite3
from app.interfaces_adapters.adapters.database_adapter import IDatabaseAdapter
from app.entities.veiculo import Veiculo
from app.entities.motorista import Motorista
from app.entities.abastecimento import RegistroAbastecimento
from app.entities.resgistro_uso import RegistroUso
class SQLiteDatabaseAdapter(IDatabaseAdapter):
    def __init__(self, db='controle_veiculos.db'):
        self.db = db

    def salvar_entidade(self, tabela, **dados):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            # Montar a string de colunas e valores dinamicamente
            colunas = ', '.join(dados.keys())
            valores = ', '.join(['?' for _ in dados.values()])

            # Executar a inserção da entidade
            cursor.execute(f'INSERT INTO {tabela} ({colunas}) VALUES ({valores})', tuple(dados.values()))

            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao salvar entidade: {e}')

        finally:
            conn.close()

    def atualizar_entidade(self, tabela, chave_primaria, valor_chave_primaria, **dados):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            
            # Montar a string de colunas e valores dinamicamente
            colunas_valores = ', '.join([f"{coluna} = ?" for coluna in dados.keys()])

            # Executar a atualização da entidade
            cursor.execute(f'UPDATE {tabela} SET {colunas_valores} WHERE {chave_primaria} = ?', tuple(dados.values()) + (valor_chave_primaria,))

            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao atualizar entidade: {e}')

        finally:
            conn.close()

    def remover_entidade(self, tabela, chave_primaria, identificador):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            cursor.execute(f'DELETE FROM {tabela} WHERE {chave_primaria} = ?', (identificador,))

            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao remover entidade: {e}')

        finally:
            conn.close()

    def buscar_entidade(self, tabela, chave_primaria, identificador):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()

            cursor.execute(f'SELECT * FROM {tabela} WHERE {chave_primaria} = ?', (identificador,))
            resultado = cursor.fetchone()

            return self.mapear_entidade(tabela, resultado)

        except sqlite3.Error as e:
            print(f'Erro ao buscar entidade: {e}')

        finally:
            conn.close()

    def mapear_entidade(self, tabela, resultado):
        if resultado:
            classes_por_tabela = {
                'veiculos': Veiculo,
                'motoristas': Motorista,
                'abastecimentos': RegistroAbastecimento,
                'uso_veiculo' : RegistroUso,
            }

            classe_entidade = classes_por_tabela.get(tabela)

            if classe_entidade:
                entidade_encontrada = classe_entidade(*resultado)
                return entidade_encontrada

        return None
   