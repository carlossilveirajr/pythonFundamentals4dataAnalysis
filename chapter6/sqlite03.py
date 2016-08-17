import sqlite3
import random
import time
import datetime

conn = sqlite3.connect('dsa.db')

c = conn.cursor()

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

def data_insert_var():
    new_data = datetime.datetime.now()
    new_prod = 'monitor'
    new_valor = random.randrange(50, 100)

    c.execute("Insert into produtos (date, prod_name, valor) values (?, ?, ?)",
              (new_data, new_prod, new_valor))
    conn.commit()

for i in range(10):
    data_insert_var()
    time.sleep(1)

c.close()
conn.close()