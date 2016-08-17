from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

print(type(conn))

#criando cadastro db
db = conn.cadastrodb

print(type(db))

# criando coleção
collection = db.cadastrodb
print(type(conn))

# coleção e banco é criado só com a inserção do primeiro documento

import datetime

post1 = { "codigo": 'id-123',
          "prod" : 'asdf',
          "marcas": ["m1", "m2", "m3"],
          "data_cadastro": datetime.datetime.utcnow()}

print(type(post1))

collection = db.posts

#create a post id
post_id = collection.insert_one(post1)

#executando inserção
print(post_id.inserted_id)


post2 = { "codigo": 'id-1233',
          "prod" : 'asdf1234',
          "marcas": ["m112", "m2123", "m314"],
          "data_cadastro": datetime.datetime.utcnow()}
collection = db.posts
post_id = collection.insert_one(post2).inserted_id

print(post_id)

# retornando
print(collection.find_one({"prod": "asdf1234"}))

for post in collection.find():
    print(post)

#pegando nome do banco
print(db.name)

print(db.collection_names())

