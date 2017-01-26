from django import forms
from django.contrib.auth.models import User
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout,Submit,Field
#from crispy_forms.bootstrap import PrependedText,PrependedAppendedText,FormActions

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label='Username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': '*****'}))
    
    def clean_username(self):
        cd = self.cleaned_data
        if cd['username'] is None:
            raise forms.ValidationError('\nThis field is required.\n')   


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30,label='Username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    email    = forms.EmailField(max_length=254,label='E-Mail',widget=forms.TextInput(attrs={'placeholder': 'E-Mail ID'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    pwdcnf   = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','email','password',)
        
    def clean_first_name(self):
        cd = self.cleaned_data
        if cd['first_name'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        return cd['first_name']
    
    def clean_pwdcnf(self):
        cd = self.cleaned_data
        if cd['password'] != cd['pwdcnf']:
            raise forms.ValidationError('\nPasswords do not match. Please enter again.\n')
        return cd['pwdcnf']
        
    def clean_username(self):
        cd = self.cleaned_data
        if cd['username'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        if User.objects.filter(username=cd['username']).count():
            raise forms.ValidationError('\nUsername already exists.\n')
        return cd['username']
        
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).count():
            raise forms.ValidationError('\nThe given E-Mail ID is already registered.\n')
        return cd['email']