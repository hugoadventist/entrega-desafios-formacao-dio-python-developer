from utils import *


def test_sacar_saldo_insuficiente():
    assert (100, "") == sacar(
        saldo=100, valor=400, numero_saques=2, limite=500, extrato="", limite_saques=2
    )
