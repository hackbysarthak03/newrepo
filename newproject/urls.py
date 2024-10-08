from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('', views.home),
    path('who-we-are/', views.about),
    path('departments/', views.dept),
    path('', include('account.urls'))
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
