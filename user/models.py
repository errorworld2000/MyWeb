from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    user_mail = models.CharField(max_length=50, default='')
    user_status = models.IntegerField()
