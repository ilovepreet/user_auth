from django.db import models


class Custmers(models.Model):
    authemail = models.EmailField(max_length=100)
    authusername = models.CharField(max_length=100)
    authpassword = models.CharField(max_length=100)
