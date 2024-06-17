from django.shortcuts import render, redirect
from checker.models import Candidate, Maker, User, Checker
from django.views import View
from django.contrib.auth import login, logout, authenticate
from checker.froms import SiginForm
# Create your views here.

class Signin(View):
    def get(self, request, *args, **kwargs):
        form = SiginForm()
        return render(request,"signin.html", {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = SiginForm()
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        print(user_name, password)
        user_auth = authenticate(request, username = user_name, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect("list-candidates")
        else:
            return render(request,"signin.html", {"form":form})

class ListAllCandidates(View):
    def get(self, request, *args, **kwargs):
        qs = Candidate.objects.filter(maker_object__checker_object__user_object = request.user, status = "pending")
        return render(request, "candidates_list.html", {"candidates":qs})


class CandidateApprove(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        candidate_object = Candidate.objects.get(id=id)
        candidate_object.status = "accepted"
        candidate_object.save()
        return redirect("list-candidates")

class CandidateDecline(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        candidate_object = Candidate.objects.get(id=id)
        candidate_object.status = "declined"
        candidate_object.save()
        return redirect("list-candidates")

class AllMakers(View):
    def get(self, request, *args, **kwargs):
        qs = Maker.objects.filter(checker_object__user_object = request.user)
        return render(request, "maker_list.html", {"makers":qs})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("checker-signin")

    






        
