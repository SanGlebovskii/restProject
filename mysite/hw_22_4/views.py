from rest_framework.viewsets import ModelViewSet
from .models import Guitar
from .serializers import GuitarSerializer


class APIGuitarViewSet(ModelViewSet):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer