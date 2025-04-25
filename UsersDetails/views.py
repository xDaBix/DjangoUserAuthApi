from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user_collection
from django.contrib.auth.hashers import make_password,check_password
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# from .forms import UserDetailsForm



def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        if user_collection.find_one({'email': email}):
            messages.error(request, "Email already registered. Please log in.")
            return redirect('login')  

        
        otp = randint(10000, 99999)
        send_mail(
            'your otp', 
            f'Your OTP is {otp}', 
            settings.EMAIL_HOST_USER, 
            [email], fail_silently=False)

        request.session['otp'] = otp
        request.session['email'] = email
        request.session['password'] = password
        return redirect('verifyotp')
    
    return render(request, 'UsersDetails/register.html')



def login_user(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=user_collection.find_one({'email':email})
        if user:
            if check_password(password,user['password']):
                return HttpResponse("Login successful")
            else:
                return HttpResponse("Invalid password")
        else:
            return HttpResponse("User not found")
    return render(request, 'UsersDetails/login.html')



def reset_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        new_password=request.POST.get('new_password')
        user=user_collection.find_one({'email':email})
        if user:
            user_collection.update_one({'email':email},{'$set':{'password':make_password(new_password)}})
            return HttpResponse("Password reset successful")
        else:
            return HttpResponse("User not found")
    return render(request, 'UsersDetails/reset_password.html')


def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp1') + request.POST.get('otp2') + request.POST.get('otp3') + request.POST.get('otp4') + request.POST.get('otp5')


        
        if otp == str(request.session.get('otp')):
            email = request.session.get('email')
            password = request.session.get('password')

            
            if user_collection.find_one({'email': email}):
                messages.error(request, "Email already registered. Please log in.")
                return redirect('login')  

            
            user_collection.insert_one({
                'email': email,
                'password': make_password(password)
            })

            
            request.session.pop('otp', None)
            request.session.pop('email', None)
            request.session.pop('password', None)

            
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  

        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('verifyotp')  

    #
    return render(request, 'UsersDetails/verifyotp.html')
