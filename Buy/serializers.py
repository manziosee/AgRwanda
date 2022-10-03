from rest_framework import serializers
from .models import BuyModel

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model=BuyModel
        fields='__all__'
        