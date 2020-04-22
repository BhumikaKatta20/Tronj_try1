from django import forms
from django.contrib.auth.models import User
from Tronj.models import fresher_Profile,Employee,Company_Profile,emp_Education,skilltest
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save

class RegistrationForm(UserCreationForm):

	class Meta:
		model=User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'input--style-2 ','placeholder': 'Enter the user name'}),
			'first_name':forms.TextInput(attrs={'class': 'input--style-2','placeholder': 'Enter your First name'}),
			'last_name':forms.TextInput(attrs={'class': 'input--style-2','placeholder': 'Enter your Last name'}),
			'email':forms.TextInput(attrs={'class': 'input--style-2','placeholder': 'Enter your email'}),
			'password1':forms.PasswordInput(attrs={'class': 'input--style-2','placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class': 'input--style-2','placeholder': 'Re-password'}),
		}

	def save(self,commit=True):
		user=super(RegistrationForm,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		


		if commit:
			def create_profilee(sender, **kwargs):
				if kwargs['created']:
					Employee.objects.create(user=kwargs['instance'])
					emp_Education.objects.create(user=kwargs['instance'])
					skilltest.objects.create(user=kwargs['instance'])
			post_save.connect(create_profilee, sender=User)
			user.save()
		return user


class CompanyRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'input--style-2 ', 'placeholder': 'Enter the Company name'}),
			'first_name': forms.TextInput(attrs={'class': 'input--style-2', 'placeholder': 'Enter your Company First name'}),
			'last_name': forms.TextInput(attrs={'class': 'input--style-2', 'placeholder': 'Enter your Company Last name'}),
			'email': forms.TextInput(attrs={'class': 'input--style-2', 'placeholder': 'Enter the email'}),
			'password1': forms.PasswordInput(attrs={'class': 'input--style-2', 'placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class': 'input--style-2', 'placeholder': 'Re-password'}),
		}

	def save(self, commit=True):
		user = super(CompanyRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.is_staff = True

		if commit:
			def create_profile(sender, **kwargs):
				if kwargs['created']:
					CompanyProfile = Company_Profile.objects.create(user=kwargs['instance'])

			post_save.connect(create_profile, sender=User)
			user.save()
		return user


class FresherForm(forms.ModelForm):

	class Meta:
		model=fresher_Profile
		fields=(
			'user',
			'Date_of_birth',
			'Address',
			'city',
			'SSLC',
			'PUC',
			'Graduation',
			'Phone_number',
			)
	def save(self,commit=True):
		user=super(FresherForm,self).save(commit=False)
		user.Date_of_birth=self.cleaned_data['Date_of_birth']
		user.Address=self.cleaned_data['Address']
		user.city=self.cleaned_data['city']
		user.SSLC=self.cleaned_data['SSLC']
		user.PUC=self.cleaned_data['PUC']
		user.Graduation=self.cleaned_data['Graduation']	
		user.Phone_number=self.cleaned_data['Phone_number']


		if commit:
			user.save()
		return user
