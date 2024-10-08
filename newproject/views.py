from django.shortcuts import render, redirect
from django.core.mail import send_mail
from department.models import Department


def home(request):
    return render(request, 'index.html')

def dept(request):
    data = Department.objects.all()
    return render(request, 'departments.html', {
        'departments':data
    })

def about(request):
    subject = 'Verify Email Address'
    message = 'Verify your Account !'
    from_email = 'care.drsaheb@gmail.com'
    recipient_list = ['vsarthak62@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return render(request, 'About.html')