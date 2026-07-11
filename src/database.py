import sqlite3
def conectar():
    conn = sqlite3.connect("../loja.db")

    conn.row_factory = sqlite3.Row

    conn.execute("PRAGMA foreign_keys = ON;")

    return conn