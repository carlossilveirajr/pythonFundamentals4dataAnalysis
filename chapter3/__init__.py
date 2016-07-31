
# Example for number that are string
disciplina = input("Disciplina ")
nota_final = input("Nota final (0, 100): ")
semestre = input("semestre (1, 4)")

if disciplina == 'Matematica' and nota_final >= '50' and int(semestre) != 1:
    print("Você foi aprovado em %s com nota de %r" %(disciplina, nota_final))
else:
    print("Sinto muito")


# exercício
listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)