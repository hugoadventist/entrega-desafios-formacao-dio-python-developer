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
    AGENCIA = "0001"

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
            while not validar_cpf(cpf):
                print("CPF inválido! Favor inserir um CPF válido.")
                cpf = input("Insira o número do seu CPF (apenas números): ")

                # continue
            if buscar_cpf(lista_de_usuarios=lista_de_usuarios, cpf=cpf):
                print("Usuário já está cadastrado!")
                continue

            endereco = input(
                textwrap.dedent(
                    "Insira o seu endereço completo no formato: logradouro,"
                    + "nro - bairro - cidade/sigla estado: "
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
            print("\n================ CADASTRO ================")
            numero_cpf = input("Insira o seu número de CPF: ")
            while not validar_cpf(numero_cpf):
                print("CPF inválido! Favor inserir um CPF válido.")
                numero_cpf = input("Insira o número do seu CPF (apenas números): ")

            if buscar_cpf(lista_de_usuarios=lista_de_usuarios, cpf=numero_cpf):
                lista_de_contas.append(
                    criar_conta_corrente(
                        agencia=AGENCIA,
                        numero_conta=numero_conta,
                        cpf_usuario=numero_cpf,
                    )
                )
                numero_conta += 1
                print("\n======= CADASTRO CONCLUÍDO================")

            else:
                print("Não possível cadastrar a sua nova conta!. CPF não encontrado!")

        elif opcao == "lcc":
            print(lista_de_contas)

        elif opcao == "icc":
            print("/n=====================================")
            conta_para_inativar = input(
                "Entre com o número da conta que deseja inativar: "
            )
            if inativar_conta(conta_para_inativar, lista_contas=lista_de_contas):
                print("A conta foi inativada com sucesso!")
            else:
                print(
                    "Não foi possível realizar a inativação da conta, "
                    + "favor verificar se inseriu os dados corretamente."
                )

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
