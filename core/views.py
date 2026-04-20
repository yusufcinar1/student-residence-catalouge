from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Residence, Student, Reservation
from .serializers import ResidenceSerializer, StudentSerializer, ReservationSerializer

class ResidenceListView(generics.ListAPIView):
    queryset = Residence.objects.prefetch_related('rooms')
    serializer_class = ResidenceSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise ValidationError(str(e))