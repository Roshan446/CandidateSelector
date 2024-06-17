from django.shortcuts import render, redirect
from checker.models import Checker, Candidate, Maker
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from maker.forms import SigninForm, CandidateAddForm
from django.views import View

# Create your views here.


class Signin(View):
    def get(self, request, *args, **kwargs):
        form = SigninForm()
        return render(request, "signin.html", {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = SigninForm()
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_auth = authenticate(request, username=username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect("candidate-status-list")
        else:
            return render(request, "signin.html", {"form":form})

class CandidateAdd(View):
    def get(self, request, *args, **kwargs):
        form = CandidateAddForm()
        return render(request, "candidate.add.html", {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = CandidateAddForm(request.POST, request.FILES)
        if form.is_valid():
            maker_obj = Maker.objects.get(user_object =request.user)
            Candidate.objects.create(**form.cleaned_data, maker_object=maker_obj)
            return redirect("candidate-status-list")
        else:
            return render(request, "signin.html", {"form":form})

class CandidateStatusList(View):
    def get(self, request, *args, **kwargs):
        qs = Candidate.objects.filter(maker_object__user_object = request.user)
        return render(request, "candidate.status.html", {"candidates":qs})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("base")

class BaseView(View):
    def get(self,request, *args, **kwargs):
        return render(request, "base.html",)

