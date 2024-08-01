from django.urls import path
from .views import lista_partos, novo_parto

urlpatterns = [
    path('', lista_partos, name='lista_partos'),
    path('novo/', novo_parto, name='novo_parto'),
]