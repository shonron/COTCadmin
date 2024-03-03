from django import forms

from .models import user, productname, adminaccount

class UserForm(forms.ModelForm):
    class Meta:
        model = adminaccount
        fields = [
        'name',
        'email',
        'password',
        'position'
    
    ]
    