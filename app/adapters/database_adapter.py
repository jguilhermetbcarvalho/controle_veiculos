from abc import ABC, abstractmethod
from entities.veiculo import Veiculo


class IDatabaseAdapter(ABC):

    @abstractmethod
    def salvar_entidade(self, tabela, **dados):
        pass

    @abstractmethod
    def atualizar_entidade(self, tabela, chave_primaria, **dados):
        pass

    @abstractmethod
    def remover_entidade(self, tabela, chave_primaria, **dados):
        pass

    @abstractmethod
    def buscar_entidade(self, tabela, **dados):
        pass

