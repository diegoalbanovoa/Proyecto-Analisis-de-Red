import os
import pandas as pd

# Define la ruta de los archivos CSV en crudo
raw_data_path = r"C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset en Crudo"

# Busca todos los archivos CSV en la ruta
csv_files = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]

# Crea una lista vacía para almacenar los DataFrames
dataframes = []

# Itera sobre cada archivo CSV y agrega su DataFrame a la lista
for csv_file in csv_files:
    file_path = os.path.join(raw_data_path, csv_file)
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    dataframes.append(df)

# Concatena todos los DataFrames en uno solo
final_df = pd.concat(dataframes, ignore_index=True)

# Define la ruta y el nombre del archivo final
output_path = r"C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Crudo Proceso de Clasificación\output.csv"

# Guarda el archivo final en la ruta especificada
final_df.to_csv(output_path, index=False)

print("Archivo final guardado en: ", output_path)


# Define la ruta y el nombre del archivo CSV generado
file_path = r"C:\Users\diego\Videos\Proyecto Analisis de Red\Proyecto-Analisis-de-Red\Dataset Crudo Proceso de Clasificación\output.csv"

# Carga el archivo CSV en un DataFrame de Pandas
df = pd.read_csv(file_path)

# Define una lista de protocolos de aplicación conocidos
app_protocols = ['HTTP', 'HTTPS', 'DNS', 'SMTP', 'FTP', 'SSH','RIP','SNMP']

# Filtra los resultados del conteo por los protocolos de aplicación conocidos
app_protocol_counts = df.loc[df['Protocol'].isin(app_protocols), 'Protocol'].value_counts()

# Imprime el resultado
print(app_protocol_counts)
