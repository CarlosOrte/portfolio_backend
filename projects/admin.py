from django.contrib import admin
from .models import Project # <-- Importado Project

@admin.register(Project) # <-- Registrado Project
class ProjectAdmin(admin.ModelAdmin): # <-- Clase cambiada
    list_display = ('title', 'category', 'deployment_link', 'github_link')
    search_fields = ('title', 'category', 'technologies_used')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'short_description', 'main_image')
        }),
        ('Detalles del Proyecto', { # <-- Etiqueta cambiada
            'fields': ('problem_statement', 'solution_details', 'process_steps',
                       'technologies_used', 'challenges_faced', 'results_impact')
        }),
        ('Enlaces', {
            'fields': ('deployment_link', 'github_link')
        }),
    )