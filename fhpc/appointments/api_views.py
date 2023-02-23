from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
import json
from accounts.models import Pet
from .models import Appointments
from .common.encoders import AppointmentSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class AppointmentApiView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = Appointments.objects.create(
                customer=serializer.validated_data['customer'],
                start_time=serializer.validated_data['start_time'],
                end_time=serializer.validated_data['end_time'],
                location=serializer.validated_data['location'],
                notes=serializer.validated_data['notes']
            )
            print(serializer.validated_data['pet'])
            for pet_data in serializer.validated_data['pet']:
                pet = Pet.objects.get(pk=pet_data['id'])
                appointment.pet.add(pet)
            appointment.save
            return Response(
                serializer.data,
                status=status.HTTP_201_created
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                appointment=Appointments.objects.get(pk=pk)
                serializer=AppointmentSerializer(appointment)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except Appointments.DoesNotExist:
                return Response({
                    'error': 'appointment not found'},
                    status=status.HTTP_404_NOT_FOUND
                    )
        
        appointments = Appointments.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )