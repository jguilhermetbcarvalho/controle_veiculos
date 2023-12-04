from abc import ABC, abstractmethod
from entities.veiculo import Veiculo


class IDatabaseAdapter(ABC):

    @abstractmethod
    def salvar_veiculo(self, veiculo: Veiculo) -> None:
        pass

    @abstractmethod
    def buscar_veiculo(self, veiculo: Veiculo) -> None:
        pass

    @abstractmethod
    def atualizar_veiculo(self, veiculo: Veiculo) -> None:
        pass

    @abstractmethod
    def remover_veiculo(self, veiculo: Veiculo) -> None:
        pass

