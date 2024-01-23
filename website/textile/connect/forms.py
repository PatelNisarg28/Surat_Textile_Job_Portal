# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, OwnerPublish, WorkerProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_owner = forms.BooleanField(required=False, initial=False)
    is_worker = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_owner', 'is_worker']

class OwnerPublishForm(forms.ModelForm):
    class Meta:
        model = OwnerPublish
        fields = ['industrial_park_name', 'owner_name', 'firm_number', 'mobile_number', 'number_of_machines',
                  'requirement_bobin_checkbox', 'requirement_bobin','requirement_tfo_checkbox', 'requirement_tfo',
                  'requirement_karigar_checkbox', 'requirement_karigar']        

class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ['name','email','phone_number','living_area','work_location','area_of_work','open_to_work','currently_working']
