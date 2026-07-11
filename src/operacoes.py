from database import conectar


##CLIENTES

def buscar_cliente(id_cliente):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = ?",(id_cliente,))
        return cursor.fetchone()

def lista_clientes():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()


def cadastrar_cliente(nome, email, telefone):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?,?);", (nome, email, telefone))
        return cursor.lastrowid


def atualizar_cliente(id_cliente, nome, email, telefone):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id_cliente = ?;",
            (nome, email, telefone, id_cliente)
        )

        return True


def deletar_cliente(id_cliente):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM clientes WHERE id_cliente = ?;", (id_cliente,)
        )
        return True


##PRODUTOS
def buscar_produto(nome):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE nome = ?",(nome,))
        return cursor.fetchone()


def listar_produtos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM produtos INNER JOIN categorias ON produtos.id_categoria = categorias.id_categoria"
        )

        return cursor.fetchall()


def cadastrar_produtos(nome, preco, estoque, id_categoria):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos(nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?)",
            (nome, preco, estoque, id_categoria)
        )

        return cursor.lastrowid


def atualizar_estoque(id_produto, quantidade):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET estoque = estoque + ? WHERE id_produto = ? AND estoque + ? >= 0",
            (quantidade, id_produto, quantidade)
        )

        return True

def cadastrar_categorias(nome):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO categorias(nome) VALUES (?)",
            (nome,)
        )

        return cursor.lastrowid


def listar_categorias():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM categorias"
        )

    return cursor.fetchall()


##PEDIDOS
def criar_pedido(id_cliente, itens):
    with conectar() as conn:
        cursor = conn.cursor()
        itens_validados = []
        for item in itens:
            cursor.execute(
                ''' SELECT id_produto, nome, preco, estoque FROM produtos WHERE id_produto = ?
                ''', (item["id_produto"],)
            )

            produto = cursor.fetchone()

            if produto is None:
                raise ValueError(f"Produto {item["id_produto"]} não encontrado!")

            if produto["estoque"] < item["quantidade"]:
                raise ValueError(f"Produto {produto["nome"]} sem estoque!")

            itens_validados.append({
                "id_produto": produto["id_produto"],
                "quantidade": item["quantidade"],
                "preco_produto": produto["preco"]
            })

        cursor.execute(
            ''' INSERT INTO pedidos(id_cliente, status) VALUES (?, ?)
            ''', (id_cliente, 'pendente')
        )

        id_pedido = cursor.lastrowid

        for item in itens_validados:
            cursor.execute(
                '''INSERT INTO itens_pedido(id_pedido, id_produto, quantidade, preco_unit) VALUES (?, ?, ?, ?)''',
                (id_pedido, item["id_produto"], item["quantidade"], item["preco_produto"]))

            cursor.execute(
                "UPDATE produtos SET estoque = estoque - ? WHERE id_produto = ?",
                (item["quantidade"], item["id_produto"])
            )

        return id_pedido


def listar_pedidos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT p.id_pedido, p.status, p.criado_em, c.nome, SUM(ip.quantidade * ip.preco_unit) AS valor_total FROM pedidos p 
            INNER JOIN clientes c ON p.id_cliente = c.id_cliente 
            INNER JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            GROUP BY p.id_pedido
            '''
        )

        return cursor.fetchall()


def detalhar_pedido(id_pedido):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT p.id_pedido, p.status, p.criado_em, c.nome
            FROM pedidos p
            INNER JOIN clientes c ON p.id_cliente = c.id_cliente
            WHERE p.id_pedido = ?
           ''', (id_pedido,)
        )

        pedido = cursor.fetchone()

        cursor.execute(
            '''SELECT pr.nome, ip.quantidade, ip.preco_unit
            FROM itens_pedido ip
            INNER JOIN produtos pr ON ip.id_produto = pr.id_produto
            WHERE ip.id_pedido = ?
           ''', (id_pedido,)
        )
        itens = cursor.fetchall()

        return pedido, itens

def atualizar_status(id_pedido, status):
    with conectar() as conn:
        cursor = conn.cursor()
        if status not in ('pendente', 'pago', 'cancelado'):
            raise ValueError("O status é inválido! Use: pendente, pago ou cancelado")
        cursor.execute(
            "UPDATE pedidos SET status = ? WHERE id_pedido = ?",(status, id_pedido)
        )

        return True

#RELATÓRIOS
def relatorio_vendas_por_categoria():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT ct.nome, COUNT(DISTINCT p.id_pedido) AS total_pedidos, SUM(ip.quantidade) AS unidades_vendidas, SUM(ip.quantidade * ip.preco_unit) AS receita
            FROM produtos pr
            INNER JOIN categorias ct ON pr.id_categoria = ct.id_categoria
            INNER JOIN itens_pedido ip ON pr.id_produto = ip.id_produto
            INNER JOIN pedidos p ON ip.id_pedido = p.id_pedido
            WHERE p.status != 'cancelado'
            GROUP BY ct.nome
            '''
        )
        return cursor.fetchall()

def relatorio_mais_vendidos(limite=5):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT pr.nome, SUM(ip.quantidade) AS unidades_vendidas FROM produtos pr
            INNER JOIN itens_pedido ip ON pr.id_produto = ip.id_produto
            GROUP BY pr.nome
            ORDER BY unidades_vendidas DESC LIMIT ?
            
            ''',(limite,)
        )
        return cursor.fetchall()

def relatorio_estoque_baixo(minimo=10):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT pr.nome, pr.estoque, ct.nome AS categoria FROM produtos pr 
            LEFT JOIN categorias ct ON pr.id_categoria = ct.id_categoria
            WHERE estoque <= ?
            ''',(minimo,)
        )

        return cursor.fetchall()