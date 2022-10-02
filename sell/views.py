from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class createProduct(generics.CreateAPIView):
    #permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = sellModel.objects.all()
    serializer_class = sellSerializer
    
class viewProduct(generics.ListAPIView):
    #permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = sellModel.objects.all()
    serializer_class= sellSerializer
    
class editProduct(generics.UpdateAPIView):
    #permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = sellModel.objects.all()
    serializer_class = sellSerializer
    
class deleteProduct(generics.DestroyAPIView):
    #permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = sellModel.objects.all()
    serializer_class = sellSerializer