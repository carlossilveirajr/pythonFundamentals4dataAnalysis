
## tratamento de erro

try:
    8 + 's'
    print("e ai?")
except TypeError:
    print("erro")
finally:
    print("oi")

try:
    f = open("testerror", 'w')
    f.write("grave no arquivo")
except IOError:
    print("Error de IO")
except:
    print("uma excecao qualquer")
else:
    print("gravado")
    f.close()
finally:
    print("mesmo de tiver excecao")


import os

text = "Carlos Roberto Silveira Junior"

arquivo = open(os.path.join("cientista.txt", 'w'))
for palavra in text.split():
    arquivo.write(palavra)

arquivo.close()

arquivo = open(os.path.join("cientista.txt", 'r'))
text = arquivo.read()
arquivo.close()

print(text)




with open("cientista.txt", 'r') as arquivo:
    text = arquivo.read()

print(text)


