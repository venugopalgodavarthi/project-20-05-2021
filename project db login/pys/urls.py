from django.urls import path
from pys import views

urlpatterns= [
    path("index/",views.index, name="index" ),
    path("home/",views.home, name="home" ),
    
]