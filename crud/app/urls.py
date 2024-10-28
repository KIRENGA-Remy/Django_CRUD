from django.urls import path
from app import views

urlpatterns = [
    path('', views.login, name='login'),
    # path(r'^$', views.login, name='login'),
    path(r'register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('add/', views.add_user, name='add_user'),
    path('show/', views.getusers, name='getusers'),
]
