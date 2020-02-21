import pandas as pd ##Pandas é fundamental para Análise de Dados.

example_series =  pd.Series([1,5,10,30,50,30,15,40,45])

print(example_series.mean())

print(example_series.median())

print(example_series.quantile()) ##O quantil é o valor abaixo do qual está um certo percentual dos dados. No caso da mediana, esse percentual é de 50%. 

print(example_series.quantile(q=0.25))


print(example_series.mode())

print(example_series.std())



##http://felipegalvao.com.br/blog/2016/03/31/estatistica-descritiva-com-python/