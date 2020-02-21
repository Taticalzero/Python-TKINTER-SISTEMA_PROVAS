import pandas as pd

example_series = pd.Series([1,5,10,30,50,30,15,40,45])

print(example_series.mean())

print(example_series.median())

print(example_series.quantile())

print(example_series.quantile(q=0.25))

print(example_series.mode())

print(example_series.std())