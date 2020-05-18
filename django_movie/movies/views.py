from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie

# Create your views here.
"""class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request,"movies/movies.html", {'movie_list' : movies})"""

class MovieView(ListView):
    """Список Фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)  

class MovieDetailView(DetailView):
    """Полное описание Фильма"""
    model = Movie
    slug_field = "url"
    
