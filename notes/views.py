from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

# Vistas basadas en clases (Class-Based Views) con APIView

class NoteList(APIView):
    # Enlistar todas las Notas
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    # Añadir notas
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NoteDetail(APIView):
    # Obtener el detalle de una Nota por pk
    def get(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    # Actualizar una nota por pk
    def put(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Eliminar una nota por pk
    def delete(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
