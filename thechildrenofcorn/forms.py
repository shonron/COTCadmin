from django import forms

from .models import user, productname, adminaccount

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = adminaccount
        fields = [
        'firstname',
        'lastname',
        'username',
        'email',
        'password',
        'position'
    
    ]
    
class Usersignin(forms.ModelForm): 
    
    class Meta:
        model = adminaccount
        fields = [
        'username',
        'password',
        ]
        remember_me = forms.BooleanField(required = False)