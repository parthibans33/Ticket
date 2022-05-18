from django.db import models

# Create your models here.


class LoginModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)
    class Meta:
        db_table = 'login_table'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

