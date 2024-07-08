from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status




class UserRegistration(APIView):
    
    def post(self,request):
        data = request.data
        serializer = UserRegistrationSerializer(data = data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user = serializer.save()
            return Response({'message':'Registration sucess', "data" :serializer.data,},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        try:
            if id:
                user = Accounts.objects.get(id = id)
                serialized_data = UserListSerializer(user,many= False)
                return Response(serialized_data.data,status=status.HTTP_200_OK)
            else:
                users = Accounts.objects.all()
                print(users)
                if not users:
                    return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)
                serialized_data = UserListSerializer(users,many= True)
                return Response(serialized_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        if id:
            user = Accounts.objects.get(id = id)
            user.delete()
            return Response({"message":f"user deleted {user.email}"},status=status.HTTP_200_OK)  
        else:
            return Response({"message":f"user with {id} not found"},status=status.HTTP_404_NOT_FOUND)
        
    def patch(self,request,id= None):
        if id:
            user = Accounts.objects.get(id = id)
            serializer = UserListSerializer(user, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

        
    
    
    
