from django import forms
from django.db.models import fields
from .models import *
from .models import UserDetail

class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['account_image'] 
class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
class ProfileUpdate(forms.ModelForm):
    class   Meta:
        model = UserDetail
        fields = ['email','image']
