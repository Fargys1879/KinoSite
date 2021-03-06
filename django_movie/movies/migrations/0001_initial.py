# Generated by Django 3.0.6 on 2020-05-17 02:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Актер и Режисер',
                'verbose_name_plural': 'Актеры и Режисеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название Фильма')),
                ('tagline', models.CharField(default='', max_length=150, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='films/', verbose_name='Постер')),
                ('year', models.PositiveIntegerField(default=2019, verbose_name='Дата Выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Дата Премьеры')),
                ('budged', models.CharField(max_length=150, verbose_name='Бюджет')),
                ('fess_in_usa', models.PositiveIntegerField(default=0, help_text='Сумма в $', verbose_name='Сборы в США')),
                ('fess_in_world', models.PositiveIntegerField(default=0, help_text='Сумма в $', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='Режисер')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда Рейтинга Фильма',
                'verbose_name_plural': 'Звезды Рейтинга Фильмов',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP-адресс')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.Movie', verbose_name='Фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.RatingStar', verbose_name='Звезды')),
            ],
            options={
                'verbose_name': 'Рейтинг Фильма',
            },
        ),
        migrations.CreateModel(
            name='MovieShot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Кадр из Фильма')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из Фильма',
                'verbose_name_plural': 'Кадры из Фильмов',
            },
        ),
    ]
