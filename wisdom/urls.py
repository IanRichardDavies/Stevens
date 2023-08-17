from django.urls import path
from . import views

urlpatterns = [
    path('', views.wisdom, name='wisdom'),
]
