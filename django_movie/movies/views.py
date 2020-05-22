from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie, Category
from .forms import ReviewsForm

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

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit = False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

    
