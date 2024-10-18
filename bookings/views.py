from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from doctor.models import DoctorProfile
from patient.models import PatientProfile
from .models import Booking
from django.core.mail import send_mail
from django.http import HttpResponse
from account.utils import generate_random_alphanumeric_string
from datetime import datetime
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

@login_required(login_url='/sign-in/')
def myBookings(request):
    if request.user.role == 'doctor':
        doctor = DoctorProfile.objects.filter(user__username = request.user.username).first()
        books = Booking.objects.filter(doctor_profile = doctor)
        return render(request, 'DoctorBooking.html',{
            'books':books
        })
    
    elif request.user.role == 'patient':
        patient = PatientProfile.objects.filter(user__username = request.user.username).first()
        books = Booking.objects.filter(patient_profile = patient)
        print(books)
        return render(request, 'PatientBooking.html', {
            'books':books
        })
    else:
        pass

@login_required(login_url='/sign-in/')
def bookDoctor(request, id):
    doctor = DoctorProfile.objects.filter(id = id).first()
    patient = PatientProfile.objects.filter(user__username = request.user.username).first()
    pr_no = generate_random_alphanumeric_string(9) + str(doctor.id) + str(patient.id)

    # Room Id = pr_no

    book = Booking.objects.create(
        doctor_profile = doctor, 
        patient_profile = patient,
        pr_no = str(pr_no.upper())
    )

    book.save()

    try:
        subject = 'Booking Successful on Dr.Saheb!'
        message = f'Hey {patient.user.first_name} {patient.user.last_name}, Appointment booked at {datetime.now()} with Dr.{doctor.user.first_name} {doctor.user.last_name} with Appointment No. {pr_no.upper()}. We will shortly reflect you back once Our Physician is free! Have a healthy life 😎 - Team Dr.Saheb!'
        from_email = 'care.drsaheb@gmail.com'
        recipient_list = [f'{patient.user.email}']
        send_mail(subject, message, from_email, recipient_list)
    except:
        pass

    return redirect('/my-bookings/')

@login_required(login_url='/sign-in/')
def invitePatient(request, pr_no):
    book = Booking.objects.filter(pr_no = pr_no).first()
    book.status = 1
    book.save()

    doctor = DoctorProfile.objects.filter(user__username = request.user.username).first()
    doctor.room_id = book.pr_no
    doctor.save()

    try:
        link = request.build_absolute_uri(f"/meet-doctor/{doctor.room_id}/")
        subject = 'Booking Successful on Dr.Saheb!'
        message = f'Hey {book.patient_profile.user.first_name} {book.patient_profile.user.last_name}, Invite for your Booked Appointment on {book.booked_on} is : {link}  Have a healthy life 😎 - Team Dr.Saheb!'
        from_email = 'care.drsaheb@gmail.com'
        recipient_list = [f'{book.patient_profile.user.email}']
        send_mail(subject, message, from_email, recipient_list)
    except:
        pass
    

    return redirect(f'/profile/join-meet/{doctor.room_id}')

@login_required(login_url='/sign-in/')
def meetDoctor(request, pr_no):

    if request.user.role == 'patient':
        current_user = request.user
        try:
            return render(request, 'VideoCall.html', {
                    'room_id':pr_no,
                    'user':current_user
                })
        except:
            return HttpResponse('Incorrect Link')

@login_required(login_url='/sign-in/')     
def prescribePatient(request, pr_no):
    if request.method == 'POST':
        book = Booking.objects.filter(pr_no = pr_no).first()
        book.prescription = request.POST.get('prescription-content')
        book.status = 2
        book.prescribed_date = datetime.now()
        book.save()

        try:
            subject = f'Checkup Successful #{book.pr_no} on Dr.Saheb!'
            message = f'Hey {book.patient_profile.user.first_name} {book.patient_profile.user.last_name}, Checkup Successful for Appointment No. {book.pr_no}. Visit MyBookings Section on Dr.Saheb! to get the Prescription. Have a healthy life 😎 - Team Dr.Saheb!'
            from_email = 'care.drsaheb@gmail.com'
            recipient_list = [f'{book.patient_profile.user.email}']
            send_mail(subject, message, from_email, recipient_list)
        except:
            pass
    
        return redirect('/my-bookings/')
    
def getPrescription(request, pr_no):
    book = Booking.objects.filter(pr_no = pr_no).first()

    return render(request, 'pdf_template.html', {
        'booking':book
    })