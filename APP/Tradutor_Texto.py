"""
Tradutor_Texto: Um exemplo simples de tradução de texto usando a API da AWS Translate.
"""

import boto3

client = boto3.client('translate', region_name='us-east-1')

response = client.translate_text(
    Text='What is your name?',
    SourceLanguageCode='en',
    TargetLanguageCode='id'
)

print(response['TranslatedText'])