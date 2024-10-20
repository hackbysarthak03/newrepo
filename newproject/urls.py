from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('', views.home),
    path('who-we-are/', views.about),
    path('departments/', views.dept),
    path('departments/<dept>', views.getDoctors),
    path('profile/', views.myProfile),
    path('profile/update/', views.updateProfile),
    path('profile/updateStatus/', views.updateStatus),
    path('profile/join-meet/<roomID>', views.joinDoctorMeet),
    path('', include('account.urls')),
    path('', include('blogs.urls')),
    path('', include('bookings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
