from django import forms
from demo.models import Detals
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
class SignUpForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(render_value=True),max_length=20)
	class Meta:
		model=Detals
		fields=('email','password')
	'''def clean_recipients(self):
		
		self.cleaned_data['password']='12'
		return self.cleaned_data['password']'''
class DetailForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(render_value=True))
	class Meta:
		model=Detals
		fields=('name','email','password','phone_number')
		intials={
		'name':_('chul'),
		'email':_('chul'),
		'phone_number':_('chul'),}
	
