from django.urls import path
from .import views

urlpatterns = [
   path('addphoto/', views.Photo_Add, name="addphoto"),
   path('viewphoto/', views.View_Photos, name="viewphoto"),
   path('login/', views.Login, name="login"),
   path('register/', views.Registration, name="register"),
   path('viewmyphotos/', views.ViewMyPhoto, name="viewmyphotos"),

]