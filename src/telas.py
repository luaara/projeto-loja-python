from decimal import Decimal

from operacoes import lista_clientes, cadastrar_cliente, atualizar_cliente, deletar_cliente, buscar_cliente, \
    listar_produtos, listar_pedidos, criar_pedido, listar_categorias, cadastrar_produtos, buscar_produto, \
    atualizar_estoque


def clientes():
    print("==========================")
    print("  CLIENTES ")
    print("==========================")
    print("1. Listar")
    print("2. Cadastrar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Sair")
    print("==========================")

    while True:
        try:
            opcao = int(input("Digite uma opção de 0 a 4: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            clientes = lista_clientes()
            print("==========================")
            print("Lista de clientes: ")
            for c in clientes:
                print(f"[{c['id_cliente']}] {c['nome']} | {c['email']}")

        if opcao == 2:
            print("==========================")
            print("Cadastrando novo cliente: ")
            nome = input("Digite o nome: ")
            email = input("Digite o email (fulano@hotmail.com): ")
            telefone = input("Digite o telefone (DDD) 00000-0000: ")
            id_novo_cliente = cadastrar_cliente(nome, email, telefone)
            cliente_cadastrado = buscar_cliente(id_novo_cliente)
            print("Cliente cadastrado com sucesso!")
            print(f"[{cliente_cadastrado['id_cliente']}] {cliente_cadastrado['nome']} | {cliente_cadastrado['email']} | {cliente_cadastrado['email']} ")

        if opcao == 3:
            print("==========================")
            print("Atualizando cliente: ")

            clientes = lista_clientes()
            print("==========================")
            print("Lista de clientes: ")
            for c in clientes:
                print(f"[{c['id_cliente']}] {c['nome']} | {c['email']} | {c['telefone']}")

            id_cliente = input("Digite o id_cliente: ")
            nome = input("Digite o nome: ")
            email = input("Digite o email (fulano@hotmail.com): ")
            telefone = input("Digite o telefone (DDD) 00000-0000: ")

            cliente_atualizado = atualizar_cliente(id_cliente, nome, email, telefone)

            if cliente_atualizado == True:
                dados_cliente_atualizado = buscar_cliente(id_cliente)
                print(f"[{dados_cliente_atualizado['id_cliente']}] {dados_cliente_atualizado['nome']} | {dados_cliente_atualizado['email']} | {dados_cliente_atualizado['telefone']} ")
                print("Atualizado com sucesso!")
            else:
                print("Cliente não encontrado.")

        if opcao == 4:
            print("==========================")
            print("Deletando cliente: ")

            clientes = lista_clientes()
            print("==========================")
            print("Lista de clientes: ")
            for c in clientes:
                print(f"[{c['id_cliente']}] {c['nome']}")

            id_cliente = input("Digite o id_cliente: ")
            cliente = buscar_cliente(id_cliente)

            if cliente:
                confirma = input(f"Deletar {cliente['nome']}? (s/n): ")
                if confirma == 's':
                    deletar_cliente(id_cliente)
                    print(f"{cliente['nome']} deletado com sucesso!")
                else:
                    print("Desistindo...")
                    print(f"{cliente['nome']} não deletado!")
            else:
                print(f"{id_cliente} não encontrado!")

        if opcao == 0:
            print("Voltando ao menu principal...")
            break

#PRODUTOS
def produtos():
    print("==========================")
    print("  PRODUTOS ")
    print("==========================")
    print("1. Listar produtos")
    print("2. Cadastrar produto")
    print("3. Buscar produto")
    print("4. Atualizar estoque")
    print("5. Cadastrar categoria")
    print("6. Listar categorias")
    print("0. Sair")
    print("==========================")

    while True:
        try:
            opcao = int(input("Digite uma opção de 0 a 4: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            produtos = listar_produtos()
            print("==========================")
            print("Lista de produtos: ")
            for p in produtos:
                print(f"{p['nome']} | R${p['preco']} | estoque:{p['estoque']}")

        if opcao == 2:
            print("==========================")
            print("Cadastrando novo produto: ")
            nome = input("Digite o nome: ")
            preco = Decimal(input("Digite o preço em R$00.00: "))
            estoque = int(input("Digite a quantidade em estoque: "))

            print("==========================")
            print("Lista de categorias: ")
            listar_categorias()
            id_categoria = int(input("Digite o id da categoria: "))

            produto_cadastrado = cadastrar_produtos(nome, preco, estoque, id_categoria)
            print("Produto cadastrado com sucesso!")
            print(f"id da categoria: [{produto_cadastrado['nome']}] -- {produto_cadastrado['nome']} | R${produto_cadastrado['preco']} | estoque: {produto_cadastrado['nome']}")

        if opcao == 3:
            print("==========================")
            print("Buscando produto: ")
            nome = input("Digite o nome do produto: ")
            buscando_produto = buscar_produto(nome)


        if opcao == 4:
            print("==========================")
            print("Atualizando estoque: ")

            produtos = listar_produtos()
            print("==========================")
            print("Lista de produtos: ")
            for p in produtos:
                print(f"id do produto:{p['id_produto']} | {p['nome']} | estoque:{p['estoque']} ")

            id_produto = input("Digite o id do produto: ")
            quantidade = int(input("Digite a nova quantidade em estoque: "))


            estoque_atualizado = atualizar_estoque(id_produto, quantidade)

            if estoque_atualizado:
                print("Atualizado com sucesso!")
            else:
                print("Produto não encontrado.")



#PEDIDOS
def pedidos():
    print("==========================")
    print("  PEDIDOS ")
    print("==========================")
    print("1. Listar pedidos")
    print("2. Criar Pedidos")
    print("3. Detalhar Pedidos")
    print("4. Atualizar Status")
    print("0. Sair")
    print("==========================")

    while True:
        try:
            opcao = int(input("Digite uma opção de 0 a 4: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            pedidos = listar_pedidos()
            print("==========================")
            print("Lista de pedidos: ")
            for p in pedidos:
                print(f"{p['nome']} | status: {p['status']} | total: R${p['valor_total']}")

        if opcao == 2:
            print("==========================")
            print("Criando um pedido: ")
            print("==========================")
            print("Lista de clientes disponíveis: ")
            clientes = lista_clientes()
            for c in clientes:
                print(f"[{c['id_cliente']}] {c['nome']} | {c['email']} | {c['telefone']}")
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
            except ValueError:
                print("ID inválido!")
                continue

            itens = []
            produtos = listar_produtos()
            while True:
                print("==========================")
                print("Lista de produtos: ")
                for p in produtos:
                    print(f"{p['nome']} | R${p['preco']} | estoque:{p['estoque']}")

                try:
                    id_produto = input("Digite o ID do produto para adicionar (ou 'F' para finalizar o pedido): ")
                    if id_produto.upper() == 'F':
                        break

                    id_produto = int(id_produto)
                    qtd = int(input("Digite a quantidade desejada: "))

                    if qtd <= 0:
                        print("A quantidade deve ser maior que zero!")
                        continue

                    itens.append({"id_produto": id_produto, "quantidade": qtd})
                    print("Produto adicionado ao carrinho!")

                except ValueError:
                    print("Entrada inválida! Digite um número para o ID/Quantidade ou 'F' para terminar.")


            if itens:
                try:
                    novo_pedido = criar_pedido(id_cliente, itens)
                    print(f"Pedido {novo_pedido} criado com sucesso!")
                except ValueError as e:
                    print(f"Erro ao criar pedido: {e}")
            else:
                print("Nenhum produto foi selecionado. Pedido cancelado.")

