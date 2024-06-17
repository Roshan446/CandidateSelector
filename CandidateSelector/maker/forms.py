from django import forms
from django.contrib.auth.models import User
from checker.models import Candidate

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CandidateAddForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ["maker_object"]

