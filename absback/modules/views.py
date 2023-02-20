from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from . import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import NombreABSPerModulesEts
from .serializers import NombreABSPerStudentSerializers
from django.db import connection
# Create your views here.

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAbsAllrStudent(request, school):
    '''
        FOnction
    '''
    if school == 'ets':
        data = NombreABSPerModulesEts.objects.all()

        dataserializer = NombreABSPerStudentSerializers(data, many=True)
        #print(dataserializer.data, 'YES')
        return Response(dataserializer.data)
    
    else:
        return Response({'Message':'School Indisponible'})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAbsOneStudent(request, idstudent, school):
    '''
        Get number of absence of one student
    '''
    
    if school == 'samis':
        pass

    elif school == 'ets':
        try:
            nbr_abs = NombreABSPerModulesEts.objects.get(id=idstudent)
            data = NombreABSPerStudentSerializers(nbr_abs, many=True)

        except:
            return Response({'Message':'ERROR STUDENT'})
    
    else:
        return Response({'Message':'ERROR SCHOOL'})
    
    return Response(data.data)
    

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateabs(request, idstudent, school, module):
    colonne = module
    filter = f"idStudent={idstudent}"

    if school == 'samis':
        table_name = "nombreabspermodulesamis"

    elif school == 'ets':
        table_name  = "nombreabspermoduleets"
    
    else:
        Response({'Message':'ERROR SCHOOL'})

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT  {colonne} FROM {table_name} WHERE {filter}")  
        result = cursor.fetchone()
        valuenow = result[0]

        cursor.execute(f"UPDATE {table_name } SET {colonne} = %s WHERE {filter}", [valuenow + 1])
        rows_updated = cursor.rowcount
        
    return Response({'Message':'Up^date edded'})

    


