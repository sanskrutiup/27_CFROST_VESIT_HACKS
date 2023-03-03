from django.db import models

# Create your models here.
class Reg(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    contact = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    userType = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    def __str__(self):
        return self.email