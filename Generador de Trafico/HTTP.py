import requests
import time

while True:
    # Hacer una solicitud HTTP GET
    url = 'http://httpbin.org/get'
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

    # Hacer una solicitud HTTP POST
    url = 'http://httpbin.org/post'
    data = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 30
    }
    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.text)

    # Hacer una solicitud HTTP PUT
    url = 'http://httpbin.org/put'
    data = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 30
    }
    response = requests.put(url, data=data)
    print(response.status_code)
    print(response.text)

    # Hacer una solicitud HTTP DELETE
    url = 'http://httpbin.org/delete'
    response = requests.delete(url)
    print(response.status_code)
    print(response.text)

    time.sleep(1)