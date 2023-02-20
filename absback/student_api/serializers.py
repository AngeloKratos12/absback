from rest_framework import serializers
from .models import EtsStudent, SamisStudent

class StudentEts(serializers.ModelSerializer):

    class Meta:
        model = EtsStudent
        fields = '__all__'
        

class StudentSamis(serializers.ModelSerializer):

    class Meta:
        model = SamisStudent
        fields = '__all__'
    
    def create(self, validated_data):
        student = EtsStudent()
        student.name = validated_data['name']
        student.user_name = validated_data['user_name']
        student.mat_number = validated_data['mat_number']
        student.classe = validated_data['classe']

        return super().create(validated_data)