from django.urls import path
from .views import home, formulario, reseña, inicio

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('reseña/', reseña, name="reseña"),
    path('inicio/', inicio, name="inicio")
]