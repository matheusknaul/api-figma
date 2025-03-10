import requests
import json

def get_json(ID_FILE, TOKEN):
    url = f"https://api.figma.com/v1/files/{ID_FILE}"
    headers = {"X-Figma-Token": TOKEN}
    request = requests.get(url, headers=headers)

    if request.status_code == 200:
        data = request.json()
        document = data['document']
        children = document['children']
        return children
    elif request.status_code == 403:
        print("Invalid token")
    elif request.status_code == 401:
        print("Token inválido ou não autorizado")
    else:
        print(f"Erro: {request.status_code} - {request.text}")

def get_components(json):
    pass
