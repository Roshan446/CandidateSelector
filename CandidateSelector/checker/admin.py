from django.contrib import admin
from django.contrib.auth.models import User
from checker.models import Maker, Checker, Candidate
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Checker)
admin.site.register(Maker)




