from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Genre, MovieShot


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'tagline', 'description', 'country')


@register(MovieShot)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')