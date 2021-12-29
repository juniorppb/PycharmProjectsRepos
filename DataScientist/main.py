import pandas as pd

#carregue o conjunto de dados chamado *nome do arquivo que vai importar, do HD
#funcao - read_csv()
#biblioteca - pandas

data = pd.read_csv('datasets/kc_house_data.csv')
#print(data.head()

# mostre na tela o numero de colunas e linhas do conjunto de dados
#print(data.shape)

#mostre na tela o nome das colunas do conjunto de dados
print(data.columns)

# mostre na tela o conjunto de dados ordenados pela coluna price
#print(data[['id','price']].sort_values('price'))

#mostre na tela o conjunto de dados ordenados pela coluna price do maior para o menor
#print(data[['id', 'price']].sort_values('price', ascending=False))

print(data[['waterfront', 'price']].sort_values('price', ascending=False))
