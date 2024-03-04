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
    
# class CarouselImage(models.Model):
#     image = models.ImageField(upload_to='carousel_images/')

#     def __str__(self):
#         return f"Carousel Image {self.pk}"

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


