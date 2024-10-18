
from django.urls import path, include
from . import views

urlpatterns = [
    path('my-bookings/', views.myBookings),
    path('book/<id>', views.bookDoctor),
    path('my-bookings/invite/<pr_no>', views.invitePatient),
    path('meet-doctor/<pr_no>', views.meetDoctor),
    path('get-prescription/<pr_no>', views.getPrescription),
    path('checkup-done/<pr_no>', views.prescribePatient),
]
