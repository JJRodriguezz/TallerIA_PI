# 🎬 Enriquecimiento de Descripciones de Películas con la API de OpenAI

## ✅ Objetivo
Aprenderás a utilizar la API de OpenAI en un proyecto Django para generar descripciones detalladas de películas almacenadas en la base de datos.

---

## 📌 🔥 ACTIVIDAD OBLIGATORIA - Actualizar la base de datos desde un CSV generado

Para **ahorrar costos de tokens** y garantizar que todos trabajen con los mismos datos, **ya hemos ejecutado la API** y generado un archivo `updated_movie_descriptions.csv`.

### ✅ ¿Qué debes hacer?
1. **Crear el comando** `update_movies_from_csv` en la aplicación `movie`:
```
movie/management/commands/update_movies_from_csv.py
```
2. **Ubicar el archivo `updated_movie_descriptions.csv` en la misma carpeta o ajustar la ruta**.

3. **Ejecutar el comando**:
```bash
python manage.py update_movies_from_csv
```

Este comando:
✅ Lee el CSV  
✅ Busca cada película por su título en la base de datos  
✅ Actualiza el campo `description`

👉 Código completo en: [update_movies_from_csv.py](update_movies_from_csv.py)

### ✅ Resultado esperado:
Tendrás en tu base de datos las descripciones enriquecidas listas para usar.

---

## 📂 ¿Qué contiene el CSV entregado?
El archivo `updated_movie_descriptions.csv` incluye:

| Title           | Updated Description                 |
|-----------------|-------------------------------------|
| Movie Title 1   | Descripción generada por OpenAI ... |
| Movie Title 2   | Descripción generada por OpenAI ... |

---

## 🚨 ACTIVIDAD OPCIONAL - Generar el CSV usando la API de OpenAI (NO obligatorio)
⚠️ Esta parte es solo **para aprendizaje** y **no debe ser ejecutada** por todos por temas de costos.

El comando `update_and_export_movies.py`:
- Recorre todas las películas
- Llama a la API de OpenAI
- Guarda el resultado en `updated_movie_descriptions.csv`

Ejecutar SOLO si el profesor lo autoriza:
```bash
python manage.py update_and_export_movies
```

👉 Código completo en: [update_and_export_movies.py](update_and_export_movies.py)

---

## 📌 Conexión a la API y construcción del prompt (solo si quieres revisar cómo funciona)
La API se conecta usando:
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('../openAI.env')
client = OpenAI(api_key=os.environ.get('openai_apikey'))
```

Y la instrucción que guía al modelo es:
```python
instruction = (
    "Vas a actuar como un aficionado del cine que sabe describir de forma clara, "
    "concisa y precisa cualquier película en menos de 200 palabras. La descripción "
    "debe incluir el género de la película y cualquier información adicional que sirva "
    "para crear un sistema de recomendación."
)
```

---

## 📌 Recomendaciones Finales
✅ Asegúrate de tener el archivo CSV disponible  
✅ Ejecuta el comando `update_movies_from_csv` para cargar las descripciones  
✅ **NO es necesario llamar la API directamente**

---

## ✅ Archivos que se entregan
✔️ `updated_movie_descriptions.csv` (ya generado)  
✔️ `update_movies_from_csv.py` (para ejecutar)  
✔️ `update_and_export_movies.py` (solo referencia - opcional)

---

## 📌 Ejemplo de ejecución esperada (obligatoria):
```bash
python manage.py update_movies_from_csv
```
Salida:
```
Found 50 movies in CSV
Processing: The Matrix
Updated: The Matrix
Processing: Interstellar
Updated: Interstellar
...
Finished updating 50 movies from CSV.
```

✅ Al finalizar tendrás la base de datos con las descripciones enriquecidas.

---
