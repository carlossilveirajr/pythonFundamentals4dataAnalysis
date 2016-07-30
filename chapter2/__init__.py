
## Type usage

print(type(5))
print(type(5.0))
print(type("Eu"))

# Bar usage
print(4 / 5)
print(4 // 5)

# Hax and Bin
print(hex(1235))
print(bin(12))

# Abs and round
print(abs(-1))
print(round(3.141565, 2))

# type works directly with variable name.
# variable type change anytime it is needed.

# Strings are imitable -cannot replace values in-between.

# get part of string
string1 = "Data Analist"
print(string1[3:9])
print(string1[1:])
print(string1[-1])
print(string1[-5:-1])
print(string1[-1:-8])
print(string1[5:-1])

print(string1.split()) #by space by standard

# List

# Any kind of obj in the list.

a = ["Carlos", "Roberto", "Silveira", "Junior"]
del a[3]
print(a)

print("Carlos" in a)


"""
    Files

    a = open(file_name, mode)
    mode : r - read
           w - write
           a - append

    a.read(10) | a.seek(0) | a.write()

    a.close()
"""

"""
import pandas as pd

df = pd.read_csv("http:// .... ")


"""