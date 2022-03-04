from django.db import models


# Create your models here.
class Patient(models.Model):
    number = models.TextField(blank=True, null=True)


