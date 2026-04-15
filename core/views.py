from django.shortcuts import render
from rest_framework import generics
from .models import Residence, Student, Reservation
from .serializers import ResidenceSerializer, StudentSerializer, ReservationSerializer


class ResidenceListView(generics.ListAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer