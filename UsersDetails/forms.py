# from .models import UserDetails
# from django import forms
# from django.contrib.auth.hashers import make_password

# class UserDetailsForm(forms.ModelForm):
#     email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
#     password=forms.CharField(required=True,min_length=8,max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#     class Meta:
#         model = UserDetails  
#         fields = ['email', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = make_password(self.cleaned_data['password'])  
#         if commit:
#             user.save()
#         return user