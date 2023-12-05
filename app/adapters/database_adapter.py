from abc import ABC, abstractmethod
from app.entities.veiculo import Veiculo


class IDatabaseAdapter(ABC):

    @abstractmethod
    def salvar_entidade(self, tabela, **dados):
        pass

    @abstractmethod
    def atualizar_entidade(self, tabela, chave_primaria, **dados):
        pass

    @abstractmethod
    def remover_entidade(self, tabela, chave_primaria, identificador):
        pass

    @abstractmethod
    def buscar_entidade(self, tabela, chave_primaria, identificador):
        pass

    @abstractmethod
    def mapear_entidade(self, tabela, resultado):
        pass

