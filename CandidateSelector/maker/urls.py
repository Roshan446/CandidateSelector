from django.urls import path, include
from maker import views


urlpatterns = [
    path("signin/", views.Signin.as_view(), name="maker-signin"),
    path("candidate/add/", views.CandidateAdd.as_view(), name="candidate-add"),
    path("candidate/status/list", views.CandidateStatusList.as_view(), name="candidate-status-list"),


]