from django.urls import path
from .views import register, home, login_view  # Importa la vista de login

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # Añade esta línea
]
