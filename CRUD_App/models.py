from django.db import models

# Create your models here.


class Employe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    salary = models.FloatField()
    dob = models.DateField()


    def __str__(self) -> str:
        return self.name