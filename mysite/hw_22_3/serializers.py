from rest_framework import serializers
from .models import *


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('brand', 'year', 'price', 'amount', 'comment')
