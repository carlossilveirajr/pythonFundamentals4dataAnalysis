
import sqlite3

conn = sqlite3.connect('dsa.db')

c = conn.cursor()

#criando funcao

def create_table():
    c.execute('Create table if not exists produtos (' \
              'id integer primary key autoincrement not null, '\
              'date text,' \
              'prod_name text, '\
              'valor real)')

def insert_data():
    c.execute("Insert into produtos values (10, '2016-05-12 14:32:11', 'Teclado', 90)")
    conn.commit()
    c.close()
    conn.close()


create_table()

insert_data()