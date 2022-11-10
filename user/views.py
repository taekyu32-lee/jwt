from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("가입완료",status=status.HTTP_200_OK)
        else:
            return Response(f"message : {serializer.errors}",status=status.HTTP_400_BAD_REQUEST)

