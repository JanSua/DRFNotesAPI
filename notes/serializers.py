from rest_framework import serializers
from .models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    # Añadir el serializer de la tag
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source='tags',
    ) #Para añadir etiquetas por id
    class Meta:
        model = Note # El modelo creado
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'tags', 'tag_ids']