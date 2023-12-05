import sqlite3

def setup_database():
    create_veiculos_table()

def create_veiculos_table():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS veiculos (
                placa TEXT PRIMARY KEY,
                modelo TEXT,
                ano INTEGER
            )
        ''')

        conn.commit()

    except sqlite3.Error as e:
        print(f'Erro ao criar tabela de veículos: {e}')

    finally:
        conn.close()

def create_uso_veiculo_table():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS uso_veiculo (
                veiculo_placa TEXT PRIMARY KEY,
                motorista_nome TEXT,
                data_inicial DATE,
                data_final DATE, 
                km_inicial REAL,
                km_final REAL
            )
                       ''')
    
    except sqlite3.Error as e:
        print(f'Erro ao criar tabela de uso de veículos: {e}')

    finally:
        conn.close()

def create_motorista_table():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS motoristas (
                nome TEXT,
                cpf TEXT PRIMARY KEY,
                funcao TEXT
            )
                       ''')
    
    except sqlite3.Error as e:
        print(f'Erro ao criar tabela de uso de veículos: {e}')

    finally:
        conn.close()

def create_abastecimento_table():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS abastecimentos (
                veiculo_placa TEXT PRIMARY KEY,
                motorista_nome TEXT,
                data DATE,
                combustivel_litros REAL,
                custo REAL
            )
                       ''')
    
    except sqlite3.Error as e:
        print(f'Erro ao criar tabela de abastecimentos: {e}')

    finally:
        conn.close()