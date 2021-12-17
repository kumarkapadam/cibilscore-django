from django import forms
from cibilscoreapp.models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

class CibilForm(forms.Form):
    salary=forms.IntegerField()
    

