from django.db import models


# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_again = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class LoginModels(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
