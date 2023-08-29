from django.urls import path
from api import views

urlpatterns = [
    path('hostname/', views.hostname),
    path('author/', views.author),
    path('id/', views.uid),
]

