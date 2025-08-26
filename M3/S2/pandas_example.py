import pandas as pd

serie = pd.Series([1,2,3])
print(serie)

serie_diccionario = pd.Series({'Manzana':5, 'Pera': 10})
print(serie_diccionario)

# acceso a series con label o indice
print(f'acceso con indice: {serie[0]}') # 1
print(f'acceso por label o clave: {serie_diccionario['Manzana']}') # 5
print(serie_diccionario[['Manzana', 'Pera']]) # accede al label (clave) y valor

# filtrado
print(f'filtrado: {serie[serie == 2]}')
print(f'filtrado: {serie[serie > 1]}')


# operaciones

print(f' mean: {serie.mean()}')
print(f' max: {serie.max()}')
print(f' min: {serie.min()}')