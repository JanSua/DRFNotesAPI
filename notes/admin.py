from django.contrib import admin
from .models import Note, Tag

admin.site.register(Note) # Para ver el modelo en django admin.
admin.site.register(Tag)
