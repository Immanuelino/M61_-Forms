from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/register/')),  # Redirige la raíz a /register/
    path('', include('mi_app.urls')),  # Incluye las URLs de mi_app
]
