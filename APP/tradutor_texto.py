import requests
import uuid
import json

key = "7c754b7ab1c94a64baae701ad7ba2f3a"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "southcentralus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'zu']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Solicita ao usuário que insira o texto a ser traduzido
text_to_translate = input("Digite o texto que deseja traduzir: ")

# Verifica se o usuário inseriu algum texto
if not text_to_translate:
    print("Nenhum texto inserido. Encerrando...")
else:
    body = [{
        'text': text_to_translate
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
