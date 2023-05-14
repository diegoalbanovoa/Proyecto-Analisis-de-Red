import pandas as pd
import os
import random

# Define la ruta del archivo CSV y la carpeta para guardar los nuevos archivos
csv_path = r'C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Crudo Proceso de Clasificación\output.csv'
folder_path = r'C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Proceso de Clasificación'

# Lee el archivo CSV en un DataFrame
df = pd.read_csv(csv_path)

# Elimina la columna "No."
df = df.drop('No.', axis=1)

# Crea la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Crea un diccionario para almacenar los DataFrames de cada protocolo
protocol_dfs = {}

# Filtra los resultados del conteo por los protocolos de aplicación conocidos
app_protocols = ['HTTP', 'DNS', 'TCP', 'FTP', 'ICMP', 'UDP']
for protocol in app_protocols:
    # Verifica si hay suficientes filas en el DataFrame para el protocolo actual
    if (df['Protocol'] == protocol).sum() <= 700:
        data = (df['Protocol'] == protocol).sum()
        print(data)
        print(f"No hay suficientes filas para el protocolo {protocol}")
        continue
    
    # Selecciona 700 filas aleatorias del DataFrame para cada protocolo
    random.seed(42)
    protocol_df = df.loc[df['Protocol'] == protocol].sample(n=700, random_state=42)
    protocol_dfs[protocol] = protocol_df

# Guarda cada DataFrame en un archivo CSV separado
for protocol, protocol_df in protocol_dfs.items():
    filename = f'{protocol.lower()}_output.csv'
    file_path = os.path.join(folder_path, filename)
    protocol_df.to_csv(file_path, index=False)