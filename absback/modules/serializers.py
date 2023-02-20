from rest_framework import serializers
from .models import NombreABSPerModulesEts

class NombreABSPerStudentSerializers(serializers.ModelSerializer):
    '''
        get student abs with all modules
    '''
    class Meta:
        model = NombreABSPerModulesEts
        fields = '__all__'

