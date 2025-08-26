from pathlib import Path
import pandas as pd

def read_csv(pandas_lib, file_name):
    '''función para lectura de csv con pandas'''
    path = Path(__file__).parent / file_name
    return pandas_lib.read_csv(path)