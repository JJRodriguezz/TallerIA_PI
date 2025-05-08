from django.urls import path 
from . import views 

urlpatterns = [ 
    path('<int:movie_id>/', views.recommend_movies, name='recommend_movies'),
]