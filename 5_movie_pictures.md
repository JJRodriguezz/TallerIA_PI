# 🎨 Generación de imágenes por película usando OpenAI y actualización en la base de datos

## ✅ Objetivo
Generar imágenes personalizadas por cada película usando la API de OpenAI y actualizar la base de datos con la imagen correspondiente.

---

## 📌 1. ¿Qué vas a hacer en esta parte?
✅ Conectarte a la API de OpenAI  
✅ Generar una imagen para una película usando una función auxiliar  
✅ Descargar y almacenar la imagen en el proyecto  
✅ Actualizar la base de datos con la nueva imagen generada

⚠️ Por ahora, el comando está configurado para generar y actualizar **solo la primera película**.

✅ Esto es intencional para **ahorrar recursos y evitar costos de API**.

✅ **Las imágenes de todas las películas ya fueron generadas** y se entregan en una carpeta lista para usar.

🚫 **No debes quitar el `break`.**

    El código lo puedes encontrar en el archivo [updates_images.py](update_images.py)
---

## 📌 2. Descripción del comando `generate_images`
El comando se debe ubicar en:
```
movie/management/commands/generate_images.py
```

### ✅ ¿Qué hace cada parte?

```python
# Carga las variables de entorno con la API Key
load_dotenv('api_keys.env')
client = OpenAI(api_key=os.environ.get('openAI_api_key'))
```
- Se conecta a la API de OpenAI cargando la clave desde el archivo `.env`

---

```python
images_folder = 'media/movie/images/'
os.makedirs(images_folder, exist_ok=True)
```
- Crea la carpeta de imágenes si no existe.

---

```python
movies = Movie.objects.all()
self.stdout.write(f"Found {movies.count()} movies")
```
- Consulta la base de datos y trae todas las películas.

---

### ✅ Función auxiliar que hace todo el trabajo con la API:
```python
def generate_and_download_image(self, client, movie_title, save_folder):
    prompt = f"Movie poster of {movie_title}"
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    image_filename = f"m_{movie_title}.png"
    image_path_full = os.path.join(save_folder, image_filename)

    image_response = requests.get(image_url)
    image_response.raise_for_status()
    with open(image_path_full, 'wb') as f:
        f.write(image_response.content)

    return os.path.join('movie/images', image_filename)
```
✅ Genera la imagen en OpenAI, descarga la imagen y la almacena en la carpeta del proyecto.

---

### ✅ Dentro del ciclo:
```python
for movie in movies:
    image_relative_path = self.generate_and_download_image(client, movie.title, images_folder)
    movie.image = image_relative_path
    movie.save()
    self.stdout.write(self.style.SUCCESS(f"Saved and updated image for: {movie.title}"))
    break
```
- Llama la función auxiliar
- Actualiza la imagen en la base de datos
- Detiene la ejecución en la primera película (luego debes quitar el `break`)

---

## 📌 3. Ejecuta el comando
```bash
python manage.py generate_images
```

✅ Verás mensajes indicando qué película se procesó y si la imagen fue descargada y almacenada.

---

## 📸 4. Verificación y captura de pantalla

✅ Levanta el servidor de Django:
```bash
python manage.py runserver
```

✅ Accede a la vista de las películas y verifica que la imagen de la primera película corresponde a la generada.

✅ **Toma una captura de pantalla** y guárdala como:
```
screenshot_generated_image.png
```

✅ Esta es la evidencia de tu proceso funcionando.

---

## 📌 5. Nota:
Una vez validado el funcionamiento, elimina la línea `break` para procesar todas las películas y generar sus imágenes.
