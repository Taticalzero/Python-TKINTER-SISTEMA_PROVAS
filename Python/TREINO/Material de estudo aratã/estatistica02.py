import pandas
# carregando iris.csv
dados = pandas.read_csv('iris.csv')
# imprimindo os dez primeiros exemplos da base de dados
print(dados.head(10))


# calculando a media para todos os atributos
print(dados.mean())
# calculando a mediana para todos os atributos
print(dados.median())
# calculando percentil 15% para todos os atributos
print(dados.quantile(0.15))

print('=======================')
# calculando o intervalo para todos os atributos
print(dados.max(numeric_only=True) - dados.min(numeric_only=True))
print('=======================')
# calculando a variancia para todos os atributos
print(dados.var())
print('=======================')
# calculando o desvio-padrao para todos os atributos
# (na biblioteca pandas, ddof=1 por padrao)
print(dados.std())

# calculando a obliquidade para todos os atributos
#print(dados.skew())
# calculando a curtose para todos os atributos
#print(dados.kurtosis())

