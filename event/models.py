from django.db import models

# Create your models here

class Event(models.Model):
    event_img= models.ImageField(upload_to='EventImage', height_field=None, width_field=None, max_length=None)