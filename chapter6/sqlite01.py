
#import do modulo
import sqlite3

con = sqlite3.connect("escola.db") ## cria ou abre

print(type(con)) # conection sqlite3

cur = con.cursor() # cursor pra navegacao dos registros

print(type(cur)) # conection sqlite3

sql_create = 'create table cursos '\
    '(id integer primary key, '\
    'titulo varchar(100), ' \
    'categoria varchar(140) )'

cur.execute(sql_create) #executa sql

sql_insert = 'insert into cursos values (?, ?, ?)'

recset = [(1000, "Ciência dos dados", 'data science'),
          (1001, "Big data Fundations", 'Big data'),
          (1002, "python fundamentos", 'analise')]

for rec in recset:
    cur.execute(sql_insert, rec)

sql_select = 'select * from cursos'

cur.execute(sql_select) # select dos dados e fica em cursor

dados = cur.fetchall() # passa tudo que pegou no banco para dados

for linha in dados:
    print("Curso %d, título %s, Categoria %s\n" %linha)

recset = [(1003, "asdfadf234", 'jeyf'),
          (1004, "asdfa", 'asdf ')]

for rec in recset:
    cur.execute(sql_insert, rec)

cur.execute('select * from cursos') # select dos dados e fica em cursor

dados = cur.fetchall() # passa tudo que pegou no banco para dados

for linha in dados:
    print("Curso %d, título %s, Categoria %s\n" %linha)

con.close() #fecha conexão