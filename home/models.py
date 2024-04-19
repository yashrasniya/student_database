from django.db import models

class Mission(models.Model):
    content = models.TextField()

class Vision(models.Model):
    content = models.TextField()

class ActivityImage(models.Model):
    image = models.ImageField(upload_to='activity_images/')

    def __str__(self):
        return f"Activity Image {self.pk}"

class Announcement(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

class FooterLink(models.Model):
    title = models.CharField(max_length=200)
    items = models.TextField()

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class News(models.Model):
    image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    title = models.CharField(max_length=255)
    # dis = models.TextField()

class Event(models.Model):
    text = models.CharField(max_length=255)

class Contact(models.Model):
    email = models.EmailField()
    address = models.TextField()
    aicte_feedback_link = models.URLField()
    helpline_number = models.CharField(max_length=15)
    
class TopHeaderLink(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link_text = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)


class SliderImage(models.Model):
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
