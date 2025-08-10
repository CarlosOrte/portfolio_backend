from rest_framework import serializers
from .models import Project # <-- Importado Project
from django.conf import settings # Importa las configuraciones

class ProjectSerializer(serializers.ModelSerializer): # <-- Clase cambiada a ProjectSerializer
    main_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project # <-- Modelo cambiado a Project
        fields = '__all__'

    def get_main_image_url(self, obj):
        if obj.main_image:
            # Retorna la URL completa de la imagen en S3
            return f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/media/{obj.main_image.name}'
        return None