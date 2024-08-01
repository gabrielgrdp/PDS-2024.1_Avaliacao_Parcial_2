from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('partos/', include('partos.urls')),
    path('', RedirectView.as_view(url='partos/', permanent=True)),  # Redireciona a rota raiz para /partos/
]