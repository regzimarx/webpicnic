from django import forms

class RegisterForm(forms.Form):
	#firstname = forms.CharField(max_length=100, label="Firstname")
	#lastname = forms.CharField(max_length=100, label="Lastname")
	email = forms.EmailField(
		max_length=100,
		label="Email address",
		widget=forms.TextInput(attrs={'class': 'form-control margin-bottom-10',})
	)
	username = forms.CharField(
		max_length=20,
		label="Username",
		widget=forms.TextInput(attrs={'class': 'form-control margin-bottom-10',})
	)
	password = forms.CharField(
		min_length=6,
		label="Password",
		widget=forms.PasswordInput(attrs={'class': 'form-control margin-bottom-10',})
	)

class LoginForm(forms.Form):
	username = forms.CharField(
		max_length=20,
		label="Username",
		widget=forms.TextInput(attrs={'class': 'form-control margin-bottom-10',})
	)
	password = forms.CharField(
		min_length=6,
		label="Password",
		widget=forms.PasswordInput(attrs={'class': 'form-control margin-bottom-10',})
	)