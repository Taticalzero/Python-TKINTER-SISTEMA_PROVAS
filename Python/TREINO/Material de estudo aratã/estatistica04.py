import numpy    ### NumPy é uma poderosa biblioteca Python que é usada principalmente para realizar cálculos em Arrays Multidimensionais
from matplotlib import pyplot
# Notas na primeira prova
notas = numpy.array([2, 5, 7, 3, 5, 6, 5, 6, 6, 5, 5, 3])
pyplot.hist(notas, bins='auto')
pyplot.title('Histograma')
pyplot.ylabel('Frequencia')
pyplot.xlabel('Nota')
pyplot.show()

