import sqlite3
from datetime import datetime

def criar_tabela_pokedex():
    conectar = sqlite3.connect("database/supertrunfo.db")
    cursor = conectar.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokedex (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            tipo_primario TEXT,
            tipo_secundario TEXT,
            hp INTEGER,
            ataque INTEGER,
            defesa INTEGER,
            jogador TEXT DEFAULT NULL,
            data TEXT DEFAULT (datetime('now'))

        )
    """)
    
    print("Tabela pokedex ✅")
    conectar.commit()
    conectar.close()


def criar_tabela_score():
    conectar = sqlite3.connect("database/supertrunfo.db")
    cursor = conectar.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jogador TEXT,
            name TEXT unique,
            pontos INTEGER,
            rodadas_vencidas INTEGER,
            data TEXT DEFAULT (datetime('now'))
        )
    """)
    conectar.commit()
    conectar.close()
    print("Tabela Score ✅")
    
def pokedex(nome, tipo_primario, tipo_secundario, hp, ataque, defesa):
    conectar = sqlite3.connect("database/supertrunfo.db")
    cursor = conectar.cursor()
    cursor.execute("""
        INSERT INTO pokedex (nome, tipo_primario, tipo_secundario, hp, ataque, defesa)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, tipo_primario, tipo_secundario, hp, ataque, defesa))
    conectar.commit()
    print("Tabela pokedex ✅")
    print("Tabela Score ✅") 
    conectar.close()

def mostrar_pokedex():
    conectar = sqlite3.connect("database/supertrunfo.db")
    cursor = conectar.cursor()
    cursor.execute("""SELECT nome FROM pokedex
                   limit 5"""

                   )
    resultados = cursor.fetchall()
    conectar.close()
    return resultados