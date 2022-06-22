from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.homepage, name='landing'),
    path('nyumbani/', views.homes, name='nyumbani'),
    path('new_nyumbani/', views.create_home, name='new-home'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('nyumbani/<int:nyumbani_id>/like',views.like_image,name='likeimage'),
]