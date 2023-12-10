import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos")

from app.external_interfaces.infrastructure.sqlite_database import DatabaseSetup
from app.interfaces_adapters.adapters.sqlite_database_adapter import SQLiteDatabaseAdapter
from app.interfaces_adapters.controllers.veiculo_controller import VeiculoController
from app.interfaces_adapters.controllers.motorista_controller import MotoristaController
from app.interfaces_adapters.controllers.uso_veiculo_controller import UsoVeiculoController
from app.interfaces_adapters.controllers.abastecimento_controller import AbastecimentoController

import os

# Configuração inicial do banco de dados
db_name = 'controle_veiculos.db'
db_setup = DatabaseSetup(db_name)
db_setup.setup_database()

# Crie uma instância do adaptador SQLite
sqlite_adapter = SQLiteDatabaseAdapter()

# Restante da inicialização do seu aplicativo
veiculo_controller = VeiculoController()
motorista_controller = MotoristaController()
uso_veiculo_controller = UsoVeiculoController()
abastecimento_controller = AbastecimentoController()

def exibir_menu_principal():
    print('----Sistema de controle de veículo----')
    print('1 - Veículo')
    print('2 - Motorista')
    print('3 - Uso de Veículo')
    print('4 - Abastecimento')

def exibir_menu(menu_nome):
    print(f'----Sistema de controle de veículo----')
    print(f'----Menu {menu_nome}----')

def escolher_opcao():
    return int(input('Escolha a opção desejada: '))

# Cadastro de entidade
def cadastro_veiculo():
    placa = str(input('Digite a placa do veículo: '))
    modelo = str(input('Digite o modelo do veículo: '))
    ano = int(input('Digite o ano do veículo: '))
    veiculo_controller.cadastrar_veiculo(placa, modelo, ano)
    print('Veículo cadastrado no banco!')
    os.system('cls')

def cadastro_motorista():
    nome = str(input('Digite o nome do motorista: '))
    cpf = str(input('Digite o CPF do motorista: '))
    funcao = str(input('Digite a função do motorista: '))
    motorista_controller.cadastrar_motorista(nome, cpf, funcao)
    print('Motorista cadastrado no banco!')
    os.system('cls')
    
def cadastro_registro_uso():
    veiculo_placa = str(input('Digite a placa do veículo: '))
    motorista_nome = str(input('Digite o nome do motorista: '))
    data_inicial = str(input('Digite a data de saída do veículo: '))
    data_final = str(input('Digite a data de volta do veículo: '))
    km_inicial = float(input('Digite a km de saída do véiculo: '))
    km_final = float(input('Digite a km de volta do veículo: '))
    uso_veiculo_controller.registrar_uso(veiculo_placa, motorista_nome, data_inicial, data_final, km_inicial, km_final)
    print('Uso do Veículo cadastrado no banco!')
    os.system('cls')

def cadastro_registro_abastecimento():
    veiculo_placa = str(input('Digite a placa do veículo: '))
    motorista_nome = str(input('Digite o nome do motorista: '))
    data = str(input('Digite a data do abastecimento do veículo: '))
    combustivel_litros = float(input('Digite quantos litros colocou no veículo: '))
    custo = float(input('Digite o valor do abastecimento do veículo: '))
    abastecimento_controller.registrar_abastecimento(veiculo_placa, motorista_nome, data, combustivel_litros, custo)
    print('Abastecimento do Veículo cadastrado no banco!')
    os.system('cls')

# Cadastro de entidade
def buscar_veiculo():
    veiculo_placa = str(input('Digite a placa do veículo: '))
    # veiculo_recuperado = self.database_adapter.buscar_entidade('veiculos', 'placa', veiculo_teste.placa)
    pass

def menu_principal():
    exibir_menu_principal()
    opcao = escolher_opcao()

    while opcao != 0:
        os.system('cls')

        if opcao == 1:
            exibir_menu('Veículos')
            cadastro_veiculo()
        elif opcao == 2:
            exibir_menu('Motoristas')
            cadastro_motorista()
        elif opcao == 3:
            exibir_menu('Uso de Veículos')
            cadastro_registro_uso()
        elif opcao == 4:
            exibir_menu('Abastecimentos')
            cadastro_registro_abastecimento()
        else:
            print('Opção inválida')

        exibir_menu_principal()
        opcao = escolher_opcao()

    print('Saindo do programa. Até mais!')

# Chame a função para iniciar o loop do menu principal
menu_principal()


