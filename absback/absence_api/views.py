from django.http import JsonResponse
from django.contrib.auth import authenticate
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import re
from pynytimes import NYTAPI
from rest_framework import permissions
from student_api.models import *
from .serializers import EtsABSSerializers
from .models import EtsABS

# Create your views here.

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def abs(request):
    '''
        Fonction initiale
    '''
    return Response({'Me':'Hello World'})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getABS(request):
    '''
        Fonction qui retourne l'absence d'un élève
    '''
    """
        if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = EtsStudent.objects.get(id=logged_user_id)
    """
    if request.method == 'GET':
        student = EtsABS.objects.all()
        data = EtsABSSerializers(student, many=True)

    return Response(data.data)
        

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAbsStudent(request, idstudent, school):
    '''
        Get number of absence of one student
    '''
    
    if school == 'SAMIS':
        pass
    elif school == 'ETS':
        pass
    else:
        return Response({'Message':'ERROR SCHOOL'})

