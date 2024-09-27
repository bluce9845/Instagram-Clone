from django.db import models
import datetime

class DataUser(models.Model):
    username = models.CharField(max_length=255)
    second_username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    