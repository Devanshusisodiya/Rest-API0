from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def testView(request):
    return Response("API Base Point")

@api_view(['GET'])
def testList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    if serializer:
       return Response(serializer.data)
    else:
        print("\n Bug Encountred \n")
        return Response("Bug Encountered", safe=False)

@api_view(['GET'])
def testListSingular(request, name):
    user = User.objects.get(name=name)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def testCreateSingular(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Invalid Data")

#checking to see if updates work