import sqlite3
from datetime import datetime

def criar_tabela_pokedex():
    conectar = sqlite3.connect("supertrunfo.db")
    cursor = conectar.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokedex (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            tipo_primario TEXT,
            tipo_secundario TEXT,
            hp INTEGER,
            ataque INTEGER,
            defesa INTEGER,
            jogador TEXT,
            data TEXT
        )
    """)
    print("Tabela pokedex✅")
    conectar.commit()
    conectar.close()




   
