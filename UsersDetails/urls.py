from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_user, name='register'),   
    path('login/',views.login_user, name='login'),
    path('reset_password/',views.reset_password, name='reset_password'),
    path('verifyotp/',views.verify_otp, name='verifyotp'),
]
