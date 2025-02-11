from django.contrib import admin
from .models import Film, Review, Actor

# Register your models here.

admin.site.register(Film)
admin.site.register(Review)
admin.site.register(Actor)