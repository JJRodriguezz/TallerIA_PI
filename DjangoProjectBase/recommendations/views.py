from django.shortcuts import render
from dotenv import load_dotenv
from movie.models import Movie
from openai import OpenAI
import numpy as np
import os
# Create your views here.
# Para la búsqueda por similitud de coseno
def cosine_search(request):
    best_movie = None
    max_similarity = -1
    user_prompt = ""

    if request.method == "POST":
        user_prompt = request.POST.get("searchQuery", "")
        if user_prompt:
            response = client.embeddings.create(
                input=[user_prompt],
                model="text-embedding-3-small"
            )
            prompt_emb = np.array(response.data[0].embedding, dtype=np.float32)

            for movie in Movie.objects.all():
                movie_emb = np.frombuffer(movie.emb, dtype=np.float32)
                similarity = cosine_similarity(prompt_emb, movie_emb)

                if similarity > max_similarity:
                    max_similarity = similarity
                    best_movie = movie

    return render(request, "cosine_search.html", {
        "best_movie": best_movie,
        "similarity": max_similarity,
        "user_prompt": user_prompt
    })

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Cargar la API Key
load_dotenv('api_keys.env')
client = OpenAI(api_key=os.environ.get('openai_apikey'))