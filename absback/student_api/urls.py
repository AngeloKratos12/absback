from . import views
from django.urls import path

urlpatterns = [
    path("", views.addETSStudent),
    path("allstudent/<str:ecole>", views.allStudent),
    path("etsstudent/<int:id>/", views.addETSStudent),
    
]