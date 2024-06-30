from django.urls import path
from . import views

urlpatterns = [
    
    path("home", views.CargarIndex, name="home"),
    path("perros", views.Cargarperros, name="perros"),
    path("gatos", views.Cargargatos, name="gatos"),
    path("productos", views.Cargarproductos, name="productos"),
    path("login", views.Cargarlogin, name="login"),
    path("art_aseo", views.CargarArt_aseo, name="art_aseo")

]
