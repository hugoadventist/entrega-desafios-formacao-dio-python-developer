"""
Functions with business rules
"""
import textwrap
import re
import hashlib
from main import Cliente, Deposito, Saque, ContaCorrente, PessoaFisica


def menu() -> None:
    options = """
    
    ========== MENU ==========

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cnu]\tCadastrar novo cliente
    [luc]\tListar clientes cadastrados
    [lc]\tListar contas cadastradas
    [cc]\tCriar conta corrente
    [icc]\tInativar conta corrente
    [q]\tSair

    => """
    return textwrap.dedent(options)


def sacar(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))

    transacao = Saque(valor)
    conta = selecionar_conta_cliente(cliente)

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    conta = selecionar_conta_cliente(cliente)
    if not conta:
        print("Opção inválida!")
        return
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    print("==========================================")


def depositar(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))

    transacao = Deposito(valor)
    conta = selecionar_conta_cliente(cliente)

    cliente.realizar_transacao(conta, transacao)


def criar_cliente(clientes: list) -> None:
    cpf = input("Informe o CPF (somente número): ")

    if validar_cpf(cpf=cpf):
        cliente = filtrar_cliente(cpf, clientes)
        if cliente:
            print("\n @@@ Já existe cliente com esse CPF: @@@")
            return
    else:
        print("Número inválido! Repita a operação.")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd - mm - aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )
    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n === Cliente criado com sucesso! ===")


def criar_conta(clientes: Cliente, contas: list) -> None:
    cpf = input("Informe o número de CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    numero_conta = len(contas) + 1

    if not cliente:
        print("\n @@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("Conta cadastrada com sucesso")
    print(str(conta))


def validar_cpf(cpf: str) -> bool:
    validacao = bool(len(cpf) == 11 and re.match("[0-9]", cpf))
    return validacao


def inativar_conta(numero_conta: str, *, lista_contas: list):
    for i in range(len(lista_contas)):
        conferir_numero_conta = lista_contas[i]["Número da conta"]
        if conferir_numero_conta == numero_conta:
            lista_contas[i]["Status"] = "inativo"
            return True


def filtrar_cliente(cpf: str, clientes: Cliente) -> Cliente | None:
    cliente_filtrado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_filtrado[0] if cliente_filtrado else None


def selecionar_conta_cliente(cliente: Cliente) -> Cliente | None:
    selecao = input("Entre com a opção da conta desejada: ")
    print(enumerate(cliente.contas))
    try:
        return cliente.contas[selecao]
    except (IndexError, TypeError):
        print("Opção inválida, tente novamente.")
        return


def string_to_random_integer(input_string: str) -> int:
    # Use SHA-256 hash function to get a secure hash
    hash_object = hashlib.sha256(input_string.encode())
    hash_hex = hash_object.hexdigest()

    # Take the first 6 characters of the hexadecimal hash and convert to integer
    random_integer = int(hash_hex[:6], 16)

    return random_integer


def listar_contas(contas) -> None:
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
