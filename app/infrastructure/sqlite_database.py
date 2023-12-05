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

# def create_uso_veiculo_table():
#     try:
#         conn = sqlite3.connect('test.db')
#         cursor = conn.cursor()

#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS uso_veiculo (
                       
#             )
#                        ''')
