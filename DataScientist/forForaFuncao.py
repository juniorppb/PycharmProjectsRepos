idades = [18, 22, 15, 50]

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print(f'{idade} anos de idade, TEM permissão para dirigir.')
  else:
    print(f'{idade} anos de idade, NÃO TEM permissão para dirigir.')

for idade in idades:
  verifica_se_pode_dirigir(idade)
