from django.urls import path
from . import views

urlpatterns = [
    path('', views.word, name='word'),
    path('create/', views.create, name='create'),
    path('reset/', views.reset, name='reset'),
]
