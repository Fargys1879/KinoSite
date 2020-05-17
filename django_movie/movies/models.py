from django.db import models

# Create your models here.
class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    descruption = models.TextField("Описание")
    slug = models.SlugField(max_length=150, unique = true)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):
    """Актеры и Режисеры"""
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0 )
    descruption = models.TextField("Описание")
    image = models.ImageField("Изображение" , upload_to ="actors/")

     def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер и Режисер"
        verbose_name_plural = "Актеры и Режисеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=150)
    descruption = models.TextField("Описание")
    slug = models.SlugField(max_length=150, unique = true)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    """Фильмы"""
    name = models.CharField("Название Фильма", max_length=150)
    tagline = models.CharField("Слоган", max_length=150)
    descruption = models.TextField("Описание")
    poster = models.ImageField("Постер" , upload_to ="films/")
    year = models.PositiveIntegerField("Дата Выхода", default= 2019)
    country = models.CharField("Страна", max_length=150)
    directors = models.ManyToManyField(Actor, verboose_name="Режисер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verboose_name="Актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verboose_name="Жанр",)
    world_premiere = models.DateField("Дата Премьеры", default= date.today)
    budged = models.CharField("Бюджет", max_length=150)
    fess_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Сумма в $")
    fess_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Сумма в $")
    category = models.ForeignKey(
        Category , verbose_name= "Категория", on_delete = models.SET_NULL, Null= True
    )
    url = models.SlugField(max_length=150, unique = true)
    draft = models.BooleanField("Черновик", default= False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"











