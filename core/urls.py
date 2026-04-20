from django.urls import path
from .views import ResidenceListView, StudentListCreateView, ReservationListCreateView

urlpatterns = [
    path('residences/', ResidenceListView.as_view()),
    path('students/', StudentListCreateView.as_view()),
    path('reservations/', ReservationListCreateView.as_view()),
]