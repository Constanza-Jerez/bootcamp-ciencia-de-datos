1. Instalar miniconda enviroment
https://www.anaconda.com/download/success

2. Extension Jupiter notebook
https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

3. Verificar la instalación del aplicativo anaconda prompt
- Buscar en el sistema la app Anaconda prompt
- Abrir aplicativo
- Se abrira con una ruta (base) C:Users\user
- Escribir `conda info --envs`
- Aparecera un solo enviroment instalado (base)

4. Ejecutar en la terminal de vs code `pip list` para listar paquetes
5. Debe mostrar aunque sea estos paquetes
```
anaconda-anon-usage      0.7.0
annotated-types          0.6.0
archspec                 0.2.3
boltons                  24.1.0
Brotli                   1.0.9
certifi                  2025.4.26
cffi                     1.17.1
charset-normalizer       3.3.2
colorama                 0.4.6
conda                    25.3.1
```

6. Ejecutar la instalación de paquetes en la terminal si aparecen los paquetes anteriores
- `pip install numpy`
- `pip install pandas`
- `pip install matplotlib`
- `pip install seaborn`
- `pip install statsmodels`
- `pip install ipykernel`