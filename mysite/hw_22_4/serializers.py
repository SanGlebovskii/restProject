from rest_framework import serializers
from .models import *


class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitar
        fields = ('brand', 'year', 'price', 'amount', 'comment')
