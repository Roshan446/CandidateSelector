from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Checker(models.Model):
    user_object = models.OneToOneField(User, on_delete=models.CASCADE)


class Maker(models.Model):
    user_object = models.OneToOneField(User, on_delete=models.CASCADE)
    checker_object = models.ForeignKey(Checker, on_delete=models.CASCADE)

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    maker_object = models.ForeignKey(Maker, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="files")
    image = models.ImageField(upload_to="image")
    status_options = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("declined", "declined")
    )
    status = models.CharField(max_length=200, choices=status_options, default="pending")




