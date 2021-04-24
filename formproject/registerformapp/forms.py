from django import forms

from registerformapp.models import User

class NewuserForm(forms.ModelForm):
    class Meta:
        model =User
        fields='__all__'

