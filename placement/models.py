from django.db import models

class PlacementCell(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Recruiter(models.Model):
    logo = models.ImageField(upload_to='recruiter_logos')
    candidates = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.candidates

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    placed = models.CharField(max_length=200)
    sal = models.CharField(max_length=100)
    image = models.ImageField(upload_to='achievement_images')

    def __str__(self):
        return self.name
    
class Cell(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='placement_images')
    description = models.TextField()

    def __str__(self):
        return self.title

class Head(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='placements/')

    def __str__(self):
        return self.title

class Subtitle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
