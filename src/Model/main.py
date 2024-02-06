# main.py
from abc import ABC, abstractmethod, abstractproperty
from typing import Type
from datetime import datetime


class Conta:
    def __init__(self, numero: int, cliente: Type["Cliente"]) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Type["Cliente"], numero: int) -> Type["Conta"]:
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> float:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Type["Cliente"]:
        return self._cliente

    @property
    def historico(self) -> Type["Historico"]:
        return self._historico

    def sacar(self, valor: float) -> bool:
        excedeu_saldo = valor > self._saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

        return True


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Cliente:
    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(
        self, cpf: str, nome: str, data_nascimento: str, endereco: str
    ) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class ContaCorrente(Conta):
    def __init__(
        self, numero: int, cliente: Cliente, limite=500, limite_saques=3
    ) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            C\C:\t\t{self.numero}
            TItular:\t{self.cliente.nome}
            """


class Historico:
    def __init__(self) -> list:
        self._transacoes = []

    @property
    def transacoes(self) -> list:
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao) -> dict:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
