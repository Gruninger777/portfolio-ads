import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "pedidos.db"


def get_connection():
    """Cria uma conexao com o banco e retorna linhas como dicionarios simples."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """
    Cria a tabela principal caso ela ainda nao exista.
    Tambem insere pedidos iniciais para facilitar testes da API.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            valor REAL NOT NULL
        )
        """
    )

    cursor.execute("SELECT COUNT(*) AS total FROM pedidos")
    total = cursor.fetchone()["total"]

    if total == 0:
        pedidos_iniciais = [
            ("Ana", "Notebook", 1, 3500.00),
            ("Carlos", "Mouse Gamer", 2, 150.90),
            ("Fernanda", "Teclado Mecanico", 1, 289.99),
        ]

        cursor.executemany(
            """
            INSERT INTO pedidos (cliente, produto, quantidade, valor)
            VALUES (?, ?, ?, ?)
            """,
            pedidos_iniciais,
        )

    connection.commit()
    connection.close()


def list_orders():
    """Retorna todos os pedidos cadastrados no banco."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pedidos ORDER BY id")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]


def get_order_by_id(order_id):
    """Busca um pedido especifico pelo identificador."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (order_id,))
    row = cursor.fetchone()
    connection.close()
    return dict(row) if row else None


def add_order(cliente, produto, quantidade, valor):
    """Adiciona um novo pedido e devolve os dados persistidos."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO pedidos (cliente, produto, quantidade, valor)
        VALUES (?, ?, ?, ?)
        """,
        (cliente, produto, quantidade, valor),
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return get_order_by_id(new_id)


def delete_order(order_id):
    """Remove um pedido. Retorna True quando a exclusao realmente acontece."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (order_id,))
    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()
    return deleted
