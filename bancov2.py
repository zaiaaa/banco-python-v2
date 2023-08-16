# função saque = keyword only
# função depósito = positional only
# função extrato = hibrid only

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def Saque(*, saldo, valor):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    global numero_saques

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print(
            f"Operação falhou! Número máximo de saques excedido. ({numero_saques} saques realizados)")

    elif valor > 0:
        saldo -= valor
        global extrato
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de {valor:.2f}R$ realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")


def Deposito(valor, /):
    if valor > 0:
        global saldo
        global extrato
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Depósito de {valor:.2f}R$ realizado com sucesso!')

    else:
        print("Operação falhou! O valor informado é inválido.")


pessoas = []


def criarUsuario(**cliente):

    print(f"Cliente {cliente['nome']} criado com sucesso!")
    pessoas.append(cliente)

    for pessoa in pessoas:
        print(pessoa['cpf'])


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        Deposito(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        Saque(saldo=saldo, valor=valor)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        criarUsuario(**{"nome": "Gustavo", "cpf": "242424",
                     "data_nascimento": "02/09/2006", "Endereço": "Rua 13, 501"})
        print(pessoas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
