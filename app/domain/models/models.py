class Veiculo:
    def __init__(self, modelo : str, ano : int, placa : str):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

class RegistroUso:
    def __init__(self, placa : str, motorista : str, data_inicial : str, data_final : str, km_inicial : float, km_final : float):
        self.placa = placa
        self.motorista = motorista
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.km_inicial = km_inicial
        self.km_final = km_final

class RegistroAbastecimento:
    def __init__(self, placa : str, motorista : str, data : str, combustivel_litros : float, custo : float):
        self.placa = placa
        self.motorista = motorista
        self.data = data
        self.combustivel_litros = combustivel_litros
        self.custo = custo
