from utils import *
import pytest


def test_sacar_saldo_insuficiente():
    assert (100, "") == sacar(
        saldo=100, valor=400, numero_saques=2, limite=500, extrato="", limite_saques=2
    )


@pytest.fixture(params=["01352430258", "12345678907"])
def validos(request):
    return request.param


def test_validar_cpf(
    validos,
):
    assert True == validar_cpf(validos)


@pytest.fixture(
    params=[
        [
            {
                "Agência": "0001",
                "Número da conta": "1",
                "Usuário": "01352430258",
                "Status": "ativo",
            }
        ]
    ]
)
def lista_de_contas(request):
    return request.param


def test_inativar_conta(lista_de_contas):
    assert True == inativar_conta("1", lista_contas=lista_de_contas)
