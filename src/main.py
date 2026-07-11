from telas import clientes, produtos, pedidos

print("==========================")
print("   🛒 LOJA VIRTUAL")
print("==========================")
print("1. Clientes")
print("2. Produtos")
print("3. Pedidos")
print("4. Relatórios")
print("0. Sair")
print("==========================")


while True:
    try:
        opcao = int(input("Digite uma opção de 0 a 4: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if opcao == 1:
        clientes()

    if opcao == 2:
        produtos()

    if opcao == 3:
        pedidos()

    elif opcao == 0:
        break



