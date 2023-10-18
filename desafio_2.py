import textwrap


def menu():
    options = """
    
    ========== MENU ==========

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cnu]\tCadastrar novo cliente
    [luc]\tListar clientes cadastrados
    [cc]\tCriar conta corrente
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


def criar_conta_corrente(*, numero_conta: int, cpf_usuario: str):
    conta_corrente = {
        "Agência": "0001",
        "Número da conta": numero_conta,
        "Nome do cliente": cpf_usuario,
    }
    return conta_corrente


def buscar_cpf(lista_de_usuarios: list, cpf: str):
    for i in range(len(lista_de_usuarios)):
        conferir_cpf = lista_de_usuarios[i]["CPF"]
        if conferir_cpf == cpf:
            print("Usuário já está cadastrado!")
            return False
        else:
            continue


def main():
    saldo_acumulado = 0
    limite_conta = 500
    extrato_acumulado = ""
    numero_saques_diario = 0
    LIMITE_SAQUES_DIA = 3
    lista_de_usuarios = []
    lista_de_contas = []
    numero_conta = 1

    while True:
        opcao = input(menu())

        if opcao == "d":
            entrada = float(input("Informe o valor do depósito: "))
            saldo_acumulado, extrato_acumulado = depositar(
                saldo_acumulado, entrada, extrato_acumulado
            )

        elif opcao == "s":
            saldo_acumulado, extrato_acumulado = sacar(
                saldo=saldo_acumulado,
                limite=limite_conta,
                valor=float(input("Informe o valor do saque: ")),
                numero_saques=numero_saques_diario,
                extrato=extrato_acumulado,
                limite_saques=LIMITE_SAQUES_DIA,
            )

        elif opcao == "e":
            exibir_extrato(saldo_acumulado, extrato=extrato_acumulado)

        elif opcao == "cnu":
            print("\n================ CADASTRO ================")
            nome = input("Insira o seu nome completo: ")
            data_nascimento = input("Insira a data de nascimento: ")
            cpf = input("Insira o número do seu CPF (apenas números): ")

            if buscar_cpf(lista_de_usuarios=lista_de_usuarios, cpf=cpf):
                main()

            endereco = input(
                """Insira o seu endereço completo no formato: logradouro,
                nro - bairro - cidade/sigla estado: """
            )
            print("\n======= CADASTRO CONCLUÍDO================")

            lista_de_usuarios.append(
                criar_usuario(
                    nome=nome,
                    data_de_nascimento=data_nascimento,
                    cpf=cpf,
                    endereco=endereco,
                )
            )

        elif opcao == "luc":
            print(lista_de_usuarios)

        elif opcao == "cc":
            numero_cpf = input("Insira o seu número de CPF: ")

            print(
                criar_conta_corrente(numero_conta=numero_conta, cpf_usuario=numero_cpf)
            )

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
