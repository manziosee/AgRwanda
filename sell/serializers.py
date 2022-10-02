from .models import sellModel
from rest_framework import serializers

class sellSerializer(serializers.ModelSerializer):
    class Meta():
        model = sellModel
        fields = '__all__'