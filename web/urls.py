
from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/web/', views.servicios_web, name="servicios_web"),
    path('servicios/iching/', views.servicios_iching, name="servicios_iching"), 

    
]
