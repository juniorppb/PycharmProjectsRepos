from random import randrange, seed
seed(10)
randrange(0,11)

notas_matematica = []
for nota in range(8):
    notas_matematica.append(randrange(0,11))
print (notas_matematica)
