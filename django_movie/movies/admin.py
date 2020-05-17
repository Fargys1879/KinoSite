from django.contrib import admin
from .models import Category,Movie,MovieShot,RatingStar,Rating,Reviews,Actor,Genre
# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Actor)
admin.site.register(Genre)
