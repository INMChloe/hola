from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    middlename = models.CharField(max_length=10)
    date_of_birth = models.DateField()

