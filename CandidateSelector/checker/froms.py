from django import forms

class SiginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
