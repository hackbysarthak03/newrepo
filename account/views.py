from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from . import utils

User = get_user_model()


# Create your views here.

def SignIn(request):
    roles = User.ROLE_CHOICES
    if request.method == 'POST':
        user_role = request.POST.get('role')
        user_username = request.POST.get('email').split('@')[0]
        user_psw = request.POST.get('psw')


        try:    
            user = get_object_or_404(User, username = user_username, role = user_role)
            user = User.objects.filter(username = user_username).first()
        except:
            return render(request, 'SignIn.html', {
            'roles':roles,
            'message':'nf'
            })
        
        if user.is_email_verified == True:
            try:
                user = authenticate(username = user_username, password = user_psw)
                login(request, user)
                return redirect('/')
            except:
                return render(request, 'SignIn.html', {
                'roles':roles,
                'message':'ic'
                })
        else:
            
            return render(request, 'SignIn.html', {
            'roles':roles,
            'message':'nv'
            })

    return render(request, 'SignIn.html', {
        'roles':roles,
        'message':'new'
    })

def Register(request):
    roles = User.ROLE_CHOICES

    if request.method == 'POST':
        email = request.POST.get('email')
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        psw = request.POST.get('psw')
        cpsw = request.POST.get('cpsw')
        role = request.POST.get('role')

        
        if(len(psw) != len(cpsw)) and psw != cpsw:
            messages.error(request, 'Passwords do not match!')
            return redirect('/signin')

        try:
            print('inside try catch block')
            user = User.objects.create(
                username = email.split('@')[0],
                email = email,
                first_name = f_name,                
                last_name = l_name,
                role = role
            )
            user.set_password(psw)
            user.save()

            # Sending Email to the Client
            verification_link = request.build_absolute_uri(f"/email-verification-process/{user.unique_verify_string}/")
            subject = 'First Step towards a healthy lifestyle! - Email Verification from Dr.Saheb!'
            message = f'Hey {f_name} {l_name}, Greetings from Dr.Saheb! Please Verify your Email through the following Link: {verification_link}'
            from_email = 'care.drsaheb@gmail.com'
            recipient_list = [f'{email}']
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'Register.html', {'roles':roles, 'section': 'verify'})
            
            # messages.success(request, 'Account Created Sucessfully ✅')
        except:
            # messages.error(request, 'Account already exist with the Email')
            return redirect('/register')

    print('new new')
    return render(request, 'Register.html', {
        'roles':roles,
        'section': 'new'
    })

def verify(request, token):
    try:
        
        user = get_object_or_404(User, unique_verify_string=token)
        user.is_email_verified = True
        user.save()

        return render(request, 'Register.html', {
            'section': 'success'
        })
    
    except:
        return render(request, 'Register.html', {
            'section': 'error'
        })

def oldVerify(request):
    roles = User.ROLE_CHOICES

    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_username = request.POST.get('email').split('@')[0]

        try:    
            user = get_object_or_404(User, username = user_username)
            user = User.objects.filter(username = user_username).first()
            print(user)
        except:
            return render(request, 'Verify.html', {
            'tag':'nf'
            })
        
        verification_link = request.build_absolute_uri(f"/email-verification-process/{user.unique_verify_string}/")
        subject = 'First Step towards a healthy lifestyle! - Email Verification from Dr.Saheb!'
        message = f'Hey {user.first_name} {user.last_name}, Greetings from Dr.Saheb! Please Verify your Email through the following Link: {verification_link}'
        from_email = 'care.drsaheb@gmail.com'
        recipient_list = [f'{user_email}']
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'Verify.html', {
            'tag':'su'
        })


    return render(request, 'Verify.html', {
        'tag':'new'
    })

def signOut(request):
    logout(request)
    return redirect('/')

def changePassword(request, token):
    roles = User.ROLE_CHOICES
    try:
        user = get_object_or_404(User, passwordChangeField = token)
    except:
        return render(request, 'NewPassword.html', {
        'tag':'nf'
        })
    
    if request.method == 'POST':
        psw = request.POST.get('psw')
        cpsw = request.POST.get('cpsw')

        if psw != cpsw:
            return render(request, 'NewPassword.html', {
            'tag':'dm'
            })
    
        user.set_password(psw)
        user.save()

        subject = 'Hey! You\'re back .. Password Changed on Dr.Saheb!'
        message = f'Hey {user.first_name} {user.last_name}, Greetings from Dr.Saheb! We\'ve noticed that you\'ve changed the password for your account recently. Glad to hear that you\'re back on our platform!'
        from_email = 'care.drsaheb@gmail.com'
        recipient_list = [f'{user.email}']
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'NewPassword.html', {
            'tag':'pc'
        })
        
    return render(request, 'NewPassword.html', {
        'tag':'new'
    })
    

def forgotPassword(request):
    roles = User.ROLE_CHOICES

    if request.method == 'POST':
        user_role = request.POST.get('role')
        user_email = request.POST.get('email')
        user_username = request.POST.get('email').split('@')[0]

        try:    
            user = get_object_or_404(User, username = user_username, role = user_role)
            user = User.objects.filter(username = user_username).first()
        except:
            return render(request, 'PasswordChange.html', {
            'roles':roles,
            'tag':'nf'
            })
        
        link = utils.generate_random_alphanumeric_string(128)
        user.passwordChangeField = link
        user.save()

        verification_link = request.build_absolute_uri(f"/update-password/{link}/")
        subject = 'Password Change Request - Dr.Saheb!'
        message = f'Hey {user.first_name} {user.last_name}, Greetings from Dr.Saheb! We noticed you facing difficulty in signing in to your account. Don\'t worry, Click on the following link: {verification_link}'
        from_email = 'care.drsaheb@gmail.com'
        recipient_list = [f'{user_email}']
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'PasswordChange.html', {
            'roles':roles,
            'tag':'su'
        })


    return render(request, 'PasswordChange.html', {
        'roles':roles,
        'tag':'new'
    })