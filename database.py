import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnpj TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf_cnpj TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo TEXT NOT NULL UNIQUE,
            valor REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas_fiscais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_emissao TEXT NOT NULL,
            chave TEXT NOT NULL,
            cliente_cpf_cnpj TEXT NOT NULL,
            valor_total REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
