from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note # El modelo creado
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']