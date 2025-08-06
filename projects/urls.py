from django.urls import path
from .views import ProjectListCreate, ProjectDetail # <-- Importaciones cambiadas

urlpatterns = [
    path('projects/', ProjectListCreate.as_view(), name='project-list'), # <-- Ruta y nombre cambiados
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'), # <-- Ruta y nombre cambiados
]   