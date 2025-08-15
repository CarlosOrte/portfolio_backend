# myportfolio_project/projects/models.py (antes casestudies/models.py)
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Project(models.Model): # <-- Clase cambiada a Project
    title = models.CharField(max_length=255, verbose_name="Título del Proyecto") # <-- Etiqueta cambiada
    category = models.CharField(max_length=100, verbose_name="Categoría (ej: Web, Diseño, Mobile)")
    short_description = models.TextField(blank=True, null=True, verbose_name="Descripción Corta")

    problem_statement = models.TextField(verbose_name="Planteamiento del Problema")
    solution_details = models.TextField(verbose_name="Detalles de la Solución")
    process_steps = models.TextField(blank=True, null=True, verbose_name="Pasos del Proceso (ej: Markdown/HTML)")
    technologies_used = models.CharField(max_length=500, verbose_name="Tecnologías Utilizadas (ej: React, Django, SQL)")
    challenges_faced = models.TextField(blank=True, null=True, verbose_name="Desafíos Enfrentados")
    results_impact = models.TextField(verbose_name="Resultados e Impacto")

    main_image_url = CloudinaryField('image')

    deployment_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Enlace de Despliegue/Demo")
    github_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Enlace a GitHub")

    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = "Proyecto" # <-- Cambiado
        verbose_name_plural = "Proyectos" # <-- Cambiado
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title