# 🛒 Projeto Loja Virtual

Um sistema completo de gerenciamento para loja virtual desenvolvido em **Python** com banco de dados **SQLite**. O sistema funciona via terminal (CLI) e possui uma arquitetura bem definida, separando a interface (telas), regras de negócio (operações) e persistência de dados.

---

## ⚙️ Funcionalidades

O sistema está dividido em quatro módulos principais (em construção):

### 👥 Clientes
* Cadastrar novos clientes.
* Listar todos os clientes cadastrados.
* Atualizar dados cadastrais.
* Excluir clientes do sistema.

### 📦 Produtos
* Cadastrar e listar categorias de produtos.
* Cadastrar produtos vinculados a categorias.
* Listar e buscar produtos.
* Gerenciamento e atualização de estoque.

### 🛍️ Pedidos
* Criar pedidos adicionando múltiplos produtos ao carrinho.
* **Validação inteligente:** Verifica automaticamente se há estoque disponível antes de fechar o pedido.
* Baixa automática no estoque após a criação do pedido.
* Detalhar itens de um pedido específico.
* Atualizar status do pedido (`pendente`, `pago` ou `cancelado`).

### 📊 Relatórios
* Visualizar o volume de vendas e a receita gerada por categoria.
* Top 5 produtos mais vendidos.
* Alerta de produtos com estoque baixo.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Banco de Dados:** SQLite3 (embutido nativamente no Python, sem necessidade de servidores extras)
* **Estrutura de Dados:** Utilização de `sqlite3.Row` para acesso aos dados por nome de coluna (dicionários).

---

## 📁 Estrutura do Projeto

A arquitetura do projeto foi pensada para manter a organização e escalabilidade:

```text
loja_virtual/
│
├── src/
│   ├── main.py          # Arquivo principal que inicializa o menu do sistema
│   ├── telas.py         # Interface de linha de comando (CLI) e interação com o usuário
│   ├── operacoes.py     # Lógica de negócios (CRUD e regras do sistema)
│   └── database.py      # Configuração de conexão com o SQLite
│
├── schema.sql           # Script SQL contendo a estrutura de tabelas do banco
└── README.md            # Documentação do projeto

```

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório:
```bash
git clone https://github.com/luaara/projeto-loja-python.git

```


3. Navegue até a pasta do projeto:
```bash
cd projeto-loja-python

```


4. Execute o arquivo principal dentro da pasta `src`:
```bash
python src/main.py

```



*(Nota: O banco de dados `loja.db` será gerenciado automaticamente pelas funções do sistema, de acordo com o `schema.sql` construído previamente).*

---

## 🧑‍💻 Autor

Desenvolvido por **Luara** durante estudos de programação em Python, SQL e Banco de Dados.
