from django.http import JsonResponse

import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(APIView):
    def get(self, request, *args, **kwargs):
        if 'user_id' in kwargs:
            try:
                person = Person.objects.get(id=kwargs['user_id'])
                serializer = PersonSerializer(person)

                return JsonResponse(serializer.data)
            except Person.DoesNotExist:
                return JsonResponse(json.dumps({'detail': 'This Person Cannot be Found'}), status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            people = Person.objects.all()
            serializer = PersonSerializer(people, many=True)
            
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            person = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return JsonResponse(json.dumps({'detail': 'This Person Cannot be Found'}), status=status.HTTP_404_NOT_FOUND, safe=False)
        
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id):
        try:
            person = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return JsonResponse(json.dumps({'detail': 'This Person Cannot be Found'}), status=status.HTTP_404_NOT_FOUND, safe=False)
        
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if 'user_id' in kwargs:
            try:
                person = Person.objects.get(id=kwargs['user_id'])
                person.delete()
                
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return JsonResponse(json.dumps({'detail': 'This Person Cannot be Found'}), status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(json.dumps({'detail': 'This Person Cannot be Found'}), status=status.HTTP_404_NOT_FOUND, safe=False)
            