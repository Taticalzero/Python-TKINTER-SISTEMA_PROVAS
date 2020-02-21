import pandas
from matplotlib import pyplot

# carregando iris.csv
dados = pandas.read_csv('iris.csv')
# gerando bloxplot para os atributos da Iris
dados.plot(kind='box')

pyplot.show()
