from django.db import models

# Create your models here.
class Calculator(models.Model):
    number = models.CharField(max_length=10)