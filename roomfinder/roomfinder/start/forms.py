from django import forms
from .models import Register,Login

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ('FirstName','LastName', 'UserName', 'Email', 'Password','ConfirmPassword')


class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = ('UserName','Password')