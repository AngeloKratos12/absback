from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate
from . import models
from rest_framework.decorators import api_view, permission_classes
import re
from pynytimes import NYTAPI
from rest_framework import permissions
from .models import EtsStudent, SamisStudent
from .serializers import StudentEts, StudentSamis
# Create your views here.

'''
name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    mat_number = models.CharField(max_length=12)
    classe = models.CharField(max_length=3)
'''

##GET ALL STUDENT IN ONE SCHOOLL ETS/SAMIS
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def allStudent(request, ecole):
    '''
        Fonction qui montre tous les étudiant  ETS/SAMIS
    '''
    if ecole == 'samis':
        allstudent = SamisStudent.objects.all()
        serialize = StudentSamis(allstudent, many=True)
    
    elif ecole == 'ets':
        allstudent = EtsStudent.objects.all()
        serialize = StudentEts(allstudent, many=True)

    else:
        return Response({'Message':'SCHOOL NOT FOUND'})

    return Response(serialize.data)
#----------------------------------------------------------------------------------

#GET ONE STTUDENT WITH SHCOOL SPECIFIED
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getStudent(request, ecole, id):
    '''
        Fonction qui montre  un étudiant du ETS/SAMIS
    '''
    if ecole == "samis":
        allstudent = SamisStudent.objects.get(id=id)
        serialize = StudentSamis(allstudent)

    elif ecole == 'ets':
        allstudent = EtsStudent.objects.get(id=id)
        serialize = StudentEts(allstudent)

    else:
        return Response({'Message':'SCHOOL NOT FOUND'})

    return Response(serialize.data)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def addETSStudent(request):
    '''
        Fonction qui ajoute un étudiant ETS
        name, user_name = request.POST['name'], request.POST['user_name']
        mat_number, classe  = request.POST['mat_number'], request.POST['classe']
        data = EtsStudent(name=name, user_name=user_name, mat_number=mat_number, classe=classe)
        data.save()
    '''
    serializer = StudentEts(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def addSamisStudent(request):
    '''
        Fonction qui ajoute un étudiant ETS
        name, user_name = request.POST['name'], request.POST['user_name']
        mat_number, classe  = request.POST['mat_number'], request.POST['classe']
        data = EtsStudent(name=name, user_name=user_name, mat_number=mat_number, classe=classe)
        data.save()
    '''
    serializer = StudentEts(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
