from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.homepage, name='landing'),
    path('nyumbani/', views.homes, name='nyumbani'),
]