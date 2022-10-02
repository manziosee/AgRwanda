from rest_framework import generics
from .serializers import BuySerializer
from .models import BuyModel

# Create your views here.

class BuyProduct(generics.CreateAPIView):
    queryset=BuyModel.objects.all()
    