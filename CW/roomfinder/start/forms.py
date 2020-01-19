from django import forms
from .models import Register

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ('FirstName','LastName', 'UserName', 'Email', 'Password','ConfirmPassword')