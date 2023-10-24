"""
Functions with business rules
"""
import textwrap
import re


def menu():
    options = """
    
    ========== MENU ==========

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cnu]\tCadastrar novo cliente
    [luc]\tListar clientes cadastrados
    [lcc]\tListar contas cadastradas
    [cc]\tCriar conta corrente
    [icc]\tInativar conta corrente
    [q]\tSair

    => """
    return textwrap.dedent(options)


def sacar(*, saldo, valor, numero_saques, limite, extrato, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def depositar(saldo: float, valor: float, extrato: str, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def criar_usuario(*, nome: str, data_de_nascimento: str, cpf: str, endereco: str):
    novo_usuario = {
        "nome": nome,
        "Data de nascimento": data_de_nascimento,
        "CPF": cpf,
        "Endereço": endereco,
    }
    return novo_usuario


def criar_conta_corrente(
    *, agencia: str, numero_conta: str, cpf_usuario: str, status: str = "ativo"
):
    conta_corrente = {
        "Agência": agencia,
        "Número da conta": str(numero_conta),
        "Usuário": cpf_usuario,
        "Status": status,
    }
    return conta_corrente


def buscar_cpf(lista_de_usuarios: list, cpf: str):
    for i in range(len(lista_de_usuarios)):
        conferir_cpf = lista_de_usuarios[i]["CPF"]
        if conferir_cpf == cpf:
            return True


def validar_cpf(cpf: str):
    validacao = bool(len(cpf) == 11 and re.match("[0-9]", cpf))
    return validacao


def inativar_conta(numero_conta: str, *, lista_contas: list):
    for i in range(len(lista_contas)):
        conferir_numero_conta = lista_contas[i]["Número da conta"]
        if conferir_numero_conta == numero_conta:
            lista_contas[i]["Status"] = "inativo"
            return True