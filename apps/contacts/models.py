from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name
