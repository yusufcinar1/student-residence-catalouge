from rest_framework import serializers
from .models import Residence, Student, Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'code', 'max_occupancy']


class ResidenceSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Residence
        fields = ['id', 'name', 'city', 'rooms']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'student', 'room', 'start_date', 'end_date']

    def validate(self, data):
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError(
                "End date must be after start date."
            )

        return data