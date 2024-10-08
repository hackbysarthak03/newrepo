from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.SignIn, name='sign-in'),
    path('register/', views.Register, name='register'),
    path('email-verification-process/<token>/', views.verify, name='verify_email'),
    path('verify-email/', views.oldVerify, name='oldverify_email'),
    path('logout/', views.signOut),
    path('forgot-password/', views.forgotPassword),
    path('update-password/<token>/', views.changePassword),
]