import sqlite3


connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS HOTEIS (HOTEL_ID text PRIMARY KEY,\
nome text, estrelas real, diaria real, cidade real)"

cursor.execute(criar_tabela)
connection.commit()
connection.close()
