from django.db import models

class Tag(models.Model):
    # Dar nombre unico a cada etiqueta.
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f' id:({self.id}) {self.name}'

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # añadir el campo de la tag
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)
    
    def __str__(self):
        return self.title # Para cuando se llamen las notas, aparezca el título
