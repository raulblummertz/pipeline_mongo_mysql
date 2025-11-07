from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
uri_mongo = f"mongodb+srv://raulblummertz:{db_password}@cluster-pipeline.jzk8vg0.mongodb.net/?appName=Cluster-pipeline"



def visualize_collection(col):
    for doc in col.find():
        print(doc)

def rename_column(col, col_name, new_name): 
    col.update_many({}, {"$rename": {f"{col_name}": f"{new_name}"}})

def select_category(col, category):
    query = {"Categoria do Produto": f"{category}"}
    lista_categoria = []
    for doc in col.find(query):
        lista_categoria.append(doc)
    return lista_categoria

def make_regex(col, regex):
    query = {"Data da Compra": {"$regex": f"{regex}"}}
    lista_regex = []
    for doc in col.find(query):
        lista_regex.append(doc)
    return lista_regex

def create_dataframe(lista):
    df = pd.DataFrame(lista)
    return df 

def format_date(df): 
    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
    df["Data da Compra"] = df["Data da Compra"].dt.strftime("%Y-%m-%d")

def save_csv(df, path):
    df.to_csv(f"{path}", index=False)
    return



if __name__ == "__main__":
    
    client = connect_mongo(uri_mongo)
    db = create_connect_db(client, "db_produtos_desafio")
    col = create_connect_collection(db, "produtos") 
    
    rename_column(col, "lat", "Latitude")
    rename_column(col, "lon", "Longitude")

    lst_livros = select_category(col, "livros")
    df_livros = create_dataframe(lst_livros)
    format_date(df_livros)
    save_csv(df_livros, "/home/monza/Documentos/pipeline_python_mongo_mysql/data_teste/tb_livros.csv")

    lst_produtos = make_regex(col, "/202[1-9]")
    df_produtos = create_dataframe(lst_produtos)
    format_date(df_produtos)
    save_csv(df_produtos, "/home/monza/Documentos/pipeline_python_mongo_mysql/data_teste/tb_produtos.csv")