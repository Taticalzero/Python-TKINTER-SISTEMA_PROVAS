import pandas  as pd
dados = pd.read_csv('iris.csv')
print(dados.head(10))

print(dados.mean())

print(dados.median())

print(dados.quantile(0.15))

print('=========================')

