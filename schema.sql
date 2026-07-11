PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categorias (

id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL UNIQUE

);

CREATE TABLE IF NOT EXISTS clientes (

id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
telefone TEXT 
);

CREATE TABLE IF NOT EXISTS produtos (

id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL NOT NULL CHECK(preco >= 0),
estoque INTEGER DEFAULT 0 CHECK(estoque >= 0),
id_categoria INTEGER,
CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)

);

CREATE TABLE IF NOT EXISTS pedidos (
id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
status TEXT DEFAULT 'pendente' CHECK(status IN ('pendente', 'pago', 'cancelado')),
criado_em TEXT DEFAULT (datetime('now', 'localtime')),
id_cliente INTEGER,
CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)

);

CREATE TABLE IF NOT EXISTS itens_pedido (

id_item INTEGER PRIMARY KEY AUTOINCREMENT,
quantidade INTEGER NOT NULL CHECK(quantidade > 0),
preco_unit REAL NOT NULL CHECK(preco_unit >= 0),
id_pedido INTEGER,
id_produto INTEGER,
CONSTRAINT fk_pedido FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)

);


