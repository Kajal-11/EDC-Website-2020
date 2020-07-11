from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User, StudentProfile, StartupProfile

class StudentRegisterForm(UserCreationForm):
	email 	= forms.EmailField()
	city 	= forms.CharField(max_length=40)
	college = forms.CharField(max_length=50)
	name 	= forms.CharField(max_length=60)
	contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False) 
	
	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'contact', 'college', 'city', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data


class StartupRegisterForm(UserCreationForm):
    startup_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    founders = forms.CharField(max_length=150)
    about = forms.CharField(max_length=500, widget=forms.TextInput({}), required=False)
    city = forms.CharField(max_length=40)
    field_of_work = forms.CharField(max_length=50)
    website = forms.URLField(max_length=254)
    startup_logo = forms.ImageField()
    contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False)
	
    class Meta():	
        model = User
        fields = ['startup_name', 'email', 'contact', 'about', 'founders', 'city', 'field_of_work', 'website', 'startup_logo', 'password1','password2']

    @transaction.atomic
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Account with this email already exists")
        return self.cleaned_data


class StudentUpdateForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['city', 'college', 'contact']

class StartupUpdateForm(forms.ModelForm):
	class Meta:
		model = StartupProfile
		fields = ['startup_name', 'about', 'founder', 'city', 'field_of_work', 'website', 'contact', 'image']