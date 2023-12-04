import pytest
import sys
sys.path.append(r"C:\Users\joaog\Documents\controle_veiculos")

from app.domain.models import Veiculo, RegistroUso, RegistroAbastecimento

def test_veiculo():
    result = Veiculo('FIAT STRADA', 2014, 'NDS3536')
    assert result.__dict__ == {'modelo': 'FIAT STRADA', 'ano': 2014, 'placa': 'NDS3536'}

def test_registro_uso():
    result = RegistroUso('NDS3536', 'GUILHERME', '01/12/2023', '01/12/2023', 100, 200)
    assert result.__dict__ == {'placa': 'NDS3536', 'motorista': 'GUILHERME', 'data_inicial': '01/12/2023', 'data_final': '01/12/2023', 'km_inicial': 100, 'km_final': 200}

def test_registro_abastecimento():
    result = RegistroAbastecimento('NDS3536', 'GUILHERME', '01/12/2023', 44, 288)
    assert result.__dict__ == {'placa': 'NDS3536', 'motorista': 'GUILHERME', 'data': '01/12/2023', 'combustivel_litros': 44, 'custo': 288}
