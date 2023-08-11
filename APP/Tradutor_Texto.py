import requests

url = "https://text-translator2.p.rapidapi.com/translate"

querystring = {
    "source_language": "en",
    "target_language": "10",
    "text": "What is your name?"
}

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "f8a3611d6bmsh9bf6eaf4ebe3e75p13f3adjsn1422b4650143",
    'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)