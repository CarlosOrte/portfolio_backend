from rest_framework import serializers
from .models import Project # <-- Importado Project

class ProjectSerializer(serializers.ModelSerializer): # <-- Clase cambiada a ProjectSerializer
    main_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project # <-- Modelo cambiado a Project
        fields = '__all__'

    def get_main_image_url(self, obj):
        if obj.main_image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.main_image.url)
            return obj.main_image.url
        return None