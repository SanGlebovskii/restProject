from rest_framework import status

from .serializers import CarSerializer
from .models import Car
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def api_cars(request):
    if request.method == "GET":
        cars = Car.objects.filter()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        serializer = CarSerializer(car)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CarSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)