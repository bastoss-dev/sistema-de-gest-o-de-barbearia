clientes = ["Amaury Criança", "Amaury Adulto", "Amaury Idoso"]

valor_total = 0
servicos = 0

for cliente in clientes:

    print("Cliente:", cliente)

    continuar = "s"

    while continuar == "s":

        preco = float(input("Preço do serviço: "))

        valor_total += preco
        servicos += 1

        continuar = input("Mais um serviço? (s/n): ")

print("Total de serviços:", servicos)
print("Valor arrecadado:", valor_total)
