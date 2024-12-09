# -*- coding: utf-8 -*-
"""stemming.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y0g_ju-hNpo15cCuO_2ixds0mvWPLm5k
"""

# Remove special characters
def remove_special_characters(text):
  result = ''.join(letter for letter in text if (letter.isalnum() or letter == ' '))
  return result

# Convert to lowercase
def convert_to_lowercase(text):
  return text.lower()

# Tokenize
def tokenize(text, sep=' '):
  return text.split(sep)

import requests

def get_stopwords(url):
  response = requests.get(STOPWORDS_URL)
  stopwords = response.text
  stopwords = stopwords.split('\n')[:-1]
  return stopwords

# Remove stopwords
def remove_stopwords_from_tokens(tokens, stopwords):
  return [token for token in tokens if token not in stopwords]

# Apply stemming
from nltk.stem import PorterStemmer


def stem(tokens):
  ps = PorterStemmer()

  stems = [ps.stem(token) for token in tokens]
  return stems

# Process text

# Available langs: https://github.com/Alir3z4/stop-words
LANG = 'spanish'
STOPWORDS_URL = f'https://raw.githubusercontent.com/Alir3z4/stop-words/refs/heads/master/{LANG}.txt'

TEXT = "Este es un ejemplo de texto que contiene algunos caracteres especiales, números y palabras en mayúsculas. Queremos preprocesar este texto para que esté listo para el análisis de texto en un proyecto de Procesamiento de Lenguaje Natural (NLP)."

text = remove_special_characters(TEXT)
text = convert_to_lowercase(text)
tokens = tokenize(text)

stopwords = get_stopwords(STOPWORDS_URL)
tokens = remove_stopwords_from_tokens(tokens, stopwords)
stems = stem(tokens)
stems