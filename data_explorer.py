import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

engine = create_engine("postgresql://postgres:admin@localhost:5432/learning_machines")

# Leitura dos dados com pandas e sqlalchemy
df_clientes = pd.read_sql("SELECT * FROM clientes", con=engine)
df_contas = pd.read_sql("SELECT * FROM contas", con=engine)
df_emprestimos = pd.read_sql("SELECT * FROM historico_emprestimos", con=engine)

df_completo = pd.merge(df_clientes, df_contas, left_on="id", right_on="id_cliente", suffixes=("cli", "_conta"))
df_final = pd.merge(df_completo, df_emprestimos, on="id_cliente", suffixes=("", "_emprestimo"))

print("Valores ausentes por coluna: ")
print(df_final.isnull().sum())

# Se existir nulos:
# df_final["renda_mensal"] = df_final["renda_mensal"].fillna(df_final["renda_mensal"].median())

# Remoção de duplicidades
df_final = df_final.drop_duplicates()

# Conversão de tipo de dado
df_final["idade"] = df_final["idade"].astype(int)

print("Resultado final:")
print(df_final.head())

# Leitura dos dados com pandas e pymongo
client = MongoClient("mongodb://localhost:27018/")
db = client["learning_machines"]
collection = db["feedbacks_sac"]

df = pd.DataFrame(list(collection.find({})))
print(df.head())