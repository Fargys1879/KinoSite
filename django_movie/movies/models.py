from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):
    """Актеры и Режисеры"""
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0 )
    description = models.TextField("Описание")
    image = models.ImageField("Изображение" , upload_to ="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер и Режисер"
        verbose_name_plural = "Актеры и Режисеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    """Фильмы"""
    name = models.CharField("Название Фильма", max_length=150)
    tagline = models.CharField("Слоган", max_length=150, default= "")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер" , upload_to ="films/")
    year = models.PositiveIntegerField("Дата Выхода", default= 2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режисер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанр",)
    world_premiere = models.DateField("Дата Премьеры", default= date.today)
    budged = models.CharField("Бюджет", max_length=150)
    fess_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Сумма в $")
    fess_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Сумма в $")
    category = models.ForeignKey(
        Category , verbose_name= "Категория", on_delete = models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Черновик", default= False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={ "slug" : self.url},)

class MovieShot(models.Model):
    """Кадры из Фильмов"""
    
    title = models.CharField("Заголовок", max_length= 100)
    description = models.TextField("Описание")
    image = models.ImageField("Кадр из Фильма" , upload_to ="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name= "Фильм", on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из Фильма"
        verbose_name_plural = "Кадры из Фильмов"

class RatingStar(models.Model):
    """Звезды Рейтинга Фильмов"""
    value = models.SmallIntegerField("Значение", default = 0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звезда Рейтинга Фильма"
        verbose_name_plural = "Звезды Рейтинга Фильмов"

class Rating(models.Model):
    """Рейтинг Фильмов"""
    ip = models.CharField("IP-адресс", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete= models.CASCADE, 
    verbose_name="Звезды")
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE,
    verbose_name= "Фильм")

    def __str__(self):
        return f"{self.star}-{self.movie}"

    class Meta:
        verbose_name = "Рейтинг Фильма"

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField("E-mail")
    name = models.CharField("Имя", max_length=50)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete= models.SET_NULL, blank= True, null=True
        )
    movie = models.ForeignKey(Movie, verbose_name= "Фильм", on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        

















