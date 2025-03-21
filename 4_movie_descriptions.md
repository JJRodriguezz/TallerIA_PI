# 🎬 Enriquecimiento de Descripciones de Películas con la API de OpenAI

## ✅ Objetivo
Aprenderás a utilizar la API de OpenAI en un proyecto Django para enriquecer las descripciones de las películas en la base de datos.

---

## 📌 1. Configurar la conexión con la API de OpenAI (OPCIONAL - SOLO CONSULTA)
Esta sección es para que entiendas cómo funciona la conexión, **NO es necesario que la ejecutes**.

### 🔑 Pasos:
- Crear un archivo `.env` con la API Key:
```
openai_apikey=sk-xxxxxxxxxxxxxxxxxxxx
```
- Código de conexión:
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('../openAI.env')
client = OpenAI(api_key=os.environ.get('openai_apikey'))
```

✅ Esto permite conectarse de forma segura a la API.

---

## 📌 2. Preparar el Prompt y consultar la API (OPCIONAL - SOLO CONSULTA)
Ejemplo de la instrucción (prompt) enviada a la API:
```python
instruction = (
    "Vas a actuar como un aficionado del cine que sabe describir de forma clara, "
    "concisa y precisa cualquier película en menos de 200 palabras. La descripción "
    "debe incluir el género de la película y cualquier información adicional que sirva "
    "para crear un sistema de recomendación."
)
```

---

## 📌 3. Recorrer la base de datos y generar descripciones (OPCIONAL - SOLO CONSULTA)
Este paso es costoso y **NO debe ser ejecutado**. Lo mostramos para que conozcas el proceso.

```python
movies = Movie.objects.all()
for movie in movies:
    prompt = f"{instruction} Actualiza la descripción '{movie.description}' de la película '{movie.title}'"
    response = get_completion(prompt)
    movie.description = response
    movie.save()
```

### 📥 El código está en: [update_descriptions.py](update_descriptions.py)

### 📥 Este proceso debe realizarse como un **comando de Django dentro de la app `movie`**, ubicado en:
```
movie/management/commands/update_descriptions.py
```
Y ejecutarlo así (solo si fuera necesario):
```bash
python manage.py update_descriptions
```

✅ Sin embargo, este comando **ya fue ejecutado por el equipo docente** y se entrega solo para consulta.

---

## 🚨 4. ¿Qué hicimos nosotros por ti?
✅ Ya ejecutamos el proceso completo con la API.  
✅ Generamos el archivo **`updated_movie_descriptions.csv`** con todas las descripciones actualizadas.

---

## 📌 5. ¿Qué debes hacer tú? (OBLIGATORIO)

### ✅ Crear el comando de Django `update_movies_from_csv`
Ubícalo en:
```
movie/management/commands/update_movies_from_csv.py
```

### ✅ Ejecuta el comando:
```bash
python manage.py update_movies_from_csv
```

Este comando:
- Lee el CSV
- Busca cada película por título en la base de datos
- Actualiza la descripción

✅ Al finalizar, tendrás las descripciones enriquecidas en tu base de datos.

---

## 📂 6. Estructura del CSV entregado
El archivo contiene:

| Title           | Updated Description                 |
|-----------------|-------------------------------------|
| Movie Title 1   | Descripción generada por OpenAI ... |
| Movie Title 2   | Descripción generada por OpenAI ... |

---

## 💻 7. Ejemplo de ejecución (OBLIGATORIO):
```bash
python manage.py update_movies_from_csv
```
Salida esperada:
```
Found 50 movies in CSV
Processing: The Matrix
Updated: The Matrix
...
Finished updating 50 movies from CSV.
```

---

## 📌 8. Archivo adicional (OPCIONAL - NO EJECUTAR)
También se entrega el comando `update_and_export_movies.py` que permite:
- Recorrer las películas
- Consultar la API
- Crear un nuevo CSV

⚠️ *Este comando es solo de referencia y **NO debe ejecutarse**.*

```bash
python manage.py update_and_export_movies
```

---

## 📌 9. Resumen Final:
| Paso | Acción | ¿Obligatorio? |
|-----|--------|--------------|
| 1   | Conectar a la API (revisar) | ❌ Opcional |
| 2   | Preparar y enviar prompts   | ❌ Opcional |
| 3   | Generar CSV con la API      | ❌ Opcional |
| 4   | Usar el CSV para actualizar la BD | ✅ Sí, obligatorio |

---

✅ Con esto garantizamos que todos trabajen con los mismos datos y minimizamos costos de uso de la API.
