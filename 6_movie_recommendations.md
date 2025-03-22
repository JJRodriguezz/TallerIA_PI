# 🎯 Recomendador de Películas usando Embeddings y OpenAI

## ✅ Objetivo
Crear un sistema de recomendación de películas utilizando **embeddings generados por OpenAI** y calcular la similitud entre las películas.

---

# 🎯 1. Introducción - ¿Qué es un Embedding y la Similitud de Coseno?

## ✅ ¿Qué es un Embedding?
Un **embedding** es una representación numérica de un texto o dato en un espacio vectorial. En nuestro caso:
- La **descripción de una película** se transforma en un vector de números
- Cada número representa una característica semántica de la descripción
- Películas con descripciones similares tendrán vectores (embeddings) cercanos

👉 Estos embeddings son generados por un modelo de OpenAI (`text-embedding-3-small`).

![embeddings](imgs/sr1.svg)

---

## ✅ ¿Qué es la Similitud de Coseno?
La **similitud de coseno** mide el ángulo entre dos vectores:
- Valor cercano a 1 → descripciones muy parecidas
- Valor cercano a 0 → descripciones diferentes

### ✅ Fórmula:
```
sim(a, b) = (a · b) / (||a|| * ||b||)
```
Donde:
- `a · b` → producto punto
- `||a||` → norma o magnitud del vector

---

## 📌 2. ¿Qué haremos a continuación?

Para comprender cómo funciona la generación de **embeddings** y el cálculo de **similitud**, crearemos un **comando de Django** que:

✅ Seleccionará **dos películas** desde la base de datos  
✅ Generará el **embedding de la descripción** de cada una usando la API de OpenAI  
✅ Calculará la **similitud de coseno** entre ambas películas

De esta forma, podrás observar cómo el sistema mide qué tan parecidas son dos películas a partir de sus descripciones.

---

## 📌 3. Explicación del Código
### ✅ Conectarse a la API de OpenAI y cargar las películas
```python
load_dotenv('openAI.env')
client = OpenAI(api_key=os.environ.get('openai_api_key'))

movie1 = Movie.objects.get(title="Saving Private Ryan")
movie2 = Movie.objects.get(title="Schindler's List")
```
- Carga la API Key
- Selecciona las películas desde la base de datos por su título

---

## 📌 2. Función para generar el embedding
```python
def get_embedding(text):
    response = client.embeddings.create(input=[text], model="text-embedding-3-small")
    return np.array(response.data[0].embedding, dtype=np.float32)
```
- Envía la descripción a OpenAI
- Recibe el embedding como un vector numérico

---

## 📌 3. Función para calcular la similitud de coseno
```python
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```
- Calcula qué tan parecidas son dos películas comparando sus embeddings

---

## 📌 4. Calcular los embeddings y compararlos
```python
emb1 = get_embedding(movie1.description)
emb2 = get_embedding(movie2.description)

similarity = cosine_similarity(emb1, emb2)
```
✅ Genera los embeddings  
✅ Calcula la similitud entre las dos descripciones

---

## 📌 5. Interpretar el resultado
```python
self.stdout.write(f"🎬 {movie1.title} vs {movie2.title}: {similarity:.4f}")
```
- Muestra en consola el nivel de similitud
- Un valor **mayor a 0.7** suele indicar que las películas son similares temáticamente

---

## ✅ Resultado esperado
Ejemplo de salida:
```
🎬 Saving Private Ryan vs Schindler's List: 0.8521
```

✅ Esto sugiere que ambas películas comparten una temática cercana (en este caso, la Segunda Guerra Mundial).
