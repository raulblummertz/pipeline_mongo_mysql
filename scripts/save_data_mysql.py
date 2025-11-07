import mysql.connector
from dotenv import load_dotenv 
import os
import pandas as pd

load_dotenv()

host_name = os.getenv("DB_HOST")
user_name = os.getenv("DB_USER")
password = os.getenv("MYSQL_PASSWORD")

def connect_mysql(host_name, user_name, pw): 
    cnx = mysql.connector.connect(
    host="localhost",
    user="monza",
    password="monza"
    )
    return cnx
        
def create_cursor(cnx):
    cursor = cnx.cursor()
    return cursor

def create_database(cursor, db_name):
    cursor.execute("CREATE DATABASE IF NOT EXISTS dbprodutos_v2;")
    
def show_databases(cursor):
    cursor.execute("SHOW DATABASES;")
    for db in cursor:
        print(db)
    
def create_product_table(cursor, db_name, tb_name):
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {db_name}.{tb_name}(
        id VARCHAR(100),
        Produto VARCHAR(100),
        Categoria_Produto VARCHAR(100),
        Preco FLOAT(10,2),
        Frete FLOAT(10,2),
        Data_Compra DATE,
        Vendedor VARCHAR(100),
        Local_Compra VARCHAR(100),
        Avaliacao_Compra FLOAT,
        Tipo_Pagamento VARCHAR(100),
        Qntd_Parcelas INT,
        Latitude FLOAT(10,2),
        Longitude FLOAT(10,2),
        
        PRIMARY KEY (id)
    );                              
""")
    
def show_tables(cursor, db_name):
    cursor.execute(f"USE {db_name};")
    cursor.execute("SHOW TABLES;")
    for tb in cursor:
        print(tb)


def read_csv(path):
    df = pd.read_csv(f"{path}")
    return df


def add_product_data(cnx, cursor, df, db_name, tb_name):
    lista_dados = [tuple(row) for i, row in df.iterrows()]
    sql = f"INSERT INTO {db_name}.{tb_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.executemany(sql, lista_dados)
    cnx.commit()
    return print(cursor.rowcount, "registros inseridos.")

def drop_table(cursor, db_name, tb_name):
    cursor.execute(f"DROP TABLE {db_name}.{tb_name};")
    print(f"Tabela {tb_name} deletada com sucesso.")

if __name__ == "__main__":
    cnx = connect_mysql(host_name, user_name, password)
    cursor = create_cursor(cnx)
    
    create_database(cursor, "dbprodutos_v2")
    show_databases(cursor)
    
    create_product_table(cursor, "dbprodutos_v2", "tb_produtos")
    show_tables(cursor, "dbprodutos_v2")
    
    df = read_csv("data/tabela_produtos_2021_2029.csv")
    add_product_data(cnx, cursor, df, "dbprodutos_v2", "tb_produtos")