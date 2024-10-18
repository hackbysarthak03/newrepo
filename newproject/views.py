from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from department.models import Department
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from doctor.models import *
from patient.models import *
import random
from doctor.models import DoctorProfile

User = get_user_model()

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

@login_required(login_url='/sign-in/')
def myProfile(request):
    root_user = request.user
    print(root_user)
    try:
        if root_user.role == 'doctor':
            current_user = DoctorProfile.objects.filter(user__username = root_user.username).first()
            
        else:
            current_user = PatientProfile.objects.filter(user__username = root_user.username).first()
            
    except:
        return False
    
    return render(request, 'MyProfile.html', {
        'role_data' : current_user
    })

@login_required(login_url='/sign-in/')
def joinDoctorMeet(request, roomID):
    if request.user.role == 'doctor':
        current_user = User.objects.filter(username = request.user).first()
        
        return render(request, 'VideoCall.html', {
            'room_id':roomID,
            'user':current_user
        })
    else:
        return HttpResponse('You are not allowed to Join')


@login_required(login_url='/sign-in/')
def updateProfile(request):

    current_user = request.user
    allDept = Department.objects.all()

    if request.method == 'POST':
        if current_user.role == 'doctor':
            doctor = DoctorProfile.objects.filter(user__username = request.user.username).first()
            department = Department.objects.filter(name = request.POST.get('dept')).first()
            doctor.department = department
            doctor.degree = request.POST.get('degree')
            doctor.reg_no = request.POST.get('reg_no')
            doctor.specialist = request.POST.get('specialist_in')
            doctor.hospital = request.POST.get('hospital')
            doctor.hospital_district = request.POST.get('district')
            doctor.hospital_state = request.POST.get('state')
            doctor.desc = request.POST.get('desc')
            doctor.save()


        if current_user.role == 'patient':
            patient = PatientProfile.objects.filter(user__username = current_user.username).first()
            patient.healthCard = request.POST.get('health-card')
            patient.district = request.POST.get('district')
            patient.state = request.POST.get('state')
            patient.desc = request.POST.get('desc')
            patient.save()

        user = User.objects.filter(username = current_user.username).first()
        if request.FILES.get('avatar'):
            user.avatar = request.FILES.get('avatar')
        else:
            pass

        user.save()
        
        return redirect('/profile/')
        
    return render(request, 'MyProfileUpdate.html', {
        'departments':allDept
    })

@login_required(login_url='/sign-in/')
def updateStatus(request):
    status = int(request.GET.get('status'))
    if status == 100:
        print('manageBlogs')
        return redirect('/my-blogs/')
    
    elif status == 200:
        current_user = request.user
        doctor = DoctorProfile.objects.filter(user__username = current_user.username).first()
        doctor.avail = not doctor.avail
        doctor.save()
        return redirect('/profile/')
    
    elif status == 300:
        roomID = str(request.user) + str(random.randint(1, 10000))
        doctor = DoctorProfile.objects.filter(user__username = request.user).first()
        doctor.room_id = roomID
        doctor.save()

        return redirect(f'/profile/join-meet/{roomID}')
    
    else:
        return HttpResponse('Status Code Not Found!')

def getDoctors(request, dept):
    department = Department.objects.filter(name = dept).first()
    doctors = DoctorProfile.objects.filter(department = department)

    print(doctors)
    data = {
        'doctors':doctors,
        'department':dept
    }

    return render(request, 'Doctors.html', data)