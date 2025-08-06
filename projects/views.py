# myportfolio_project/projects/views.py (antes casestudies/views.py)
from rest_framework import generics
from .models import Project # <-- Importado Project
from .serializers import ProjectSerializer # <-- Importado ProjectSerializer

class ProjectListCreate(generics.ListCreateAPIView): # <-- Clase cambiada
    queryset = Project.objects.all() # <-- Modelo cambiado
    serializer_class = ProjectSerializer # <-- Serializador cambiado

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView): # <-- Clase cambiada
    queryset = Project.objects.all() # <-- Modelo cambiado
    serializer_class = ProjectSerializer # <-- Serializador cambiado
    lookup_field = 'pk'