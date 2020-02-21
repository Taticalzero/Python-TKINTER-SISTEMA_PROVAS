import pandas
from matplotlib import pyplot

dados = pandas.read_csv('iris.csv')

dados.plot(kind="box")

pyplot.show()