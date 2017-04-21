from django import forms

class RegisterForm(forms.Form):
	#firstname = forms.CharField(max_length=100, label="Firstname")
	#lastname = forms.CharField(max_length=100, label="Lastname")
	email = forms.EmailField(max_length=100, label="Email address")
	username = forms.CharField(max_length=20, label="Username")
	password = forms.CharField(min_length=6, label="Password", widget=forms.PasswordInput)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20, label="Username")
	password = forms.CharField(min_length=6, label="Password", widget=forms.PasswordInput)