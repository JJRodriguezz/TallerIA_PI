# 🎨 Generación de Imágenes con la API de OpenAI para Películas

## ✅ Objetivo
En esta etapa aprenderás a usar la API de OpenAI para generar ilustraciones de las películas y actualizar las imágenes almacenadas en la base de datos.

---

## 📌 1. Conexión con la API de OpenAI y generación de imágenes (OPCIONAL - SOLO CONSULTA)
Te explicamos cómo funciona la conexión y la llamada a la API de generación de imágenes, pero **no es obligatorio ejecutarlo** por costos y tiempo.

### 🔑 Configuración inicial
- Asegúrate de tener en tu `.env` la API Key:
```
openAI_api_key=sk-xxxxxxxxxxxxxxxxxxxx
```

### ✅ Código base de conexión:
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('../openAI.env')
client = OpenAI(api_key=os.environ.get('openAI_api_key'))
```

---

## 📌 2. Código para generar imágenes desde los títulos de las películas (OPCIONAL - NO EJECUTAR)
El siguiente código permite recorrer las películas y generar una imagen usando la API `dall-e-2`.

```python
from movie.models import Movie
import requests
from PIL import Image
from io import BytesIO

def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

movies = Movie.objects.all()

for movie in movies:
    prompt = f"Portada de la película {movie.title}"
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    img = fetch_image(image_url)
    img.save(f"media/movie/images/{movie.title}.png")
```

⚠️ *Este proceso es costoso y se deja solo como referencia*.

---

## 🚨 3. ¿Qué se hizo por ustedes?
✅ Se ejecutó el proceso de generación de imágenes.  
✅ Se empaquetaron las imágenes en un archivo `.zip` que deben descargar desde el siguiente enlace:

👉 [Descargar imágenes](https://eafit-my.sharepoint.com/:f:/g/personal/jdmartinev_eafit_edu_co/El6GJ5EpcR5PiKJJkoSotHsBrqrlsGEcfB2pUerg9QOPpA?e=NVXca3)

---

## 📌 4. Actividad obligatoria: Actualizar la base de datos con las nuevas imágenes
### ✅ ¿Qué debes hacer?
1. **Descargar y descomprimir las imágenes** en la carpeta:
```
media/movie/images/
```

2. **Crear el comando `modify_image_paths_db` en la app movie**:
```
movie/management/commands/modify_image_paths_db.py
```

3. **Ejecutar el comando**:
```bash
python manage.py modify_image_paths_db
```

✅ Este comando actualiza la ruta de la imagen de cada película en la base de datos.

---

## 📂 5. Resultado esperado
Al correr el servidor de Django, las imágenes mostradas en la vista de cada película serán las generadas por la API de OpenAI.

---

## ✅ 6. Alternativa (OPCIONAL)
También puedes explorar el archivo `movie_pictures_hf.py` para generar imágenes con Stable Diffusion en Hugging Face.

---

## 📌 7. Resumen Final
| Paso | Acción | ¿Obligatorio? |
|-----|--------|--------------|
| 1   | Conectar y usar la API (revisar) | ❌ Opcional |
| 2   | Generar imágenes desde la API    | ❌ Opcional |
| 3   | Descargar imágenes y actualizar rutas | ✅ Sí, obligatorio |
| 4   | Explorar Hugging Face (opcional) | ❌ Opcional |

---

