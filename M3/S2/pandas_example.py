import pandas as pd

serie = pd.Series([1,2,3])
print(serie)    

serie_diccionario = pd.Series({'Manzana':5, 'Pera':10})
print(serie_diccionario)

#acceso a series con label o indice
print(serie[0])#1
print(serie_diccionario['Manzana'])#5
print(serie_diccionario[['Manzana', 'Pera']])#5 y 10

#operaciones 
print(f'mean: {serie.mean()}')
print(f'número máximo: {serie.max()}')
print(f'número mínimo: {serie.min()}')
