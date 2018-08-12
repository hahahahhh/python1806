from django.db import models

# Create your models here.
class UserModel(models.Model):
    u_name = models.CharField(max_length = 16, unique = True)
    u_token = models.CharField(max_length = 128, unique= True)


class BuyerModel(models.Model):
    b_name = models.CharField(max_length=16)
    b_icon = models.ImageField(upload_to='icons')