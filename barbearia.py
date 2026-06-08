fila = []

clientes_atendidos = 0
valor_total = 0

while True:

    print("\n===== BARBEARIA =====")
    print("1 - Adicionar cliente")
    print("2 - Ver fila")
    print("3 - Atender cliente")
    print("4 - Relatório")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome do cliente: ")

        print("1 - Corte (R$55)")
        print("2 - Barba (R$30)")
        print("3 - Sobrancelha (R$15)")

        servico = input("Escolha o serviço: ")

        fila.append([nome, servico])

        print("Cliente adicionado!")

    elif opcao == "2":

        print("\nFila:")

        if len(fila) == 0:
            print("Fila vazia")

        else:
            for cliente in fila:
                print(cliente[0])

    elif opcao == "3":

        if len(fila) > 0:

            cliente = fila.pop(0)

            nome = cliente[0]
            servico = cliente[1]

            if servico == "1":
                valor = 55

            elif servico == "2":
                valor = 30

            else:
                valor = 15

            print("\nCliente:", nome)
            print("Valor a pagar: R$", valor)

            clientes_atendidos += 1
            valor_total += valor

        else:

            print("Fila vazia")

    elif opcao == "4":

        print("\n===== RELATÓRIO =====")
        print("Clientes atendidos:", clientes_atendidos)
        print("Valor arrecadado: R$", valor_total)

    elif opcao == "5":

        print("Sistema encerrado")
        break

    else:

        print("Opção inválida")
