from rest_framework import serializers
from .models import Residence, Student, Reservation


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'