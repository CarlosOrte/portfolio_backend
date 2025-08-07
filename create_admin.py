import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')
django.setup()

# Ahora sí, puedes usar los modelos de Django
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'carlosortegaux@gmail.com', 'OEcc61959_$')
    print("Superuser 'admin' creado exitosamente.")
else:
    print("El superuser 'admin' ya existe.")