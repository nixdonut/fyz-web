from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Unit, SUBJECT_CHOICES


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit = True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UploadFileForm(forms.Form):

    file = forms.FileField()

class UploadUnitForm(forms.Form):

	name = forms.CharField(max_length = 200)
	subject = forms.ChoiceField(choices = SUBJECT_CHOICES)
	source = forms.CharField(max_length = 200)
	pdf = forms.FileField()
	solutions = forms.FileField(required = False)