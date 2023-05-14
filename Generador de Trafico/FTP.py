import ftplib
import random
import string
import os
import time

# Conectarse al servidor FTP local
ftp_server = ftplib.FTP()
ftp_server.connect('localhost', 21)
ftp_server.login('usuario', 'contraseña')

# Definir la ruta completa de la carpeta C:\ftp
ftp_directory = r'C:\ftp'
letters = string.ascii_lowercase

# Ciclo infinito para crear, eliminar y modificar archivos de manera aleatoria
MAX_FILES = 100  # Limitar el número máximo de archivos
files_created = 0
while True:
    # Salir del ciclo si se han creado el número máximo de archivos
    if files_created >= MAX_FILES:
        print(f'Se han creado {MAX_FILES} archivos. Saliendo del ciclo.')
        break

    # Generar un número aleatorio para determinar la acción a realizar
    action = random.randint(1, 3)

    # Crear un archivo aleatorio
    if action == 1:
        # Generar un nombre de archivo aleatorio
        filename = ''.join(random.choice(letters) for i in range(10)) + '.txt'
        # Crear la ruta completa del archivo en la carpeta C:\ftp
        filepath = os.path.join(ftp_directory, filename)
        # Crear un archivo con el nombre generado
        with open(filepath, 'w') as f:
            f.write('Este es un archivo de prueba.')
        # Subir el archivo al servidor FTP
        with open(filepath, 'rb') as f:
            ftp_server.storbinary(f'STOR {filename}', f)
        print(f'Se creó el archivo {filename} en la carpeta {ftp_directory} y se subió al servidor FTP.')
        files_created += 1  # Incrementar el contador de archivos creados

    # Eliminar un archivo aleatorio
    elif action == 2:
        if len(ftp_server.nlst()) > 0:
            # Obtener una lista de los archivos en el directorio remoto
            files = ftp_server.nlst()
            # Seleccionar un archivo aleatorio de la lista
            filename = files[len(files)-1]
            # Eliminar el archivo del servidor FTP
            ftp_server.delete(filename)
            # Eliminar el archivo localmente si existe
            filepath = os.path.join(ftp_directory, filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f'Se eliminó el archivo {filename} localmente.')
            # Imprimir un mensaje si el archivo no existe localmente
            else:
                print(f'No se puede eliminar el archivo {filename} localmente porque no existe.')
            print(f'Se eliminó el archivo {filename} del servidor FTP y localmente.')

    # Modificar un archivo aleatorio
    else:
        if len(ftp_server.nlst()) > 0:
            # Obtener una lista de los archivos en el directorio remoto
            files = ftp_server.nlst()
            # Seleccionar un archivo aleatorio de la lista
            filename = files[len(files) - 1]
            # Descargar el archivo desde el servidor FTP
            with open(os.path.join(ftp_directory, filename), 'wb') as f:
                ftp_server.retrbinary(f'RETR {filename}', f.write)
            # Modificar el archivo localmente
            with open(os.path.join(ftp_directory, filename), 'a') as f:
                f.write('\nEsta línea se agregó de manera aleatoria.')
            # Cargar el archivo modificado al servidor FTP
            with open(os.path.join(ftp_directory, filename), 'rb') as f:
                ftp_server.storbinary(f'STOR {filename}', f)
            print(f'Se modificó el archivo {filename} en la carpeta {ftp_directory} y se actualizó en el servidor FTP.')

    # Esperar un tiempo aleatorio antes de la siguiente iteración
    time.sleep(random.randint(1, 2))

# Cerrar la conexión al servidor FTP local
ftp_server.quit()