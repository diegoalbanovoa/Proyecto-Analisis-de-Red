import os
import random
import pandas as pd

# Define la ruta de la carpeta que contiene los archivos CSV
folder_path = r'C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Proceso de Clasificación'

# Crea una lista vacía para almacenar los DataFrames de cada archivo CSV
dfs = []

# Lee cada archivo CSV en un DataFrame y agrégalo a la lista
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatena los DataFrames en uno solo
df = pd.concat(dfs, ignore_index=True)

# Mezcla las filas del DataFrame de forma pseudoaleatoria
random.seed(42)
df = df.sample(frac=1).reset_index(drop=True)

# Guarda el DataFrame mezclado en un archivo CSV
mixed_csv_path = r'C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Analisis de redes\dataset.csv'
df.to_csv(mixed_csv_path, index=False)