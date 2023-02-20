from rest_framework import serializers
from .models import EtsABS

class EtsABSSerializers(serializers.ModelSerializer):
    class Meta:
        model = EtsABS
        fields = ['id', 'motif', 'status']