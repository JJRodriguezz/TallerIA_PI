
# 🌟 Generación y almacenamiento de embeddings en la base de datos

## 🔗 ¿Por qué almacenar los embeddings en la base de datos?

Para construir un sistema de recomendación eficiente, es necesario **almacenar los embeddings de cada película**. Esto permite que, en lugar de calcular el embedding cada vez que se hace una búsqueda, podamos comparar rápidamente los vectores ya almacenados.

En sistemas reales, normalmente se utilizan **bases de datos vectoriales** como **Pinecone**, **FAISS** o **Weaviate** que están optimizadas para realizar búsquedas rápidas por similitud. 

En este taller, aprenderemos a almacenar los embeddings **directamente en la base de datos por defecto de Django** (SQLite o PostgreSQL) usando un campo binario, lo que nos permite:

✅ Evitar instalar una base de datos vectorial externa  
✅ Controlar completamente el proceso de almacenamiento y recuperación  
✅ Entender el proceso desde cero

---

## 🔗 Modificación del modelo Movie

Para almacenar los embeddings en la base de datos, primero debemos modificar el modelo **Movie** agregando un nuevo campo de tipo **BinaryField** que permita guardar el vector como datos binarios.

Ejemplo de modelo actualizado:

```python
from django.db import models
import numpy as np

def get_default_array():
    default_arr = np.random.rand(1536)
    return default_arr.tobytes()

class Movie(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    emb = models.BinaryField(default=get_default_array())

    def __str__(self): 
        return self.title
```

✅ Recuerda que cada que modifiques el modelo debes ejecutar:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📅 ¿Por qué almacenar los embeddings como binarios?

Los embeddings son vectores de números (floats). Como las bases de datos relacionales no almacenan directamente arrays, convertimos el array en un archivo binario:

```python
import numpy as np

# Crear embedding binario
embedding_array = np.array([0.1, 0.2, 0.3])
binary_data = embedding_array.tobytes()

# Leer embedding desde binario
recovered_array = np.frombuffer(binary_data, dtype=np.float32)
```

De esta forma, podemos almacenar el vector como un campo **BinaryField** y recuperarlo cuando sea necesario para calcular similitudes.

---

## 🔄 Generar y almacenar embeddings desde la API de OpenAI

Hemos creado el comando `generate_embeddings` que:

✅ Recorre cada película en la base de datos  
✅ Genera el embedding usando la descripción de la película  
✅ Guarda el embedding como binario en el campo `emb`

### 🔄 Ejecución:
```bash
python manage.py generate_embeddings
```

### 🔄 Resultado esperado:
```
Found 50 movies in the database
👌 Embedding stored for: The Matrix
👌 Embedding stored for: Interstellar
...
🌟 Finished generating embeddings for all movies
```

---

## 🔄 Verificación de los embeddings

Para validar que los embeddings se almacenaron correctamente, puedes crear un comando que recorra las películas y recupere el array:

```python
for movie in Movie.objects.all():
    embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
    print(movie.title, embedding_vector[:5])  # Muestra los primeros valores
```

---

## ✅ Resultado
Tendrás cada película con su embedding almacenado y listo para hacer recomendaciones por similitud.

A partir de este punto, cualquier recomendación se puede hacer comparando los embeddings directamente desde la base de datos.

---

## 📚 Nota:
De forma opcional, podrías generar los embeddings usando otros modelos como Gemini (ver archivo `movie_descriptions_gemini.py`), pero para este taller trabajamos con OpenAI.

---
