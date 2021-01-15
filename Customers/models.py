from django.db import models


# Create your models here.
class Customers(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Current_Balance = models.BigIntegerField(max_length=100000000000)


class Transfers(models.Model):
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    Amount = models.BigIntegerField(max_length=100000000000)
    date = models.DateField()
