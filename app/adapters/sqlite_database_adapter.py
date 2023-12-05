import sqlite3
from adapters.database_adapter import IDatabaseAdapter
from entities.veiculo import Veiculo
from entities.motorista import Motorista
from entities.abastecimento import RegistroAbastecimento
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

    def atualizar_entidade(self, tabela, chave_primaria, **dados):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            
            # Montar a string de colunas e valores dinamicamente
            colunas_valores = ', '.join([f"{coluna} = ?" for coluna in dados.keys()])

            # Executar a atualizaç da entidade
            cursor.execute(f'UPDATE {tabela} SET {colunas_valores} WHERE {chave_primaria} = ?', tuple(dados.values()) + (dados['placa'],))

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
            
            if resultado:
                if f'{tabela}' == 'veiculos':
                    # Criar uma instância de Veiculo com os dados encontrados no banco de dados
                    veiculo_encontrado = Veiculo(placa=resultado[0], modelo=resultado[1], ano=resultado[2])
                    return veiculo_encontrado
                if f'{tabela}' == 'motoristas':
                    # Criar uma instância de Motorista com os dados encontrados no banco de dados
                    motorista_encontrado = Motorista(nome=resultado[0], cpf=resultado[1], funcao=resultado[2])
                    return motorista_encontrado
                if f'{tabela}' == 'abastecimento':
                    # Criar uma instância de Abastecimento com os dados encontrados no banco de dados
                    abastecimento_encontrado = RegistroAbastecimento(veiculo=resultado[0], motorista=resultado[1], data=resultado[2], combustivel_litros=resultado[3], custo=resultado[4])
                    return abastecimento_encontrado

            else:
                # Retornar None se nenhuma entidade foi encontrado
                return None


            return resultado

        except sqlite3.Error as e:
            print(f'Erro ao buscar entidade: {e}')

        finally:
            conn.close()

   