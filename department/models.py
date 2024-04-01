from django.db import models

# Create your models here.

class Deparment(models.Model):
    branch_choice = (
        ('Computer science and engineering', 'CSE'),
        ('Electrical engineering', 'EE'),
        ('Electronics and Communications Engineering', 'ECE'),
        ('Civil Engineering', 'CE'),
        ('Mechanical engineering', 'ME'),
    )
    department_branch= models.CharField(choices=branch_choice, max_length=50, blank=True)
    department_subjects= models.CharField(max_length=50, default='')
    department_labs= models.CharField(max_length=50)
    department_syllabus= models.FileField(upload_to='pdfs/', default='')
    department_images= models.ImageField(upload_to= 'department_image', default= '')

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})    

class Faculty(models.Model):
    department_name= models.CharField(max_length=50, default= '')
    deparment_faculty= models.CharField(max_length=50, default= '')
    deparment_faculty_role= models.CharField(max_length=50, default= '')
    deparment_faculty_subject= models.CharField(max_length=50, default='')
    deparment_faculty_number= models.CharField(max_length=10, unique=True)
    deparment_faculty_image= models.ImageField(upload_to='Profile', default='')