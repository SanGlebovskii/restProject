from .serializers import PetSerializer
from .models import Pet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class APIPets(APIView):
    def get(self, request):
        pets = Pet.objects.filter()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPetDetail(APIView):
    def get(self, request, pk):
        pet = Pet.objects.get(pk=pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk):
        pet = Pet.objects.get(pk=pk)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pet = Pet.objects.get(pk=pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
