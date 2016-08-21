##
## importar um modulo (do arquivo meu_modulo.py
##      import meu_modulo
##
## importar funcao
##      from math import funcao
##

import math  #importa tudo de math

print(dir(math))

print(math.sqrt(25))

from math import sqrt # importa so sqrt

print(sqrt(15))

print(help(sqrt))

from random import choice

print(choice(["Maça", "Banana", "Uva"]))

## modules
##  statistics, os, sys,

import sys
print(sys.version)




#importando pacote
import urllib.request

resposta = urllib.request.urlopen('http://python.org')

print(resposta)

html = resposta.read()

print(html)




import matplotlib.pyplot as plt
import pandas

from functools import reduce


#list comprehension

x_ = (x for x in range(100) if x % 2 == 0)
print(list(x_))

lst = [x ** 2 for x in [x + 1 for x in range(11)]]
print(lst)

print(type([]))
print(type({}))
print(type(()))


for indice, item in enumerate("Carlos"):
    print("indece %i item %s" %(indice, item))
