from django.shortcuts import render
from django.http import HttpResponse
from .models import user_collection
from django.contrib.auth.hashers import make_password,check_password
# from .forms import UserDetailsForm





def register_user(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        if user_collection.find_one({'email':email}):
            return HttpResponse("User already exists")
        

        user={
            'email':email,
            'password':make_password(password)
        }
        user_collection.insert_one(user)
        return HttpResponse("User registered successfully")
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
