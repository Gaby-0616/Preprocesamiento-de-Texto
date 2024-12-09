"""
Creado automáticamente en Colab.

El archivo original está ubicado en:
    https://colab.research.google.com/drive/1y0g_ju-hNpo15cCuO_2ixds0mvWPLm5k
"""

# Eliminar caracteres especiales
def eliminar_caracteres_especiales(cadena):
    limpio = ''.join(caracter for caracter in cadena if caracter.isalnum() or caracter == ' ')
    return limpio

# Convertir a minúsculas
def convertir_a_minusculas(cadena):
    return cadena.lower()

# Dividir texto en palabras
def dividir_en_palabras(cadena, separador=' '):
    return cadena.split(separador)

import requests

def obtener_lista_stopwords(url):
    respuesta = requests.get(url)
    palabras_stop = respuesta.text.split('\n')[:-1]
    return palabras_stop

# Filtrar palabras vacías
def filtrar_palabras_vacias(palabras, palabras_vacias):
    return [palabra for palabra in palabras if palabra not in palabras_vacias]

# Aplicar reducción morfológica (stemming)
from nltk.stem import PorterStemmer

def aplicar_stemming(palabras):
    stemmer = PorterStemmer()
    palabras_raiz = [stemmer.stem(palabra) for palabra in palabras]
    return palabras_raiz

# Procesar texto

# Idiomas disponibles: https://github.com/Alir3z4/stop-words
IDIOMA = 'spanish'
URL_STOPWORDS = f'https://raw.githubusercontent.com/Alir3z4/stop-words/refs/heads/master/{IDIOMA}.txt'

TEXTO_INICIAL = "Este es un ejemplo de texto que contiene algunos caracteres especiales, números y palabras en mayúsculas. Queremos preprocesar este texto para que esté listo para el análisis de texto en un proyecto de Procesamiento de Lenguaje Natural (NLP)."

texto_procesado = eliminar_caracteres_especiales(TEXTO_INICIAL)
texto_procesado = convertir_a_minusculas(texto_procesado)
palabras = dividir_en_palabras(texto_procesado)

stopwords = obtener_lista_stopwords(URL_STOPWORDS)
palabras_filtradas = filtrar_palabras_vacias(palabras, stopwords)
palabras_reducidas = aplicar_stemming(palabras_filtradas)

palabras_reducidas

