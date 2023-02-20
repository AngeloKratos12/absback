from . import views
from django.urls import path

urlpatterns = [
    path("<str:school>/all", views.getAbsAllrStudent),
    path("<str:school>/<int:idstudent>", views.getAbsAllrStudent),
    path("updateabs/<str:school>/<str:module>/<int:idstudent>", views.updateabs),
    
    
]