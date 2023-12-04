class SistemaControleVeiculos:

    def criar_tabelas(self):
        pass

    def cadastrar_veiculo(self, modelo : str, ano : int, placa : str):
        print('Veículo cadastrado com Sucesso!')

    def cadastrar_uso_veiculo(self, placa : str, motorista : str, data_inicial : str, data_final : str, km_inicial : float, km_final : float):
        print('')

    def cadastrar_abastecimento(self, placa : str, motorista : str, data : str, combustivel_litros : float, custo : float):
        pass

    def consultar_veiculo(self, placa : str):
        pass

    def consultar_uso_veiculo(self, placa : str = None, motorista : str = None, data_inicial : str = None, data_final : str = None):
        pass

    def consultar_abastecimento(self, placa : str):
        pass