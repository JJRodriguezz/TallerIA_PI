# 🎬 Enriquecimiento de Descripciones de Películas con la API de OpenAI

## ✅ Objetivo
Aprenderás a utilizar la API de OpenAI en un proyecto Django para enriquecer las descripciones de las películas en la base de datos.

---

## 📌 1. Conexión con la API de OpenAI (OPCIONAL - SOLO CONSULTA)
Esta sección es para que comprendas cómo se configura y conecta el proyecto a la API de OpenAI.

### 🔑 ¿Qué necesitas?
1. Crear un archivo `.env` donde almacenes tu API Key de forma segura:
```
openai_apikey=sk-xxxxxxxxxxxxxxxxxxxx
```
2. Cargar esa clave en tu código usando la librería `dotenv`.

### ✅ Código de conexión explicado:
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv('../openAI.env')

# Inicializa el cliente de OpenAI con la API Key
client = OpenAI(api_key=os.environ.get('openai_apikey'))
```
- `load_dotenv()` carga las variables del archivo `.env`
- `OpenAI()` crea el cliente para hacer las solicitudes a la API

---

## 📌 2. Función auxiliar para obtener la respuesta de la API (OPCIONAL - SOLO CONSULTA)
Creamos una función `get_completion()` que se encarga de:
✅ Recibir el `prompt` como entrada  
✅ Armar la estructura de la conversación requerida por la API  
✅ Hacer la consulta y devolver solo el texto generado

```python
def get_completion(prompt, model="gpt-3.5-turbo"):
    # Define el mensaje con el rol 'user' y el contenido que enviamos
    messages = [{"role": "user", "content": prompt}]
    
    # Llama a la API con el modelo y los mensajes
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Controla la creatividad (0 = más preciso)
    )
    
    # Retorna solo el contenido de la respuesta generada
    return response.choices[0].message.content.strip()
```

### 🔎 ¿Por qué usamos una función?
- Centraliza la llamada a la API
- Permite cambiar el modelo o parámetros fácilmente
- Facilita el reuso en un ciclo `for` sobre las películas

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

Este fragmento recorre todas las películas de la base de datos y actualiza su descripción usando una IA (como GPT).

¿Qué hace cada parte?

    Movie.objects.all(): Obtiene todas las películas de la base de datos.

    for movie in movies: Recorre cada película.

    prompt: Construye el mensaje para la IA con el título y la descripción actual.

    get_completion(prompt): Llama a la IA y genera una nueva descripción.

    movie.description = response: Actualiza la descripción.

    movie.save(): Guarda el cambio en la base de datos.

### 📥 Este proceso debe realizarse como un **comando de Django dentro de la app `movie`**, ubicado en:
```
movie/management/commands/update_descriptions.py
```
Y ejecutarlo así (solo si fuera necesario):
```bash
python manage.py update_descriptions
```

✅ Sin embargo, este comando **ya fue ejecutado por el equipo docente** y se entrega solo para consulta.


🔎 Para consulta, el código lo pueden encontrar en el archivo [update_descriptions.py](update_descriptions.py)
---


## 🚨 4. ¿Qué hicimos nosotros por ti?
✅ Ya ejecutamos el proceso completo con la API utilizando el comando [update_and_export_movies.py](update_and_export_movies.py).  
✅ Como resultado, generamos el archivo [updated_movie_descriptions.csv](updated_movie_descriptions.csv) con todas las descripciones actualizadas.


---

## 📌 5. ¿Qué debes hacer tú? (OBLIGATORIO)

### ✅ Crear el comando de Django `update_movies_from_csv`
Ubícalo en:
```
movie/management/commands/update_movies_from_csv.py
```

El código base del comando es el siguiente:

```python
import os
import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie descriptions in the database from a CSV file"

    def handle(self, *args, **kwargs):
        # 📥 Ruta del archivo CSV con las descripciones actualizadas
        csv_file = 'updated_movie_descriptions.csv'  # ← Puedes cambiar el nombre si es necesario

        # ✅ Verifica si el archivo existe
        if not os.path.exists(csv_file):
            self.stderr.write(f"CSV file '{csv_file}' not found.")
            return

        updated_count = 0

        # 📖 Abrimos el CSV y leemos cada fila
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['Title']
                new_description = row['Updated Description']

                try:
                    # ❗ Aquí debes completar el código para buscar la película por título
                    movie = __________.objects.get(__________)

                    # ❗ Aquí debes actualizar la descripción de la película
                    movie.__________ = __________
                    movie.save()
                    updated_count += 1

                    self.stdout.write(self.style.SUCCESS(f"Updated: {title}"))

                except Movie.DoesNotExist:
                    self.stderr.write(f"Movie not found: {title}")
                except Exception as e:
                    self.stderr.write(f"Failed to update {title}: {str(e)}")

        # ✅ Al finalizar, muestra cuántas películas se actualizaron
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movies from CSV."))

```
Debes completar los espacios en blanco y ubicar el archivo [updated_movie_descriptions.csv](updated_movie_descriptions.csv) en la raíz del proyecto django.

### ✅ Ejecuta el comando:
```bash
python manage.py update_movies_from_csv
```

Este comando:
- Lee el CSV
- Busca cada película por título en la base de datos
- Actualiza la descripción

✅ Al finalizar, tendrás las descripciones enriquecidas en tu base de datos.

✅ Para ejecutar el comando, debes asegurate de que la consola esté ubicada en la carpeta del proyecto Django ``DjangoProjectBase``.

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
✅ **Entregable:** Captura de pantalla donde se evidencie la actualización de la descripción de las películas en la base de datos.

