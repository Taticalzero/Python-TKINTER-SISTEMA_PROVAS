import numpy
from matplotlib import pyplot

notas = numpy.array([2,5,7,3,5,6,5,6,6,5,5,3])
pyplot.hist(notas,bins = 'auto')
pyplot.title('Histograma')
pyplot.ylabel('Frequencia')
pyplot.xlabel('Nota')
pyplot.show()