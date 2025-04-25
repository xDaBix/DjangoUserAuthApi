from django.shortcuts import render
from django.http import HttpResponse
from .models import user_collection
from django.contrib.auth.hashers import make_password,check_password
# from .forms import UserDetailsForm



# def register_user(request):
#     if request.method == 'POST':
#         form = UserDetailsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("User registered successfully")
#     else:
#         form = UserDetailsForm()
#     return render(request, 'UsersDetails/register.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user={
            'email':email,
            'password':make_password(password)
        }
        user_collection.insert_one(user)
        return HttpResponse("User registered successfully")
    return render(request, 'UsersDetails/register.html')

# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             user = UserDetails.objects.get(email=email)
#             if check_password(password, user.password):
#                 return HttpResponse("Login successful")
#             else:
#                 return HttpResponse("Invalid credentials")
#         except UserDetails.DoesNotExist:
#             return HttpResponse("User does not exist")
#     return render(request, 'UsersDetails/login.html')