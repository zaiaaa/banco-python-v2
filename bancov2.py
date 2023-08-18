# função saque = keyword only
# função depósito = positional only
# função extrato = hibrid only
def Saque(*, saldo, valor, numero_saques, extrato, limite, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print(
            f"Operação falhou! Número máximo de saques excedido. ({numero_saques} saques realizados)")
        return saldo, extrato, numero_saques

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de {valor:.2f}R$ realizado com sucesso!")
        return saldo, extrato, numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")


def Deposito(valor, saldo, extrato, /):
    if valor > 0:
        novoSaldo = saldo + valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(
            f'Depósito de {valor:.2f}R$ realizado com sucesso! (Saldo: {novoSaldo})')

        return novoSaldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato


def criarUsuario(**cliente):

    print(f"Cliente {cliente['nome']} criado com sucesso!")
    pessoas.append(cliente)
    # print(pessoas)


def mostrarUsuarios():

    if pessoas != []:
        print('Contas cadastradas: ')
        for i, pessoa in enumerate(pessoas):
            num_cliente = i+1

            print(
                f"Cliente {num_cliente}: Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Data de nascimento: {pessoa['data_nascimento']}, Endereço: {pessoa['endereco']}")
    else:
        print('Nenhuma pessoa cadastrada.')


def mostrarExtrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def filtrarUsuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    # pessoas.filter(e => e.cpf === cpf)
    # Python é uma MERDA por causa disso, tão simples...
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criarConta(agencia, numero_conta, pessoas):
    cpf = str(input('Digite o CPF do usuário que fará a conta: '))
    pessoa = filtrarUsuario(cpf, pessoas)
    if pessoa:
        contas.append(
            {"agencia": agencia, "numero_conta": numero_conta, "usuario": pessoa})
        print(contas)
        print("Conta criada com sucesso!")
    else:
        print('Usuário não encontrado.')


def vizualisar_contas(lista_contas):
    tamanhoLista = len(lista_contas)
    # print(tamanhoLista)
    if tamanhoLista == 0:
        print('n tem conta ainda')
    else:
        for conta in lista_contas:
            print(
                f"Agência: {conta['agencia']}, Numero da conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")


def exibirUsuarioFiltrado(cpf):
    pessoasFiltradas = [pessoa for pessoa in pessoas if pessoa['cpf'] == cpf]
    print(exibirUsuariosFormatados(pessoasFiltradas))


def exibirUsuariosFormatados(lista_pessoas):
    for i, pessoa in enumerate(lista_pessoas):
        num_cliente = i+1
        print(
            f"Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Data de nascimento: {pessoa['data_nascimento']}, Endereço: {pessoa['endereco']}")


contas = []
pessoas = []


def main():

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[t] Criar conta corrente
[v] Visualizar usuários
[h] Visualizar contas corrente 
[f] Filtrar usuários
[q] Sair

=> """
    saldo = 100
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    numero_conta = 1
    while True:

        opcao = input(menu)
        if opcao == "d":
            valorDeposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = Deposito(valorDeposito, saldo, extrato)
        elif opcao == "s":
            valorSaque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = Saque(saldo=saldo, valor=valorSaque,
                                                  numero_saques=numero_saques, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            mostrarExtrato(saldo, extrato)

        elif opcao == "c":
            nome = str(input("Informe o nome do novo usuário: "))
            cpf = str(input("Informe o CPF do novo usuário: "))
            data_nasc = str(
                input("Informe a data de nascimento do novo usuário: "))
            endereco = str(input("Informe o endereço do novo usuário: "))
            verificaCpf = [pessoa for pessoa in pessoas
                           if cpf == pessoa['cpf']]
            # pessoas.filter(e => e.cpf == cpf)
            # print(verificaCpf)

            if verificaCpf == []:
                criarUsuario(**{"nome": nome, "cpf": cpf,
                                "data_nascimento": data_nasc, "endereco": endereco})
            else:
                print('CPF já cadastrado.')

        elif opcao == "q":
            break
        elif opcao == 'v':
            mostrarUsuarios()
        elif opcao == 't':
            criarConta(AGENCIA, numero_conta, pessoas)
            numero_conta = numero_conta + 1
        elif opcao == 'h':
            vizualisar_contas(contas)
        elif opcao == 'f':
            if len(pessoas) == 0:
                print('Não existem usuários cadastrados.')
            else:
                print(f'Usuários cadastrados:')
                exibirUsuariosFormatados(pessoas)
                cpf = str(input('Digite o CPF da pessoa que deseja encontrar: '))
                exibirUsuarioFiltrado(cpf)

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
