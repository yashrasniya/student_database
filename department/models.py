from django.db import models
from accounts.models import User
# Create your models here.

class Image(models.Model):
    img= models.ImageField(upload_to='department_images', default= '')

class Subject(models.Model):
    name= models.CharField(max_length= 50, default= '')
    desc= models.CharField(max_length= 500, default= '')

class Labs(models.Model):
    name= models.CharField(max_length=50, default= '')
    desc= models.CharField(max_length= 5000, default='')

class Deparment(models.Model):
    branch_choice = (
        ('Computer science and engineering', 'CSE'),
        ('Electrical engineering', 'EE'),
        ('Electronics and Communications Engineering', 'ECE'),
        ('Civil Engineering', 'CE'),
        ('Mechanical engineering', 'ME'),
    )
    department_branch= models.CharField(choices=branch_choice, max_length=50, blank=True)
    department_subjects_name= models.ManyToManyField(Subject)
    department_labs_name= models.ManyToManyField(Labs)
    department_images= models.ManyToManyField(Image)
    deparment_faculty_HOD= models.ForeignKey(User, related_name= 'hod', on_delete=models.CASCADE)
    department_vision= models.CharField(max_length=50)
    department_objectives= models.CharField(max_length=50, default='')
    department_description= models.CharField(max_length=50)
    department_mission= models.CharField(max_length=50)
    department_syllabus= models.FileField(upload_to='pdfs/', default='')
    user= models.ForeignKey( User, on_delete=models.CASCADE)
    deparment_faculty= models.ManyToManyField(User, related_name= 'faculty_name')
    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})     

class NavBar(models.Model):
    title= models.CharField(max_length=50)
    link= models.URLField(max_length=2400)
    child= models.ForeignKey('self', on_delete=models.CASCADE, related_name= 'children')

class Working_communities(models.Model):
    name= models.CharField(max_length=50)
    Faculty= models.ForeignKey( User, on_delete=models.CASCADE)