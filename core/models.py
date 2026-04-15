from django.db import models
from django.core.exceptions import ValidationError


class Residence(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name="rooms")
    code = models.CharField(max_length=20)
    max_occupancy = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.residence.name} - {self.code}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 

    def __str__(self):
        return self.name


class Reservation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date")

    def __str__(self):
        return f"{self.student.name} -> {self.room.code}"