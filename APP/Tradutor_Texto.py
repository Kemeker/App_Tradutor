import requests

# Defina a URL da API de tradução da Azure
url = "https://api.cognitive.microsofttranslator.com/"

# Substitua 'SUA_CHAVE_AQUI' pela sua Chave do Assinante
subscription_key = '7c754b7ab1c94a64baae701ad7ba2f3a'

# Defina o texto e o idioma de origem e destino
text_to_translate = "What is your name?"
source_language = "en"
target_language = "id"

# Parâmetros de consulta
params = {
    "api-version": "3.0",
    "from": source_language,
    "to": target_language
}

# Cabeçalhos da requisição
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

# Corpo da requisição
body = [{"text": text_to_translate}]

# Envie a requisição POST
response = requests.post(url, params=params, headers=headers, json=body)

# Obtenha a tradução do corpo da resposta
translation = response.json()[0]["translations"][0]["text"]

# Imprima a tradução
print(f"Tradução: {translation}")
