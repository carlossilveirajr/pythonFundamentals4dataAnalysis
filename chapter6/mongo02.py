import pymongo

client_con = pymongo.MongoClient()

# pega bancos disponiveis
print(client_con.database_names())

# conectando o banco cadastro db
db = client_con.cadastrodb

# achando collections
print(db.collection_names())

db.create_collection("mycollection")
print(db.collection_names())

#inserindo documento
db.mycollection.insert_one({"titulo" : "python", "document": "algo"})

#pegando o inserido
print(db.mycollection.find_one())




col = db["mycollection"]

print(type(col))

col.count()

rec = col.find_one()

print(rec)

