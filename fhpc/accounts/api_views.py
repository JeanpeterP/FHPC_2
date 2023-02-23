from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
import json
from .models import Account, Pet
from .common.encoders import PetSerializer, AccountSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class AccountListApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                account = Account.objects.get(pk=pk)
                serializer = AccountSerializer(account)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return Response({'error': 'Account not found.'}, status=status.HTTP_404_NOT_FOUND)

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            # Validate password
            password = serializer.validated_data['password']
            try:
                validate_password(password)
            except ValidationError as e:
                return Response(
                    {'error': ', '.join(e.messages)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create the account object using create_user()
            account = Account.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=password,
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name']
            )

            return Response(
                AccountSerializer(account).data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )


class PetApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                account = Pet.objects.get(pk=pk)
                serializer = PetSerializer(account)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except Pet.DoesNotExist:
                return Response({
                    'error': 'Account not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    def post (self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            pet = Pet.objects.create_user(
                name=serializer.validated_data['name'],
                breed=serializer.validated_data['breed'],
                age=serializer.validated_data['age'],
                weight=serializer.validated_data['weight'],
                #owner=owner
            )
            pass