from rest_framework import status, generics

from .serializers import ComputerSerializer
from .models import Computer


class APIComputers(generics.ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class APIComputerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
