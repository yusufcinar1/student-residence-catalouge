from django.urls import path
from .views import ResidenceListView, StudentCreateView, ReservationCreateView

urlpatterns = [
    path('residences/', ResidenceListView.as_view()),
    path('students/', StudentCreateView.as_view()),
    path('reservations/', ReservationCreateView.as_view()),
]