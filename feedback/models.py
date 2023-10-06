from django.db import models


# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE ,blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=20000, blank=True)
