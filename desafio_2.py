from utils import *


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
                print("Usuário já está cadastrado!")
                continue

            endereco = input(
                textwrap.dedent(
                    """Insira o seu endereço completo no formato: logradouro, nro - bairro - cidade/sigla estado: """
                )
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
