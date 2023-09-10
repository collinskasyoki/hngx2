from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(APIView):
    def get(self, request, *args, **kwargs):
        if 'name' in kwargs:
            try:
                person = Person.objects.get(name=kwargs['name'])
                serializer = PersonSerializer(person)

                return Response(serializer.data)
            except Person.DoesNotExist:
                return Response({'detail': 'This Person Cannot be Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            people = Person.objects.all()
            serializer = PersonSerializer(people, many=True)
            
            return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name):
        try:
            person = Person.objects.get(name=name)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        if 'name' in kwargs:
            try:
                person = Person.objects.get(name=kwargs['name'])
                person.delete()
                
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return Response({'detail': 'This Person Cannot be Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'This Person Cannot be Found'}, status=status.HTTP_404_NOT_FOUND)
            