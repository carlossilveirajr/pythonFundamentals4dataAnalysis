import sqlite3

# to plot graphics
# import matplotlib.pyplot as plt
# %matplotlib notebook

conn = sqlite3.connect('dsa.db')

c = conn.cursor()

c.execute("select * from produtos ")

for i in c.fetchall():
    print(i)

c.execute("select * from produtos where valor > 60")

for i in c.fetchall():
    print(i)


#restringindo a coluna
c.execute("select * from produtos where valor > 60")

for i in c.fetchall():
    print(i[3])


# plot a bar graphic
# def dados_grafico():
#     c.execute("select id, valor from produtos")
#     ids = []
#     value = []
#     for linhas in c.fetchall():
#         ids.append(linhas[0])
#         value.append(linhas[1])
#
#     plt.bar(ids, value)
#     plt.show()

c.close()
conn.close()