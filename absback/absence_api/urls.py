from . import views
from django.urls import path

urlpatterns = [
    path("", views.abs),
    path("allabs/", views.getABS),
]