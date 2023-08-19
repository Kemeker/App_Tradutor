import tkinter as tk
from tkinter import ttk
import requests
import uuid
import json

def translate_text():
    text_to_translate = input_text.get("1.0", "end-1c")
    
    if not text_to_translate:
        result_text.config(text="Nenhum texto inserido.")
        return
    
    body = [{
        'text': text_to_translate
    }]
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
    translated_text = response[0]['translations'][0]['text']
    target_language = response[0]['translations'][0]['to']
    
    result_text.config(text=f"Tradução: {translated_text}\nLíngua: {target_language}")

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

app = tk.Tk()
app.title("Tradutor")

input_label = ttk.Label(app, text="Digite o texto que deseja traduzir:")
input_label.pack(pady=10)

input_text = tk.Text(app, height=5, width=40)
input_text.pack()

translate_button = ttk.Button(app, text="Traduzir", command=translate_text)
translate_button.pack(pady=10)

result_text = ttk.Label(app, text="")
result_text.pack()

app.mainloop()

