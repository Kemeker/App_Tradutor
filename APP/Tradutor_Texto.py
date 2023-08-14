"""
Tradutor_Texto: Um exemplo simples de tradução de texto usando a API da AWS Translate.
"""

import boto3

client = boto3.client('translate')

response = client.translate_text(
    Text='What is your name?',
    SourceLanguageCode='en',
    TargetLanguageCode='id'
)

print(response['TranslatedText'])