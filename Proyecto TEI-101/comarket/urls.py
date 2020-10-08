from django.urls import path
from . import views
from comarket import views
urlpatterns = [
    path('', views.index, name= "index"),
    path('servicio',views.servicio, name = "servicio"),
    path('nosotros',views.nosotros, name = "nosotros"),
    path('ods',views.ods, name = "ods"),
    path('formulario', views.formulario, name= "formulario"),
    path('enviado', views.enviado, name= "enviado")
]