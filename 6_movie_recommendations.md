# 🎯 Taller - Recomendador de Películas usando Embeddings y OpenAI

## ✅ Objetivo
Crear un sistema de recomendación de películas utilizando **embeddings generados por OpenAI** y calcular la similitud entre las películas.

---

## 📌 1. ¿Qué son los embeddings?
Los embeddings son representaciones numéricas de textos que capturan su significado en un espacio vectorial. En este caso, obtendremos el embedding de la descripción de cada película.

![embeddings](imgs/sr1.svg)

---

## 📌 2. ¿Qué haremos?
✅ Generar el embedding de cada descripción de película  
✅ Guardar esos embeddings en un archivo JSON  
✅ Calcular la similitud entre películas  
✅ Hacer una recomendación a partir de un prompt del usuario

---

## 📌 3. Código Base Explicado
```python
from dotenv import load_dotenv
import json
import os
import numpy as np
from openai import OpenAI
```
- Se cargan librerías necesarias, incluida la API de OpenAI.

---

### ✅ Conexión a la API y carga de datos
```python
load_dotenv('api_keys.env')
client = OpenAI(api_key=os.environ.get('openai_api_key'))

with open('movie_descriptions.json', 'r') as file:
    movies = json.load(file)
```
- Se carga la API key y el archivo con las descripciones de las películas.

---

### ✅ Función para obtener el embedding de cada texto
```python
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding
```
- Esta función llama a la API y devuelve el embedding.

---

### ✅ Función para calcular la similitud de coseno
```python
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```
- La similitud de coseno nos indica qué tan parecidas son dos películas.

---

## 📌 4. Generación de embeddings por película
✅ Se recorre la base de datos y se agrega el embedding a cada película:
```python
for movie in movies:
    movie['embedding'] = get_embedding(movie['description'])
```

✅ Se guarda en un nuevo archivo:
```python
with open('movie_descriptions_embeddings.json', 'w') as file:
    json.dump(movies, file)
```

---

## 📌 5. Comparación de similitud entre películas
✅ Se seleccionan tres películas y se calcula la similitud entre ellas:
```python
print(f"Similitud entre {movies[27]['title']} y {movies[3]['title']}: {cosine_similarity(movies[27]['embedding'], movies[3]['embedding'])}")
print(f"Similitud entre {movies[27]['title']} y {movies[20]['title']}: {cosine_similarity(movies[27]['embedding'], movies[20]['embedding'])}")
```
Entre más alto el valor, más parecidas son.

---

## 📌 6. Recomendación a partir de un prompt
✅ Se define un prompt de ejemplo:
```python
prompt = "película de la segunda guerra mundial"
prompt_emb = get_embedding(prompt)
```

✅ Se calcula la similitud entre el prompt y cada película:
```python
similarities = [cosine_similarity(prompt_emb, movie['embedding']) for movie in movies]
idx = np.argmax(similarities)
print(f"La película recomendada es: {movies[idx]['title']}")
```

---

## ✅ 7. Entregable:
📸 **Captura de pantalla** mostrando la recomendación de la película más similar al prompt.  

---

## 📌 8. Nota:
✅ Este método permite crear un sistema de recomendación basado en similitud semántica.  
✅ Puedes cambiar el `prompt` para probar diferentes recomendaciones.

---
