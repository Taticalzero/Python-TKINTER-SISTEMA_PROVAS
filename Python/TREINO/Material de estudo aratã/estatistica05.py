# Load the data
from sklearn.datasets import load_iris  ###O sklearn.datasetspacote incorpora alguns conjuntos de dados de brinquedos pequenos, conforme apresentado na seção Introdução .
iris = load_iris()

from matplotlib import pyplot as plt

# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: 
    iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], 
            c=iris.target) ##target = destino de uma lista
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout() ##tight_layout ajusta automaticamente os parâmetros de subparcela para que a subtrama se ajuste à área da figura
plt.show()

