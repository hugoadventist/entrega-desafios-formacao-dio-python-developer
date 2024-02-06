from utils import *


def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "cnu":
            criar_cliente(clientes)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "cc":
            criar_conta(clientes, contas)
        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
